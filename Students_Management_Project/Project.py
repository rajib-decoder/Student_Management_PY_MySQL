
import mysql.connector as ms

mydb = ms.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Student_Management"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE Student_Management")
# print("Database Created")

# mycursor.execute("CREATE TABLE Students ( ID INT, Fname VARCHAR(255), Lname VARCHAR(255), Branch VARCHAR(255))")

# print("Table Created")

print("===============================")
print("*** Student Management ***")
print("===============================")

# mycursor.execute("ALTER TABLE Students MODIFY ID INT PRIMARY KEY")
# print("Table Modified")

while (True):
    print("\n1. Add a Student")
    print("2. View All Students")
    print("3. Search Students By ID")
    print("4. Update Students Details")
    print("5. Delete a Students")
    print("6. Exit")
    choice = int(input("Enter Your Choice:"))

    match choice :
        case 1:
            ID = int(input("Enter Student ID:"))
            Fname = input("Enter the Fname of Student:")
            Lname = input("Enter the Lname of Student:")
            Branch = input("Enter the Branch of Student:")

            sql = "INSERT INTO Students VALUES(%s, %s, %s, %s)"
            value =(ID, Fname, Lname, Branch) 

            mycursor.execute(sql, value)
            mydb.commit()
            print(mycursor.rowcount,"Student Added !!")


        case 2:

            mycursor.execute("SELECT *FROM Students")

            data = mycursor.fetchall()
            for x in data:
                print(x)


        case 3:

            ID = int(input("Enter Student ID:"))

            sql = ("SELECT *FROM Students WHERE ID = %s")
            value = (ID,)

            mycursor.execute(sql, value)

            data = mycursor.fetchall()
            for x in data:
                print(x)


        case 4:
            ID = int(input("Enter Student ID:"))

            sql = ("SELECT *FROM Students WHERE ID = %s")
            value = (ID,)
            
            mycursor.execute(sql, value)

            data = mycursor.fetchall()
            for x in data:
                print(x)

            IDE = int(input("\nEnter Student ID:"))
            Fname = input("Enter the Fname of Student:")
            Lname = input("Enter the Lname of Student:")
            Branch = input("Enter the Branch of Student:")

            query = "UPDATE Students SET Fname = %s, Lname = %s, Branch = %s WHERE ID = %s"
            val = (Fname, Lname, Branch , IDE)

            mycursor.execute(query, val)
            mydb.commit()

            print(mycursor.rowcount,"Student Record Updated")
            
            
        case 5:
            ID = int(input("Enter Student ID:"))

            sql = ("DELETE FROM Students WHERE ID = %s")
            value = (ID, )

            mycursor.execute(sql, value)
            mydb.commit()

            print(mycursor.rowcount,"Student Record Deleted !!")


        case 6:
            print("Thank You !!")
            break


        case _:
            print("Invalid Choice !!")
            print("Please Enter Choice Between(1-6)")












