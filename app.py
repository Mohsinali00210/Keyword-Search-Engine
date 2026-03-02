from flask import Flask,send_file,render_template_string,flash, render_template, request, redirect, url_for, session, jsonify, send_from_directory
import os
import pandas as pd
import sqlite3
from datetime import datetime
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from spellchecker import SpellChecker
from rapidfuzz.distance import Levenshtein
# import language_tool_python
from whoosh.highlight import HtmlFormatter, Highlighter
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.writing import AsyncWriter
import chardet
import bcrypt
from textblob import TextBlob


# Flask app setup
app = Flask(__name__)
app.secret_key = "supersecretkey"
spell = SpellChecker()
custom_words = set()  # User-defined custom dictionary
# tool = language_tool_python.LanguageToolPublicAPI('en-US')

# Load custom dictionary if available
try:
    with open('custom_words.txt', 'r') as file:
        custom_words = file.read().splitlines()
        spell.word_frequency.load_words(custom_words)
except FileNotFoundError:
    custom_words = []
# Define paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
INDEX_DIR = os.path.join(BASE_DIR, "indexdir")
DATABASE = os.path.join(BASE_DIR, "documents.db")
EXPORT_FOLDER = os.path.join(BASE_DIR, "backup")

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(INDEX_DIR, exist_ok=True)

# Configure Flask app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DATABASE'] = DATABASE

# Whoosh index initialization
def create_index():
    schema = Schema(filename=ID(stored=True), content=TEXT(stored=True))
    if not os.path.exists(INDEX_DIR) or not os.listdir(INDEX_DIR):
        ix = create_in(INDEX_DIR, schema)
    else:
        ix = open_dir(INDEX_DIR)
    return ix

# Initialize Index
ix = create_index()

@app.route("/spell")
def spells():
    return render_template("spell.html")


# @app.route('/check', methods=['POST'])
# def check():
#     data = request.get_json()
#     text = data.get("text", "")

#     matches = tool.check(text)
#     results = []

#     for match in matches:
#         word = text[match.offset: match.offset + match.errorLength]
#         if word in custom_words:
#             continue  # Ignore known custom words

#         if match.ruleIssueType in ['misspelling', 'grammar']:
#             results.append({
#                 "word": word,
#                 "suggestions": match.replacements[:5],  # Top 5 suggestions
#                 "message": match.message,
#                 "type": match.ruleIssueType
#             })

#     return jsonify(results)
spell = SpellChecker()


@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    text = data.get("text", "")
    words = text.split()
    results = []

    for word in words:
        if word.lower() in custom_words:
            continue

        corrected_word = str(TextBlob(word).correct())
        if corrected_word.lower() != word.lower():
            suggestions = list(spell.candidates(word))
            if word.lower() in suggestions:
                suggestions.remove(word.lower())
            results.append({
                "word": word,
                "suggestions": suggestions[:5],
                "message": f"Possibly misspelled word: '{word}'",
                "type": "misspelling"
            })

    return jsonify(results)
custom_words = set()  # make sure this is at the top

@app.route("/add_word", methods=["POST"])
def add_words():
    data = request.get_json()
    word = data.get("word")
    if word:
        custom_words.add(word.lower())
    return jsonify({"success": True, "message": f"'{word}' added to dictionary."})


# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            upload_date TEXT NOT NULL,
            username TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

#Check Spelling
@app.route('/check_spelling', methods=['POST'])
def check_spelling():
    data = request.json
    words = data.get("text", "").split()
    
    if not words:
        return jsonify({"error": "No text provided"}), 400  # Bad Request

    misspelled= {
    word: list(spell.candidates(word) or [])  # Ensure it's always iterable
    for word in words if word not in spell and word not in custom_words
}

    
    return jsonify(misspelled)


@app.route('/check-spelling', methods=['POST'])
def check_spellings():
    text = request.json.get('text', '')
    
    words = text.split()
    misspelled = []

    for word in words:
        if word.lower() not in spell:
            misspelled.append(word)
    
    suggestions = {}
    for word in misspelled:
        # Convert set to list before returning
        suggestions[word] = list(spell.candidates(word.lower()))

    return jsonify(suggestions)

# Endpoint to add a word to the dictionary
@app.route('/add-to-dictionarys', methods=['POST'])
def add_to_dictionarys():
    word = request.json.get('word', '')
    if word:
        spell.word_frequency.add(word.lower())
        return jsonify({"message": f"Word '{word}' added to the dictionary."}), 200
    return jsonify({"message": "No word provided."}), 400

@app.route("/get_suggestions", methods=["POST"])
def get_suggestions():
    data = request.get_json()
    word = data.get("word", "")
    
    if word:
        suggestions = list(spell.candidates(word))
        return jsonify({"suggestions": suggestions})
    
    return jsonify({"suggestions": []})
