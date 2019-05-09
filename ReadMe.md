
# Udacity Logs Analysis project:-
### By Ahmed Alhawsawi
## ReadMe.md 

### Introduction
This project is for those who enrolled in Full-Stack Web Developer Nanodegree program which is provided by Udacity platform. The aim of this project is to improve the skills of the trainees in SQL database server by working with data that have millions of rows. To achieve the project’s goals, there are some requirements to be met and procedures to be followed. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:
-  What are the most popular three articles of all time?
-  Who are the most popular article authors of all time?
-  On which days did more than 1% of requests lead to errors?

### Requirements:  

- [Python](https://www.python.org/) 2.7, 3.5 or latest version of Python programming language.
- [VartualBox](https://www.virtualbox.org/wiki/Downloads) the software that runs the Virtual Machine (VM) environment locally in the Operating System (OS).
- [Vagrant](https://www.vagrantup.com/) the software that lunches and configures the virtual machine in your computer.
- [Git](https://git-scm.com/) a free and open source Unix-style terminal. 

### How to git to the project: 
[VartualBox](https://www.virtualbox.org/wiki/Downloads) software will be installed to the OS firstly. Next, the installation of [vagrant](https://www.vagrantup.com/) will take place. After the installation of these two software the work will be on command line to run the virtual machine and configure its all settings.  
A **_vagrantfile_** is a file that can be used to initiate the system by using vagrant program. This file contains all other neccessary files and tools for this project. This is provided by Udacity platform.

Running a _vagrantfile_ with **vagrant up** command will install Ubuntu Linux OS and setup all the other settings that required for this project.
If the setup is done successfully, then the use of **_Vagrant ssh_** command will take place to log in to the system. 
In case of any failure of logging to the system after executing this command, **winpty vagrant ssh** command can be used instead to log in to the system. If this command doesn’t work either, running **vagarnt up**command again can solve this problem. In case of the operation unsolved the problem, the installation of different version of vagrant can be one solution of it.

If the system is working properly, PostgreSQL database server will start inside the VM. Then _psql_ command will be used to access and run SQL statements.

### Runing the virtual machine
These steps will be taken after successful setup:
- **cd  /vagrant** to change the dircotory to access the main files.
- **Vagrant ssh**
- In case if **vagrant ssh** is not working – **winpty vagrant ssh**
-	**psql – d news – f newsdata.sql**: connecting with news data base and loading [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file to the VM.
-	**Psql – d news –f create_views.sql**: to load create views to news data base.
-	**\lc or psql –d news** to connect db.
-	**\d** list all tables with views.
-	**\d table_name** to llist columns and rows in assigned table
-	**\q** to exit news db.
-	**python logs_analysis.py** to run the project file and print the results.


