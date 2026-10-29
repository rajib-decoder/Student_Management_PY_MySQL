Student Management System using Python and MySQL

A simple Student Management System built using Python and MySQL to manage student records through a menu-driven console application. The project allows users to add, view, search, update, and delete student details stored in a MySQL database.

Features
Add Student: Insert new student records with ID, first name, last name, and branch.
View All Students: Display all student records from the database.
Search Student by ID: Find a specific student using their unique ID.
Update Student Details: Modify existing student information.
Delete Student: Remove a student record using their ID.
Exit: Close the application.
Technologies Used
Python
MySQL
MySQL Connector/Python
Database Structure

The project uses a MySQL database named Student_Management with a Students table containing the following fields:

ID – Student ID
Fname – Student's first name
Lname – Student's last name
Branch – Student's branch
How to Run
Install Python and MySQL on your system.
Install the required Python package:
bash
pip install mysql-connector-python

Create a MySQL database named Student_Management.
Create the Students table with the required columns.
Update the database connection credentials in the Python file if necessary.
Run the program:
bash
python main.py

Project Purpose

This project demonstrates the practical use of Python database connectivity, SQL queries, CRUD operations (Create, Read, Update, Delete), and menu-driven programming.

Future Improvements: Add input validation, exception handling, and a graphical user interface for a better user experience.