@app.route("/add_to_dictionary", methods=["POST"])
def add_to_dictionary():
    data = request.get_json()
    word = data.get("word", "")
    
    if word:
        custom_words.add(word)
    
    return jsonify({"message": "Word added successfully!"})

# Home route
@app.route('/')
def home():
    return render_template('index.html', username=session.get('username'))
@app.route('/backup')
def backup():
    return render_template('backup.html', username=session.get('username'))
@app.route("/export/sql", methods=["GET"])
def export_sql():
    try:
        conn = sqlite3.connect(DATABASE)
        sql_dump_file = os.path.join(EXPORT_FOLDER, "backup.sql")
        
        with open(sql_dump_file, "w") as f:
            for line in conn.iterdump():
                f.write(f"{line}\n")
        
        conn.close()
        return send_file(sql_dump_file, as_attachment=True)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# **Export Users Table as CSV**
@app.route("/export/csv", methods=["GET"])
def export_csv():
    try:
        conn = sqlite3.connect(DATABASE)
        df = pd.read_sql_query("SELECT * FROM users", conn)
        csv_file = os.path.join(EXPORT_FOLDER, "backup_users.csv")
        
        df.to_csv(csv_file, index=False)
        conn.close()
        
        return send_file(csv_file, as_attachment=True)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# **Import SQL Dump into Database**
@app.route("/import/sql", methods=["POST"])
def import_sql():
    try:
        sql_dump_file = request.files["file"]
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        print(sql_dump_file.filename)
        file_content = sql_dump_file.read().decode("utf-8")
        
        # **Modify SQL commands to prevent duplicates**
        sql_script = file_content.replace("INSERT INTO", "INSERT OR IGNORE INTO")
        sql_script = sql_script.replace("CREATE TABLE", "CREATE TABLE IF NOT EXISTS")

        cursor.executescript(sql_script)

        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Database imported, skipping duplicates!"})

    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": str(e)}), 500


