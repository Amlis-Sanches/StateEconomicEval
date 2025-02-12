---
title: "Python SQLite - GeeksforGeeks"
source: "https://www.geeksforgeeks.org/python-sqlite/#"
author:
  - "[[GeeksforGeeks]]"
published: 2021-09-22
created: 2025-02-11
description: "A Computer Science portal for geeks. It contains well written, well thought and well explained computer science and programming articles, quizzes and practice/competitive programming/company interview Questions."
tags:
  - "clippings"
---
Last Updated : 09 Aug, 2024

[![News](https://media.geeksforgeeks.org/auth-dashboard-uploads/Google-news.svg)](https://news.google.com/publications/CAAqBwgKMLTrzwsw44bnAw?hl=en-IN&gl=IN&ceid=IN%3Aen)

****Python SQLite3**** module is used to integrate the SQLite database with Python. It is a standardized Python DBI API 2.0 and provides a straightforward and simple-to-use interface for interacting with SQLite databases. There is no need to install this module separately as it comes along with Python after the 2.5x version.

![Python SQLite tutorial](https://media.geeksforgeeks.org/wp-content/uploads/20210901170408/PythonSQLitetutorial.jpg)

This Python SQLite tutorial will help to learn how to use SQLite3 with Python from basics to advance with the help of good and well-explained examples and also contains Exercises for honing your skills.

## Introduction

- [Introduction to SQLite in Python](https://www.geeksforgeeks.org/introduction-to-sqlite-in-python/)
- [Python SQLite – Connecting to Database](https://www.geeksforgeeks.org/python-sqlite-connecting-to-database/)
- [SQLite Datatypes and its Corresponding Python Types](https://www.geeksforgeeks.org/sqlite-datatypes-and-its-corresponding-python-types/)

## SQLite Queries

- [Python SQLite – Cursor Object](https://www.geeksforgeeks.org/python-sqlite-cursor-object/)
- [Python SQLite – Create Table](https://www.geeksforgeeks.org/python-sqlite-create-table/)
- [Python SQLite – Insert Data](https://www.geeksforgeeks.org/python-sqlite-insert-data/)
- [Python SQLite – Select Data from Table](https://www.geeksforgeeks.org/python-sqlite-select-data-from-table/)
- [Python SQLite – WHERE Clause](https://www.geeksforgeeks.org/python-sqlite-where-clause/)
- [Python SQLite – ORDER BY Clause](https://www.geeksforgeeks.org/python-sqlite-order-by-clause/)
- [Python SQLite – LIMIT Clause](https://www.geeksforgeeks.org/python-sqlite-limit-clause/)
- [Python SQLite – JOIN Clause](https://www.geeksforgeeks.org/python-sqlite-join-clause/)
- [Python SQLite – Deleting Data in Table](https://www.geeksforgeeks.org/python-sqlite-deleting-data-in-table/)
- [Python SQLite – DROP Table](https://www.geeksforgeeks.org/python-sqlite-drop-table/)
- [Python SQLite – Update Data](https://www.geeksforgeeks.org/python-sqlite-update-data/)
- [Python SQLite – Update Specific Column](https://www.geeksforgeeks.org/python-sqlite-update-specific-column/)

## Working with Tables

- [Check if Table Exists in SQLite using Python](https://www.geeksforgeeks.org/check-if-table-exists-in-sqlite-using-python/)
- [How to list tables using SQLite3 in Python ?](https://www.geeksforgeeks.org/how-to-list-tables-using-sqlite3-in-python/)
- [How to Alter a SQLite Table using Python ?](https://www.geeksforgeeks.org/how-to-alter-a-sqlite-table-using-python/)
- [How to Delete a Specific Row from SQLite Table using Python ?](https://www.geeksforgeeks.org/how-to-delete-a-specific-row-from-sqlite-table-using-python/)
- [How to Update all the Values of a Specific Column of SQLite Table using Python ?](https://www.geeksforgeeks.org/how-to-update-all-the-values-of-a-specific-column-of-sqlite-table-using-python/)

## Working with Images

- [How to Insert Image in SQLite using Python?](https://www.geeksforgeeks.org/how-to-insert-image-in-sqlite-using-python/)
- [How to Read Image in SQLite using Python?](https://www.geeksforgeeks.org/how-to-read-image-in-sqlite-using-python/)
- [Storing OpenCV Image in SQLite3 with Python](https://www.geeksforgeeks.org/storing-opencv-image-in-sqlite3-with-python/)

## Exercises

- [Count total number of changes made after connecting SQLite to Python](https://www.geeksforgeeks.org/count-total-number-of-changes-made-after-connecting-sqlite-to-python/)
- [How to Show all Columns in the SQLite Database using Python ?](https://www.geeksforgeeks.org/how-to-show-all-columns-in-the-sqlite-database-using-python/)
- [How to Count the Number of Rows of a Given SQLite Table using Python?](https://www.geeksforgeeks.org/how-to-count-the-number-of-rows-of-a-given-sqlite-table-using-python/)
- [How to import CSV file in SQLite database using Python ?](https://www.geeksforgeeks.org/how-to-import-csv-file-in-sqlite-database-using-python/)
- [How to Execute a Script in SQLite using Python?](https://www.geeksforgeeks.org/how-to-execute-a-script-in-sqlite-using-python/)
- [How to store Python functions in a Sqlite table?](https://www.geeksforgeeks.org/how-to-store-python-functions-in-a-sqlite-table/)
- [How to Create a Backup of a SQLite Database using Python?](https://www.geeksforgeeks.org/how-to-create-a-backup-of-a-sqlite-database-using-python/)
- [How to connect to SQLite database that resides in the memory using Python ?](https://www.geeksforgeeks.org/how-to-connect-to-sqlite-database-that-resides-in-the-memory-using-python/)
- [Change SQLite Connection Timeout using Python](https://www.geeksforgeeks.org/change-sqlite-connection-timeout-using-python/)

## Python SQLite – FAQs

### Can You Use SQLite with Python?

> Yes, you can use SQLite with Python. Python comes with built-in support for SQLite through the `sqlite3` module, which allows you to interact with an SQLite database directly from Python code. This makes it an excellent choice for applications that require a lightweight database without the overhead of a full database management system.

### How to Use pysqlite?

> `pysqlite` is an external library in Python that provides SQLite database access. It was the original interface to the SQLite relational database management system before it became integrated into Python’s standard library as `sqlite3`. Since Python 2.5 and above, `sqlite3` is included in Python’s standard library, which essentially provides the same functionalities as `pysqlite`. If you are using Python 2.5 or later, it is recommended to use `sqlite3` instead. Here’s a basic example of using `sqlite3`:
> 
> ```
> import sqlite3
> 
> # Connect to an SQLite database (or create it if it doesn't exist)
> conn = sqlite3.connect('example.db')
> 
> # Create a cursor object using the cursor() method
> cursor = conn.cursor()
> 
> # Create table
> cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
>              (date text, trans text, symbol text, qty real, price real)''')
> 
> # Insert a row of data
> cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
> 
> # Save (commit) the changes
> conn.commit()
> 
> # Close the connection
> conn.close()
> ```

### What is the Purpose of the Python SQLite Connector?

> The purpose of the Python SQLite connector, implemented as the `sqlite3` module, is to provide a lightweight disk-based database that doesn’t require a separate server process. It allows Python applications to access SQLite databases in a straightforward way. It’s used to execute SQL commands and queries, handle databases, and perform other database management tasks.

### What is the Difference Between SQLite and MySQL?

> - ****SQLite****:
> - SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
> - It is embedded into the end program. SQLite reads and writes directly to ordinary disk files. A complete SQL database with multiple tables, indices, triggers, and views, is contained in a single disk file.
> - It is used predominantly for applications that need a lightweight database without the need for a network-accessible database management system.
> 
> - ****MySQL****:
> - MySQL is a full-featured relational database management system (RDBMS) that supports a wide array of features and extensive customization.
> - It operates as a server providing multi-user access to a number of databases.
> - Suitable for large scale applications and websites that need to handle large volumes of data and high user loads.

### Is sqlite3 Part of Python?

> Yes, `sqlite3` is part of Python’s standard library for versions 2.5 and later. It provides an SQL interface compliant with the DB-API 2.0 specification described by PEP 249. This means you don’t need to install anything extra if you’re using these versions of Python; you can start using SQLite databases in your applications right away.

  
  

### Similar Reads

- [

Python SQLite

Python SQLite3 module is used to integrate the SQLite database with Python. It is a standardized Python DBI API 2.0 and provides a straightforward and simple-to-use interface for interacting with SQLite databases. There is no need to install this module separately as it comes along with Python after

4 min read

](https://www.geeksforgeeks.org/python-sqlite/?ref=lbp)

## SQLite in Python - Getting Started

- [

Introduction to SQLite in Python

Databases offer numerous functionalities by which one can manage large amounts of information easily over the web and high-volume data input and output over a typical file such as a text file. SQL is a query language and is very popular in databases. Many websites use MySQL. SQLite is a "light" vers

3 min read

](https://www.geeksforgeeks.org/introduction-to-sqlite-in-python/?ref=lbp)

---
- [

Python SQLite - Connecting to Database

In this article, we'll discuss how to connect to an SQLite Database using the sqlite3 module in Python. Connecting to the Database Connecting to the SQLite Database can be established using the connect() method, passing the name of the database to be accessed as a parameter. If that database does no

2 min read

](https://www.geeksforgeeks.org/python-sqlite-connecting-to-database/?ref=lbp)

---
- [

SQLite Datatypes and its Corresponding Python Types

SQLite is a C-language-based library that provides a portable and serverless SQL database engine. It has a file-based architecture; hence it reads and writes to a disk. Since SQLite is a zero-configuration database, no installation or setup is needed before its usage. Starting from Python 2.5.x, SQL

3 min read

](https://www.geeksforgeeks.org/sqlite-datatypes-and-its-corresponding-python-types/?ref=lbp)

---

## SQLite Queries

- [

Python SQLite - Cursor Object

In this article, we are going to discuss cursor objects in sqlite3 module of Python. Cursor Object It is an object that is used to make the connection for executing SQL queries. It acts as middleware between SQLite database connection and SQL query. It is created after giving connection to SQLite da

2 min read

](https://www.geeksforgeeks.org/python-sqlite-cursor-object/?ref=lbp)

---
- [

Python SQLite - Create Table

In this article, we will discuss how can we create tables in the SQLite database from the Python program using the sqlite3 module. In SQLite database we use the following syntax to create a table: CREATE TABLE database\_name.table\_name( column1 datatype PRIMARY KEY(one or more columns), column2 datat

1 min read

](https://www.geeksforgeeks.org/python-sqlite-create-table/?ref=lbp)

---
- [

Python SQLite - Insert Data

In this article, we will discuss how can we insert data in a table in the SQLite database from Python using the sqlite3 module. The SQL INSERT INTO statement of SQL is used to insert a new row in a table. There are two ways of using the INSERT INTO statement for inserting rows: Only values: The firs

3 min read

](https://www.geeksforgeeks.org/python-sqlite-insert-data/?ref=lbp)

---
- [

Python SQLite - Select Data from Table

In this article, we will discuss, select statement of the Python SQLite module. This statement is used to retrieve data from an SQLite table and this returns the data contained in the table. In SQLite the syntax of Select Statement is: SELECT \* FROM table\_name; \* : means all the column from the tabl

3 min read

](https://www.geeksforgeeks.org/python-sqlite-select-data-from-table/?ref=lbp)

---
- [

Python SQLite - WHERE Clause

Where clause is used in order to make our search results more specific, using the where clause in SQL/SQLite we can go ahead and specify specific conditions that have to be met when retrieving data from the database. If we want to retrieve, update or delete a particular set of data we can use the wh

4 min read

](https://www.geeksforgeeks.org/python-sqlite-where-clause/?ref=lbp)

---
- [

Python SQLite - ORDER BY Clause

In this article, we will discuss ORDER BY clause in SQLite using Python. The ORDER BY statement is a SQL statement that is used to sort the data in either ascending or descending according to one or more columns. By default, ORDER BY sorts the data in ascending order. DESC is used to sort the data i

3 min read

](https://www.geeksforgeeks.org/python-sqlite-order-by-clause/?ref=lbp)

---
- [

Python SQLite - LIMIT Clause

In this article, we are going to discuss the LIMIT clause in SQLite using Python. But first, let's get a brief about the LIMIT clause. If there are many tuples satisfying the query conditions, it might be resourceful to view only a handful of them at a time. LIMIT keyword is used to limit the data g

2 min read

](https://www.geeksforgeeks.org/python-sqlite-limit-clause/?ref=lbp)

---
- [

Python SQLite - JOIN Clause

In this article, we discuss the JOIN clause in SQLite using the sqlite3 module in Python. But at first let's see a brief about join in SQLite. Join Clause A JOIN clause combines the records from two tables on the basis of common attributes. The different types of joins are as follows: INNER JOIN (OR

5 min read

](https://www.geeksforgeeks.org/python-sqlite-join-clause/?ref=lbp)

---
- [

Python SQLite - Deleting Data in Table

In this article, we will discuss how we can delete data in the table in the SQLite database from the Python program using the sqlite3 module. In SQLite database we use the following syntax to delete data from a table: DELETE FROM table\_name \[WHERE Clause\] To create the database, we will execute the

2 min read

](https://www.geeksforgeeks.org/python-sqlite-deleting-data-in-table/?ref=lbp)

---
- [

Python SQLite - Update Data

In this article, we will discuss how we can update data in tables in the SQLite database using Python - sqlite3 module. The UPDATE statement in SQL is used to update the data of an existing table in the database. We can update single columns as well as multiple columns using UPDATE statement as per

7 min read

](https://www.geeksforgeeks.org/python-sqlite-update-data/?ref=lbp)

---
- [

Python SQLite - DROP Table

In this article, we will discuss the DROP command in SQLite using Python. But first, let's get a brief about the drop command. DROP is used to delete the entire database or a table. It deleted both records in the table along with the table structure. Syntax: DROP TABLE TABLE\_NAME; For dropping table

2 min read

](https://www.geeksforgeeks.org/python-sqlite-drop-table/?ref=lbp)

---
- [

Python SQLite - Update Specific Column

In this article, we will discuss how to update a specific column of a table in SQLite using Python. In order to update a particular column in a table in SQL, we use the UPDATE query. The UPDATE statement in SQL is used to update the data of an existing table in the database. We can update single col

3 min read

](https://www.geeksforgeeks.org/python-sqlite-update-specific-column/?ref=lbp)

---

## SQLite Clause

- [

Check if Table Exists in SQLite using Python

In this article, we will discuss how to check if a table exists in an SQLite database using the sqlite3 module of Python. In an SQLite database, the names of all the tables are enlisted in the sqlite\_master table. So in order to check if a table exists or not we need to check that if the name of the

2 min read

](https://www.geeksforgeeks.org/check-if-table-exists-in-sqlite-using-python/?ref=lbp)

---
- [

How to list tables using SQLite3 in Python ?

In this article, we will discuss how to list all the tables in the SQLite database using Python. Here, we will use the already created database table from SQLite. We will also learn exception handling during connecting to our database. Database Used: Steps to Fetch all tables using SQLite3 in Python

2 min read

](https://www.geeksforgeeks.org/how-to-list-tables-using-sqlite3-in-python/?ref=lbp)

---

## SQLite Working with Data

- [

How to Update all the Values of a Specific Column of SQLite Table using Python ?

In this article, we are going to update all the values of a specific column of a given SQLite table using Python. In order to update all the columns of a particular table in SQL, we use the UPDATE query. The UPDATE statement in SQL is used to update the data of an existing table in the database. We

3 min read

](https://www.geeksforgeeks.org/how-to-update-all-the-values-of-a-specific-column-of-sqlite-table-using-python/?ref=lbp)

---
- [

How to Insert Image in SQLite using Python?

In this article, we will discuss how to insert images in SQLite using sqlite3 module in Python. Implementation: 1. Set the connection to the SQLite database using Python code. sqliteConnection = sqlite3.connect('SQLite\_Retrieving\_data.db') cursor = sqliteConnection.cursor() 2. We need to define an I

2 min read

](https://www.geeksforgeeks.org/how-to-insert-image-in-sqlite-using-python/?ref=lbp)

---
- [

How to Read Image in SQLite using Python?

This article shows us how to use the Python sqlite3 module to read or retrieve images that are stored in the form of BLOB data type in an SQLite table. First, We need to read an image that is stored in an SQLite table in BLOB format using python script and then write the file back to any location on

3 min read

](https://www.geeksforgeeks.org/how-to-read-image-in-sqlite-using-python/?ref=lbp)

---

## Working with Images

- [

Count total number of changes made after connecting SQLite to Python

In this article, we are going to see how to count total changes since the SQLite database connection is open using Python. To get the total number of changes we use the connection object's total\_changes property. Class Instance: sqlite3.Connection Syntax: <connection\_object>.total\_changes Retu

3 min read

](https://www.geeksforgeeks.org/count-total-number-of-changes-made-after-connecting-sqlite-to-python/?ref=lbp)

---
- [

How to Show all Columns in the SQLite Database using Python ?

In this article, we will discuss how we can show all columns of a table in the SQLite database from Python using the sqlite3 module. Approach:Connect to a database using the connect() method.Create a cursor object and use that cursor object created to execute queries in order to create a table and i

3 min read

](https://www.geeksforgeeks.org/how-to-show-all-columns-in-the-sqlite-database-using-python/?ref=lbp)

---

## Python SQLite - Exercise

- [

How to Execute a Script in SQLite using Python?

In this article, we are going to see how to execute a script in SQLite using Python. Here we are executing create table and insert records into table scripts through Python. In Python, the sqlite3 module supports SQLite database for storing the data in the database. Approach Step 1: First we need to

2 min read

](https://www.geeksforgeeks.org/how-to-execute-a-script-in-sqlite-using-python/?ref=lbp)

---
- [

How to store Python functions in a Sqlite table?

SQLite is a relational database system contained in a C library that works over syntax very much similar to SQL. It can be fused with Python with the help of the sqlite3 module. The Python Standard Library sqlite3 was developed by Gerhard HÃ¤ring. It delivers an SQL interface compliant with the DB-AP

3 min read

](https://www.geeksforgeeks.org/how-to-store-python-functions-in-a-sqlite-table/?ref=lbp)

---
- [

How to Create a Backup of a SQLite Database using Python?

In this article, we will learn How to Create a Backup of an SQLite Database using Python. To Create a Backup of an SQLite Database using Python, the required modules are SQLite3 and IO. First, let's create the original database to do that follow the below program: C/C++ Code import sqlite3 import io

2 min read

](https://www.geeksforgeeks.org/how-to-create-a-backup-of-a-sqlite-database-using-python/?ref=lbp)

---
- [

How to connect to SQLite database that resides in the memory using Python ?

In this article, we will learn how to Connect an SQLite database connection to a database that resides in the memory using Python. But first let brief about what is sqlite. SQLite is a lightweight database software library that provides a relational database management system. Generally, it is a ser

3 min read

](https://www.geeksforgeeks.org/how-to-connect-to-sqlite-database-that-resides-in-the-memory-using-python/?ref=lbp)

---
- [

Change SQLite Connection Timeout using Python

In this article, we will discuss how to change the SQLite connection timeout when connecting from Python. What is a connection timeout and what causes it? A connection timeout is an error that occurs when it takes too long for a server to respond to a user's request. Connection timeouts usually occu

3 min read

](https://www.geeksforgeeks.org/change-sqlite-connection-timeout-using-python/?ref=lbp)

---
- [

Using SQLite Aggregate functions in Python

In this article, we are going to see how to use the aggregate function in SQLite Python. An aggregate function is a database management function that groups the values of numerous rows into a single summary value. Average (i.e., arithmetic mean), sum, max, min, Count are common aggregation functions

4 min read

](https://www.geeksforgeeks.org/using-sqlite-aggregate-functions-in-python/?ref=lbp)

---
- [

Launch Website URL shortcut using Python

In this article, we are going to launch favorite websites using shortcuts, for this, we will use Python's sqlite3 and webbrowser modules to launch your favorite websites using shortcuts. Both sqlite3 and webbrowser are a part of the python standard library, so we don't need to install anything separ

3 min read

](https://www.geeksforgeeks.org/launch-website-url-shortcut-using-python/?ref=lbp)

---

## Python SQLite Additional

- [

How to Execute many SQLite Statements in Python?

In SQLite using the executescript() method, we can execute multiple SQL statements/queries at once. The basic execute() method allows us to only accept one query at a time, so when you need to execute several queries we need to arrange them like a script and pass that script to the executescript() m

3 min read

](https://www.geeksforgeeks.org/how-to-execute-many-sqlite-statements-in-python/?ref=lbp)

---
- [

Python - Create or Redefine SQLite Functions

The SQLite does not have functions or stored procedure language like MySQL. We cannot create stored functions or procedures in SQLite. That means the CREATE FUNCTION or CREATE PROCEDURE does not work in SQLite. In SQLite instead of CREATE FUNCTION or CREATE PROCEDURE we have SQLiteâ€™s C API which all

3 min read

](https://www.geeksforgeeks.org/python-create-or-redefine-sqlite-functions/?ref=lbp)

---
- [

Store Google Sheets data into SQLite Database using Python

In this article, we are going to store google sheets data into a database using python. The first step is to enable the API and to create the credentials, so let's get stared. Enabling the APIs and creating the credentialsGo to Marketplace in Cloud Console.Click on ENABLE APIS AND SERVICESThen Searc

5 min read

](https://www.geeksforgeeks.org/store-google-sheets-data-into-sqlite-database-using-python/?ref=lbp)

---
- [

How to Execute a SQLite Statement in Python?

In this article, we are going to see how to execute SQLite statements using Python. We are going to execute how to create a table in a database, insert records and display data present in the table. In order to execute an SQLite script in python, we will use the execute() method with connect() objec

2 min read

](https://www.geeksforgeeks.org/how-to-execute-a-sqlite-statement-in-python/?ref=lbp)

---
- [

How to Import a CSV file into a SQLite database Table using Python?

In this article, we are going to discuss how to import a CSV file content into an SQLite database table using Python. Approach:At first, we import csv module (to work with csv file) and sqlite3 module (to populate the database table).Then we connect to our geeks database using the sqlite3.connect()

3 min read

](https://www.geeksforgeeks.org/how-to-import-a-csv-file-into-a-sqlite-database-table-using-python/?ref=lbp)

---
- [

Python SQLite - CRUD Operations

In this article, we will go through the CRUD Operation using the SQLite module in Python. CRUD Operations The abbreviation CRUD expands to Create, Read, Update and Delete. These four are fundamental operations in a database. In the sample database, we will create it, and do some operations. Let's di

4 min read

](https://www.geeksforgeeks.org/python-sqlite-crud-operations/?ref=lbp)

---