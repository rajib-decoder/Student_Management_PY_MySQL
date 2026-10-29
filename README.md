🎓 Student Management System
💻 A Python + MySQL Project for Managing Student Records

A simple, interactive, and menu-driven Student Management System built using Python and MySQL. This project helps manage student information efficiently by allowing users to add, view, search, update, and delete student records through a console-based interface.
```
✨ Features
➕ Add Student — Add new student records to the database.
📋 View All Students — Display all registered student records.
🔍 Search Student — Find student details using their unique ID.
✏️ Update Student — Modify existing student information.
🗑️ Delete Student — Remove student records from the database.
🚪 Exit Application — Safely exit the program.
🛠️ Technologies Used
Technology	Purpose
🐍 Python	Application logic and menu-driven interface
🐬 MySQL	Database for storing student records
🔌 MySQL Connector/Python	Connects Python with MySQL
🗄️ Database Structure
```
Database Name: Student_Management

Table Name: Students
```
Column	Data Type	Description
ID	INT	Unique student ID
Fname	VARCHAR(255)	Student's first name
Lname	VARCHAR(255)	Student's last name
Branch	VARCHAR(255)	Student's academic branch
⚙️ Installation & Setup
```
Follow these steps to run the project on your local machine.
```
1️⃣ Clone the Repository
bash
git clone https://github.com/YOUR-USERNAME/student-management-system.git

2️⃣ Navigate to the Project Folder
bash
cd student-management-system

3️⃣ Install the Required Package
bash
pip install mysql-connector-python

4️⃣ Create the MySQL Database
```
Open MySQL and execute:
```
sql
CREATE DATABASE Student_Management;

USE Student_Management;

CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Fname VARCHAR(255),
    Lname VARCHAR(255),
    Branch VARCHAR(255)
);
```
5️⃣ Configure the Database Connection

Update the connection settings in your Python file according to your MySQL configuration.
```
python
mydb = ms.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="Student_Management"
)
```
6️⃣ Run the Application
```
bash
python main.py
```
🖥️ Application Menu
```
text
===============================
*** Student Management ***
===============================

1. Add a Student
2. View All Students
3. Search Students By ID
4. Update Students Details
5. Delete a Students
6. Exit

Enter Your Choice:
```

Choose an option from the menu to perform the desired operation.
```
📚 Concepts Demonstrated
Python functions and control flow
match-case statements
MySQL database connectivity
SQL queries and parameterized statements
CRUD operations
Database transactions using commit()
Fetching and displaying database records
🚀 Future Enhancements
✅ Input validation and exception handling
🔐 Secure database credential management
🖼️ Graphical User Interface (GUI)
📊 Student report generation
🔎 Search students by name or branch
📅 Additional student information and reporting
🎯 Project Objective
```
The main objective of this project is to understand how Python interacts with a MySQL database and how CRUD operations can be implemented in a real-world application.

This project is suitable for Python beginners, database programming practice, and academic mini-projects.
```
GitHub: https://github.com/rajib-decoder
⭐ Support
```
If you find this project useful, consider giving the repository a ⭐ Star on GitHub!

Built with ❤️ using Python and MySQL.