# **Import CSV into Users Table**
@app.route("/import/csv", methods=["POST"])
def import_csv():
    try:
        csv_file = request.files["file"]
        df = pd.read_csv(csv_file)
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        for _, row in df.iterrows():
            # Check if the record already exists
            cursor.execute("SELECT COUNT(*) FROM users WHERE email = ?", (row["email"],))
            exists = cursor.fetchone()[0]

            if exists == 0:  # Insert only if the record does NOT exist
                cursor.execute(
                    "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                    (row["username"], row["email"], row["password"])
                )

        conn.commit()
        conn.close()

        return jsonify({"status": "success", "message": "CSV data imported, skipping duplicates!"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



@app.route("/profile")
def profile():
    if "username" not in session:
        flash("Please log in first!", "error")
        return redirect(url_for("login"))

    conn = sqlite3.connect(DATABASE)
    user = conn.execute("SELECT * FROM users WHERE username = ?", (session.get("username"),)).fetchone()
    conn.close()
    
    return render_template("profile.html", user=user,username=session.get('username'))

# **Edit Profile**
@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "username" not in session:
        flash("Please log in first!", "error")
        return redirect(url_for("login"))

    conn = sqlite3.connect(DATABASE)
    user = conn.execute("SELECT * FROM users WHERE username = ?", (session["username"],)).fetchone()
    
    if request.method == "POST":
        new_username = request.form["username"].strip()
        new_email = request.form["email"].strip()
        new_password = request.form["password"].strip()
        
        # hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")

        conn.execute(
            "UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?",
            (new_username, new_email, new_password, user[0]),
        )
        conn.commit()
        conn.close()

        session["username"] = new_username
        flash("Profile updated successfully!", "success")
        return redirect(url_for("profile"))

    conn.close()
    return render_template("edit_profile.html", user=user)

@app.route('/view/<filename>')
def view_file(filename):
    file_path = f"uploads/{filename}"

    if filename.endswith('.csv'):
        try:
            encoding = detect_encoding(file_path)
            df = pd.read_csv(file_path, encoding=encoding)
            html_table = df.to_html(classes='table table-striped')
            return render_template('view_csv.html', content=html_table)

        except Exception as e:
            return f"Error loading CSV file: {str(e)}", 404

    elif filename.endswith('.txt'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return render_template('view_txt.html', content=content)
        except Exception as e:
            return f"Error loading text file: {str(e)}", 404

    else:
        return "Unsupported file type.", 400


# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


        conn = sqlite3.connect(DATABASE, timeout=10)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            conn.close()
            return jsonify({"status": "error", "message": "Email already registered!"})

        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
        conn.commit()
        conn.close()

        return jsonify({"status": "success", "message": "Registration successful! Please login."})
    return render_template('register.html')


@app.route('/UserList')
def UserList():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return render_template("UserList.html", users=users,username=session.get('username'))

@app.route('/UserCreate', methods=['GET', 'POST'])
def UserCreate():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect(DATABASE, timeout=10, check_same_thread=False)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        if c.fetchone():
            conn.close()
            return jsonify({"status": "error", "message": "Email already registered!"})
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()
        return redirect(url_for('UserList'))
    return render_template("UserCreate.html")

@app.route('/UserUpdate/<int:user_id>', methods=['GET', 'POST'])
def UserUpdate(user_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        c.execute("UPDATE users SET username=?, email=?, password=? WHERE id=?", (username, email, password, user_id))
        conn.commit()
        conn.close()
        return redirect(url_for('UserList'))
    else:
        c.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = c.fetchone()
        conn.close()
        return render_template("UserUpdate.html", user=user)

@app.route('/UserDelete/<int:user_id>')
def UserDelete(user_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('UserList'))

@app.route('/admin')
def admin():
    if session.get("email") != "admin@gmail.com":
        return redirect(url_for('login'))
    return render_template('admin2.html', username=session.get("username"))



@app.route('/DocumentList')
def DocumentList():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM documents')
    uploads = c.fetchall()
    conn.close()
    print(uploads)
    return render_template('DocumentList.html', uploads=uploads, username=session.get("username"))

@app.route('/DeleteDocument/<int:id>')
def DeleteDocument(id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DELETE FROM documents WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('DocumentList'))
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user:
            hashed_password = user[3]  # string from DB
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                session['username'] = user[1]  # username
                session['email'] = user[2]     # email

                if user[2] == "admin@gmail.com":
                    return redirect(url_for('admin'))
                else:
                    return redirect(url_for('home'))

        error = {"status": "error", "message": "Invalid email or password!"}
        return render_template('login.html', error=error)

    return render_template('login.html')




@app.route('/searchhistory', methods=['GET'])
def searchhistory():
     
    conn = sqlite3.connect(DATABASE, timeout=10)
    username=session.get('username')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SearchHistory WHERE user_name = ? ", (username,))
    history = cursor.fetchall()
    conn.close()
    print(history)

    return render_template('history.html',history=history,username=username) 

# User logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Function to index a document
def detect_encoding(file_path):
    with open(file_path, "rb") as f:
        raw_data = f.read()
        detected_encoding = chardet.detect(raw_data)["encoding"]
    return detected_encoding

def index_document(filename,file_path):
    print(filename)
    with ix.writer() as writer:
        if filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            writer.add_document(filename=filename, content=content)
        
        elif filename.endswith(".csv"):
            encoding = detect_encoding(file_path)

            df = pd.read_csv(file_path, encoding=encoding)
            csv_content = df.to_string()
            writer.add_document(filename=filename, content=csv_content)

# Search Route
@app.route("/search", methods=["GET"])
def search():
    query_text = request.args.get("query", "").strip()
    if not query_text:
        return jsonify({"status": "error", "message": "No search query provided"}), 400
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO SearchHistory (query, user_name) VALUES (?, ?)', (query_text, session.get('username')))
    conn.commit()
    conn.close()
    ix = open_dir(INDEX_DIR)
    with ix.searcher() as searcher:
        parser = QueryParser("content", ix.schema)
        try:
            query = parser.parse(query_text)
        except Exception:
            return jsonify({"status": "error", "message": "Invalid search query"}), 400
        results = searcher.search(query, limit=10)
        formatter = HtmlFormatter(tagname="span", classname="highlight")
        highlighter = Highlighter(formatter=formatter)
        unique_results = {r["filename"]: r.highlights("content") for r in results}
        search_results = [{"filename": k, "snippet": v} for k, v in unique_results.items()]

    return jsonify({"status": "success", "results": search_results}), 200

# File upload route
@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method=='POST':
        if 'username' not in session:
            return jsonify({"status": "error", "message": "Login required!"})

        file = request.files['file']
        filename = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        username = session['username']
        overwrite = request.form.get('overwrite', 'false') == 'true'

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT filename FROM documents WHERE filename = ? AND username = ?", (filename, username))
        existing_file = cursor.fetchone()

        if existing_file and not overwrite:
            return jsonify({"status": "exists", "message": "File already exists. Overwrite?"})

        file.save(file_path)
        upload_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if existing_file:
            cursor.execute("UPDATE documents SET upload_date = ? WHERE filename = ? AND username = ?", 
                        (upload_date, filename, username))
        else:
            cursor.execute("INSERT INTO documents (filename, upload_date, username) VALUES (?, ?, ?)", 
                        (filename, upload_date, username))

        conn.commit()
        conn.close()

        
        index_document(filename,file_path)

        return jsonify({"status": "success", "message": "File uploaded successfully!"})
    return render_template('uploadDocument.html',username=session.get('username'))

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
