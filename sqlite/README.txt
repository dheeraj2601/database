
To create a new SQLite database named "ex1" with a single table named "tbl1"

$ sqlite3 ex1
SQLite version 3.8.5 2014-05-29 12:36:14
Enter ".help" for usage hints.
sqlite> create table tbl1(one varchar(10), two smallint);
sqlite> insert into tbl1 values('hello!',10);
sqlite> insert into tbl1 values('goodbye', 20);
sqlite> select * from tbl1;
hello!|10
goodbye|20
sqlite>

sqlite> .save ex1.db
sqlite>


Commands	Description
--------
.show	       Displays current settings for various parameters
.databases	 Provides database names and files
.quit	       Quit sqlite3 program
.tables	     Show current tables
.schema	     Display schema of table
.header	     Display or hide the output table header
.mode	       Select mode for the output table
.dump	       Dump database in SQL text format


Standard Commands can be classified into three groups:
------------------
Data Definition Language: It provides the storage structure and methods to access data from the database system.

CREATE
ALTER
DROP

Data Manipulation Language: It enables users to manipulate (add/modify/delete) data.

INSERT
UPDATE
DELETE

Data Query Language: It enables users to retrieve required data from the database.

SELECT


CREATE TABLE comments ( 
	post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
	name TEXT NOT NULL, 
	email TEXT NOT NULL, 
	website_url TEXT NULL, 
	comment TEXT NOT NULL );
  
 .tables
 .schema comments
 
INSERT INTO comments ( name, email, website_url, comment )
VALUES ( 'Shivam Mamgain', 'xyz@gmail.com',
'shivammg.blogspot.com', 'Great tutorial for beginners.' );
 
SELECT post_id, name, email, website_url, comment
FROM comments;

SELECT * FROM comments;
  
.show

.headers ON
.mode column


UPDATE comments
SET email = 'zyx@email.com'
WHERE name = 'Shivam Mamgain';

DELETE FROM comments WHERE post_id = 9;

New columns can be added to a table using ALTER
ALTER TABLE comments ADD COLUMN username TEXT;

DROP TABLE comments;


Writing results to a file
sqlite> .output test_file_1.txt



Installation :
sudo apt-get install sqlite3 libsqlite3-dev


Reference : 
https://www.sitepoint.com/getting-started-sqlite3-basic-commands/
https://www.sqlite.org/cli.html


----------------------------


sudo apt-get install sqlite3 libsqlite3-dev

.headers ON
.quit


https://pymotw.com/2/sqlite3/
https://www.sitepoint.com/getting-started-sqlite3-basic-commands/



python test2_sqlite3.py
sqlite3 todo.db

----------------------------

