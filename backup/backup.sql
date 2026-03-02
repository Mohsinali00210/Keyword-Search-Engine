BEGIN TRANSACTION;
CREATE TABLE DownloadHistory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER,
    user_name TEXT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE SearchHistory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT,
    user_name TEXT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "SearchHistory" VALUES(1,'Businesses','admin','2025-04-15 16:34:09');
INSERT INTO "SearchHistory" VALUES(2,'Businesses','admin','2025-04-15 16:34:10');
INSERT INTO "SearchHistory" VALUES(3,'bussiness','admin','2025-04-18 12:23:12');
INSERT INTO "SearchHistory" VALUES(4,'bussiness','admin','2025-04-18 12:23:13');
INSERT INTO "SearchHistory" VALUES(5,'bussiness',NULL,'2025-04-25 19:50:19');
INSERT INTO "SearchHistory" VALUES(6,'bussiness',NULL,'2025-04-25 19:50:19');
INSERT INTO "SearchHistory" VALUES(7,'buss',NULL,'2025-04-25 19:50:28');
INSERT INTO "SearchHistory" VALUES(8,'buss',NULL,'2025-04-25 19:50:28');
INSERT INTO "SearchHistory" VALUES(9,'b',NULL,'2025-04-25 19:50:31');
INSERT INTO "SearchHistory" VALUES(10,'b',NULL,'2025-04-25 19:50:31');
INSERT INTO "SearchHistory" VALUES(11,'b',NULL,'2025-04-25 19:50:33');
INSERT INTO "SearchHistory" VALUES(12,'b',NULL,'2025-04-25 19:50:33');
INSERT INTO "SearchHistory" VALUES(13,'b',NULL,'2025-04-25 19:50:33');
INSERT INTO "SearchHistory" VALUES(14,'b',NULL,'2025-04-25 19:50:33');
INSERT INTO "SearchHistory" VALUES(15,'b',NULL,'2025-04-25 19:50:33');
INSERT INTO "SearchHistory" VALUES(16,'b',NULL,'2025-04-25 19:50:33');
INSERT INTO "SearchHistory" VALUES(17,'b',NULL,'2025-04-25 19:50:33');
INSERT INTO "SearchHistory" VALUES(18,'b',NULL,'2025-04-25 19:50:33');
INSERT INTO "SearchHistory" VALUES(19,'a',NULL,'2025-04-25 19:50:40');
INSERT INTO "SearchHistory" VALUES(20,'a',NULL,'2025-04-25 19:50:40');
INSERT INTO "SearchHistory" VALUES(21,'a',NULL,'2025-04-25 19:50:42');
INSERT INTO "SearchHistory" VALUES(22,'a',NULL,'2025-04-25 19:50:42');
INSERT INTO "SearchHistory" VALUES(23,'a',NULL,'2025-04-25 19:50:48');
INSERT INTO "SearchHistory" VALUES(24,'a',NULL,'2025-04-25 19:50:48');
INSERT INTO "SearchHistory" VALUES(25,'a',NULL,'2025-04-25 19:50:57');
INSERT INTO "SearchHistory" VALUES(26,'a',NULL,'2025-04-25 19:50:57');
INSERT INTO "SearchHistory" VALUES(27,'a',NULL,'2025-04-25 19:50:58');
INSERT INTO "SearchHistory" VALUES(28,'a',NULL,'2025-04-25 19:50:58');
INSERT INTO "SearchHistory" VALUES(29,'a',NULL,'2025-04-25 19:50:58');
INSERT INTO "SearchHistory" VALUES(30,'a',NULL,'2025-04-25 19:50:58');
INSERT INTO "SearchHistory" VALUES(31,'a',NULL,'2025-04-25 19:50:58');
INSERT INTO "SearchHistory" VALUES(32,'a',NULL,'2025-04-25 19:50:58');
INSERT INTO "SearchHistory" VALUES(33,'a',NULL,'2025-04-25 19:51:40');
INSERT INTO "SearchHistory" VALUES(34,'a',NULL,'2025-04-25 19:51:40');
INSERT INTO "SearchHistory" VALUES(35,'a',NULL,'2025-04-25 19:51:40');
INSERT INTO "SearchHistory" VALUES(36,'a',NULL,'2025-04-25 19:51:40');
INSERT INTO "SearchHistory" VALUES(37,'a',NULL,'2025-04-25 19:51:40');
INSERT INTO "SearchHistory" VALUES(38,'a',NULL,'2025-04-25 19:51:40');
INSERT INTO "SearchHistory" VALUES(39,'a',NULL,'2025-04-25 19:51:41');
INSERT INTO "SearchHistory" VALUES(40,'a',NULL,'2025-04-25 19:51:41');
INSERT INTO "SearchHistory" VALUES(41,'bus','mohsinali112','2025-04-26 15:02:27');
INSERT INTO "SearchHistory" VALUES(42,'bus','mohsinali112','2025-04-26 15:02:27');
INSERT INTO "SearchHistory" VALUES(43,'business','mohsinali112','2025-04-26 15:02:37');
INSERT INTO "SearchHistory" VALUES(44,'business','mohsinali112','2025-04-26 15:02:37');
INSERT INTO "SearchHistory" VALUES(45,'business','mohsinali112','2025-04-26 15:02:40');
INSERT INTO "SearchHistory" VALUES(46,'business','mohsinali112','2025-04-26 15:02:40');
INSERT INTO "SearchHistory" VALUES(47,'Businesses','mohsinali112','2025-04-26 15:03:18');
INSERT INTO "SearchHistory" VALUES(48,'Businesses','mohsinali112','2025-04-26 15:03:18');
INSERT INTO "SearchHistory" VALUES(49,'bussinesses','mohsinali112','2025-04-26 15:36:47');
INSERT INTO "SearchHistory" VALUES(50,'bussinesses','mohsinali112','2025-04-26 15:36:47');
INSERT INTO "SearchHistory" VALUES(51,'businesses','mohsinali112','2025-04-26 15:36:51');
INSERT INTO "SearchHistory" VALUES(52,'businesses','mohsinali112','2025-04-26 15:36:51');
INSERT INTO "SearchHistory" VALUES(53,'businnesses','mohsinali112','2025-04-26 15:39:41');
INSERT INTO "SearchHistory" VALUES(54,'businnesses','mohsinali112','2025-04-26 15:39:41');
INSERT INTO "SearchHistory" VALUES(55,'businesses','mohsinali112','2025-04-26 15:39:45');
INSERT INTO "SearchHistory" VALUES(56,'businesses','mohsinali112','2025-04-26 15:39:45');
INSERT INTO "SearchHistory" VALUES(57,'businesses','mohsinali112','2025-04-26 17:04:24');
INSERT INTO "SearchHistory" VALUES(58,'businesses','mohsinali112','2025-04-26 17:04:25');
INSERT INTO "SearchHistory" VALUES(59,'businesses','mohsinali112','2025-04-26 17:04:27');
INSERT INTO "SearchHistory" VALUES(60,'businesses','mohsinali112','2025-04-26 17:04:27');
INSERT INTO "SearchHistory" VALUES(61,'businesses','mohsinali112','2025-04-26 17:05:36');
INSERT INTO "SearchHistory" VALUES(62,'businesses','mohsinali112','2025-04-26 17:05:36');
INSERT INTO "SearchHistory" VALUES(63,'businesses','mohsinali112','2025-04-27 11:35:33');
INSERT INTO "SearchHistory" VALUES(64,'businesses','mohsinali112','2025-04-27 11:35:33');
INSERT INTO "SearchHistory" VALUES(65,'businesses','mohsinali112','2025-04-27 11:36:29');
INSERT INTO "SearchHistory" VALUES(66,'businesses','mohsinali112','2025-04-27 11:36:29');
INSERT INTO "SearchHistory" VALUES(67,'businesses','mohsinali112','2025-04-27 11:37:18');
INSERT INTO "SearchHistory" VALUES(68,'businesses','mohsinali112','2025-04-27 11:37:18');
INSERT INTO "SearchHistory" VALUES(69,'businesses','mohsinali112','2025-04-27 11:38:08');
INSERT INTO "SearchHistory" VALUES(70,'businesses','mohsinali112','2025-04-27 11:38:08');
INSERT INTO "SearchHistory" VALUES(71,'eldon','mohsinali112','2025-04-27 11:55:32');
INSERT INTO "SearchHistory" VALUES(72,'eldon','mohsinali112','2025-04-27 11:55:32');
INSERT INTO "SearchHistory" VALUES(73,'Eldon','mohsinali112','2025-04-27 11:56:00');
INSERT INTO "SearchHistory" VALUES(74,'Eldon','mohsinali112','2025-04-27 11:56:00');
INSERT INTO "SearchHistory" VALUES(75,'Eldon','mohsinali112','2025-04-27 11:56:20');
INSERT INTO "SearchHistory" VALUES(76,'Eldon','mohsinali112','2025-04-27 11:56:20');
INSERT INTO "SearchHistory" VALUES(77,'Eldon','mohsinali112','2025-04-27 11:56:29');
INSERT INTO "SearchHistory" VALUES(78,'Eldon','mohsinali112','2025-04-27 11:56:29');
INSERT INTO "SearchHistory" VALUES(79,'eldon','mohsinali112','2025-04-27 11:57:23');
INSERT INTO "SearchHistory" VALUES(80,'eldon','mohsinali112','2025-04-27 11:57:23');
INSERT INTO "SearchHistory" VALUES(81,'Barry French','mohsinali112','2025-04-27 11:58:11');
INSERT INTO "SearchHistory" VALUES(82,'Barry French','mohsinali112','2025-04-27 11:58:11');
INSERT INTO "SearchHistory" VALUES(83,'Barry French','mohsinali112','2025-04-27 11:58:13');
INSERT INTO "SearchHistory" VALUES(84,'Barry French','mohsinali112','2025-04-27 11:58:13');
INSERT INTO "SearchHistory" VALUES(85,'Barry French','mohsinali112','2025-04-27 11:58:13');
INSERT INTO "SearchHistory" VALUES(86,'Barry French','mohsinali112','2025-04-27 11:58:13');
INSERT INTO "SearchHistory" VALUES(87,'Barry French','mohsinali112','2025-04-27 11:58:14');
INSERT INTO "SearchHistory" VALUES(88,'Barry French','mohsinali112','2025-04-27 11:58:14');
INSERT INTO "SearchHistory" VALUES(89,'Barry French','mohsinali112','2025-04-27 11:58:14');
INSERT INTO "SearchHistory" VALUES(90,'Barry French','mohsinali112','2025-04-27 11:58:14');
INSERT INTO "SearchHistory" VALUES(91,'Barry French','mohsinali112','2025-04-27 11:58:14');
INSERT INTO "SearchHistory" VALUES(92,'Barry French','mohsinali112','2025-04-27 11:58:15');
INSERT INTO "SearchHistory" VALUES(93,'Barry French','mohsinali112','2025-04-27 11:58:16');
INSERT INTO "SearchHistory" VALUES(94,'Barry French','mohsinali112','2025-04-27 11:58:16');
INSERT INTO "SearchHistory" VALUES(95,'Barry French','mohsinali112','2025-04-27 11:58:19');
INSERT INTO "SearchHistory" VALUES(96,'Barry French','mohsinali112','2025-04-27 11:58:19');
INSERT INTO "SearchHistory" VALUES(97,'Barry French','mohsinali112','2025-04-27 11:58:20');
INSERT INTO "SearchHistory" VALUES(98,'Barry French','mohsinali112','2025-04-27 11:58:20');
INSERT INTO "SearchHistory" VALUES(99,'Barry French','mohsinali112','2025-04-27 11:58:20');
INSERT INTO "SearchHistory" VALUES(100,'Barry French','mohsinali112','2025-04-27 11:58:20');
INSERT INTO "SearchHistory" VALUES(101,'Barry French','mohsinali112','2025-04-27 11:58:21');
INSERT INTO "SearchHistory" VALUES(102,'Barry French','mohsinali112','2025-04-27 11:58:21');
INSERT INTO "SearchHistory" VALUES(103,'Barry French','mohsinali112','2025-04-27 11:58:21');
INSERT INTO "SearchHistory" VALUES(104,'Barry French','mohsinali112','2025-04-27 11:58:21');
INSERT INTO "SearchHistory" VALUES(105,'Barry French','mohsinali112','2025-04-27 11:58:21');
INSERT INTO "SearchHistory" VALUES(106,'Barry French','mohsinali112','2025-04-27 11:58:21');
INSERT INTO "SearchHistory" VALUES(107,'Barry French','mohsinali112','2025-04-27 11:58:22');
INSERT INTO "SearchHistory" VALUES(108,'Barry French','mohsinali112','2025-04-27 11:58:22');
INSERT INTO "SearchHistory" VALUES(109,'3','mohsinali112','2025-04-27 11:58:26');
INSERT INTO "SearchHistory" VALUES(110,'3','mohsinali112','2025-04-27 11:58:26');
INSERT INTO "SearchHistory" VALUES(111,'3','mohsinali112','2025-04-27 11:58:28');
INSERT INTO "SearchHistory" VALUES(112,'3','mohsinali112','2025-04-27 11:58:28');
INSERT INTO "SearchHistory" VALUES(113,'3','mohsinali112','2025-04-27 11:58:28');
INSERT INTO "SearchHistory" VALUES(114,'3','mohsinali112','2025-04-27 11:58:28');
INSERT INTO "SearchHistory" VALUES(115,'3','mohsinali112','2025-04-27 11:58:28');
INSERT INTO "SearchHistory" VALUES(116,'3','mohsinali112','2025-04-27 11:58:28');
INSERT INTO "SearchHistory" VALUES(117,'3','mohsinali112','2025-04-27 11:58:28');
INSERT INTO "SearchHistory" VALUES(118,'3','mohsinali112','2025-04-27 11:58:28');
INSERT INTO "SearchHistory" VALUES(119,'barry','mohsinali112','2025-04-27 12:19:32');
INSERT INTO "SearchHistory" VALUES(120,'barry','mohsinali112','2025-04-27 12:19:32');
INSERT INTO "SearchHistory" VALUES(121,'abcdx','mohsinali112','2025-04-27 12:20:55');
INSERT INTO "SearchHistory" VALUES(122,'abcdx','mohsinali112','2025-04-27 12:20:55');
INSERT INTO "SearchHistory" VALUES(123,'barry','mohsinali112','2025-04-27 14:52:40');
INSERT INTO "SearchHistory" VALUES(124,'barry','mohsinali112','2025-04-27 14:52:40');
CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            upload_date TEXT NOT NULL,
            username TEXT NOT NULL
        );
