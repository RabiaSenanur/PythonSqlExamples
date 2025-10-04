import sqlite3
import os

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn,cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students(
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
    ''')

    cursor.execute('''
        CREATE TABLE Courses(
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER)
        ''')

def insert_sample_data(cursor):

    students = [
        (1, 'Alice Johnson', 20 ,'alice@gmail.com','New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma David', 22, 'emma@gmail.com', 'Seattle')
    ]
    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)",students)

    courses = [
        (1, 'Python Programming','Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]
    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)",courses)

def basic_sql_operations(cursor):
    # 1) SELECT ALL
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]},Email: {row[3]}, City: {row[4]}")

    # 2) SELECT Columns
    cursor.execute("Select name,age FROM Students")
    records = cursor.fetchall()
    print(records)

    # 3) Where clause
    cursor.execute("Select name,age FROM Students Where age = 20")
    records = cursor.fetchall()
    print(records)

    # 4) Where with String
    cursor.execute("Select * FROM Students Where city= 'New York'")
    records = cursor.fetchall()
    print(records)

    # 5) Order BY
    cursor.execute("Select * FROM Students ORDER BY age")
    records = cursor.fetchall()
    print(records)

    # 6) LIMIT
    cursor.execute("Select * FROM Students LIMIT 3")
    records = cursor.fetchall()
    print(records)

def sql_update_delete_insert_operations(conn,cursor):
    # 1) INSERT
    cursor.execute("INSERT INTO Students Values (6, 'Frank Miller',23,'frank@gmail.com','Miami')")
    conn.commit()

    # 2) UPDATE
    cursor.execute("UPDATE Students SET age= 24 Where id=6")
    conn.commit()

    # 3) DELETE
    cursor.execute("DELETE FROM Students Where id= 6")
    conn.commit()

def aggregate_functions(cursor):
    # 1) Count
    print("---------Aggregate Functions Count-----------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 2) Average
    print("---------Aggregate Functions Average-----------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 3) MAX - MIN
    print("---------Aggregate Functions Max-Min-----------")
    cursor.execute("SELECT MAX(age),MIN(age) FROM Students")
    max_age,min_age = cursor.fetchone()
    print(f"Max age: {max_age}")
    print(f"Min age: {min_age}")

    # 4) GROUP BY
    print("---------Aggregate Functions GROUP BY-----------")
    cursor.execute("SELECT city,COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)
def main():
    conn,cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn,cursor)
        aggregate_functions(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()