INSERT INTO "documents" VALUES(1,'words.txt','2025-03-22 21:38:32','man');
INSERT INTO "documents" VALUES(2,'hehehe.txt','2025-03-23 22:34:38','man');
INSERT INTO "documents" VALUES(3,'Novals list.txt','2025-03-22 21:16:23','man');
INSERT INTO "documents" VALUES(4,'words.txt','2025-03-23 23:27:23','sahi');
INSERT INTO "documents" VALUES(6,'hehehe.txt','2025-03-24 00:55:22','sahi');
INSERT INTO "documents" VALUES(7,'records.txt','2025-03-24 22:03:23','man');
INSERT INTO "documents" VALUES(8,'records.txt','2025-03-25 15:49:40','kumi');
INSERT INTO "documents" VALUES(10,'s.txt','2025-04-15 21:31:45','admin');
INSERT INTO "documents" VALUES(11,'s.txt','2025-04-26 20:02:53','mohsinali112');
INSERT INTO "documents" VALUES(12,'abcd.txt','2025-04-26 21:45:49','mohsinali112');
INSERT INTO "documents" VALUES(13,'SampleCSVFile_2kb.csv','2025-04-27 17:18:44','mohsinali112');
INSERT INTO "documents" VALUES(14,'SampleCSVFile_2k.csv','2025-04-27 17:19:14','mohsinali112');
INSERT INTO "documents" VALUES(15,'abcdx.txt','2025-04-27 17:20:46','mohsinali112');
INSERT INTO "documents" VALUES(16,'abcdxc.txt','2025-04-27 17:22:40','mohsinali112');
INSERT INTO "documents" VALUES(17,'abcdxcw.txt','2025-04-27 17:24:14','mohsinali112');
INSERT INTO "documents" VALUES(18,'SampleCSVFile_2k2.csv','2025-04-27 17:26:21','mohsinali112');
INSERT INTO "documents" VALUES(19,'SampleCSVFile_2k22.csv','2025-04-27 17:26:38','mohsinali112');
INSERT INTO "documents" VALUES(20,'SampleCSVFile_2k223.csv','2025-04-27 17:27:40','mohsinali112');
INSERT INTO "documents" VALUES(21,'SampleCSVFile_2k2233.csv','2025-04-27 19:49:36','mohsinali112');
INSERT INTO "documents" VALUES(22,'SampleCSVFile_2k22332.csv','2025-04-27 19:51:22','mohsinali112');
INSERT INTO "documents" VALUES(23,'SampleCSVFile_2k223323.csv','2025-04-27 19:52:25','mohsinali112');
CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
INSERT INTO "users" VALUES(1,'admin','admin@gmail.com','123');
INSERT INTO "users" VALUES(2,'man1','man123@gmail.com','12345');
INSERT INTO "users" VALUES(3,'jar','jar123@gmail.com','12345');
INSERT INTO "users" VALUES(4,'shabbir','shabbir@gmail.com','12345');
INSERT INTO "users" VALUES(5,'sadaf','sadaf123@gmail.com','12345');
INSERT INTO "users" VALUES(6,'miss','miss123@gmail.com','12345');
INSERT INTO "users" VALUES(7,'bus','bus123@gmail.com','12345');
INSERT INTO "users" VALUES(8,'hmm','hmm123@gmail.com','12345');
INSERT INTO "users" VALUES(9,'okk','okk@gmail.com','12345');
INSERT INTO "users" VALUES(11,'gud','gud@gmail.com','12345');
INSERT INTO "users" VALUES(12,'kumi','kumi123@gmail.com','12345');
INSERT INTO "users" VALUES(13,'mohsinali','hasnainalithaheem0021@gmail.com','Today');
INSERT INTO "users" VALUES(14,'mohsinali11','mohsinali00210@gmail.com','123');
INSERT INTO "users" VALUES(15,'mohsinali112','mohsinali002100@gmail.com','1234');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('users',15);
INSERT INTO "sqlite_sequence" VALUES('documents',23);
INSERT INTO "sqlite_sequence" VALUES('SearchHistory',124);
COMMIT;
