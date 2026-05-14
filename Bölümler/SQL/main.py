#Bismillah
# to work with sql we need two libraries
import sqlite3
import os # operating system



def create_database():
    # to delete existed file
   # if os.path.exists('students.db'):
    #    os.remove('students.db')
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()# tool used to process data
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMARY KEY,name VARCHAR NOT NULL ,age INTEGER,email VARCHAR UNIQUE,city VARCHAR)  ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (id INTEGER PRIMARY KEY,course_name VARCHAR NOT NULL ,instructor TEXT,credits INTEGER)  ''')


def insert_sample_data(cursor):
    #cursor.execute('''INSERT INTO Students (name,age,email,city)''') we can use this one too, one by one
    students = [
        (1,'Alice Johnson',20,'alice@gmail.com','New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Students VALUES (?,?,?,?,?)", students) # question mark is unkown we fill later.

    courses = [(1,'Python Programming','Dr. Anderson',3),
               (2, 'Web Development', 'Prof.Wilson', 4),
               (3, 'Data Science', 'Dr. Taylor', 3),
               (4, 'Mobile Apps', 'Prof.Garcia', 2)
               ]
    cursor.executemany("INSERT OR IGNORE INTO Courses VALUES (?,?,?,?)", courses)
    print("Sample data inserted successfully")


def basic_sql_operations(cursor):
    #1) SELECT ALL
    print("---------Select All----------")
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    for record in records:  # ✅ print the fetched records
        print(record)


    # 2) SELECT Columns
    print("---------Select Columns----------")
    cursor.execute("SELECT name,age FROM Students")
    records = cursor.fetchall()
    print(records)

    #3) WHERE clause -> filtering
    print("---------Where age = 20----------")
    cursor.execute("SELECT * FROM Students WHERE age = 20")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #4) WHERE with string
    print("---------Where city = New York----------")
    cursor.execute("SELECT * FROM Students WHERE city = 'New York'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #5) ORDER BY
    print("---------Order by age----------")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)


    #6) LIMIT
    print("---------Limit by 3----------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall()
    for row in records:
        print(row)


def sql_update_delete_insert_opereations(conn,cursor):
    #1) Insert
    cursor.execute("INSERT INTO Students Values(6,'Frank Miller',23,'frank@gmail.com','Miami')",)
    conn.commit() #to find immediately within the database


    #2) UPDATE
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()

    #3)DELETE
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()


def aggregate_functions(cursor):
    #1) Count
    print("--------------Aggregate Functions Count-------------")
    cursor.execute("SELECT COUNT(*) FROM Students")
   # result = cursor.fetchall() # fetchall gives list
   # if we know we only obtain one value we can use fetchone instead fetchall
    result = cursor.fetchone()
    print(result[0])

    #2) Avarage
    print("--------------Aggregate Functions Avarage-------------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    #3) Max- Min
    print("--------------Aggregate Functions Max-Mİn-------------")
    cursor.execute("SELECT MAX(age),MIN(age) FROM Students")
    result = cursor.fetchone()
    max_age , min_age = result
    print(max_age)
    print(min_age)

    #4) GROUP BY
    print("--------------Aggregate Functions Group by-------------")
    cursor.execute("SELECT city, COUNT(*) FROM Students group by city")
    result = cursor.fetchall()
    print(result)


def questions():
    print("--------------Questions---------------")
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ve derslerin isimlerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi alan öğrencileri getirin

    Detaylı
    1) Öğrencileri alfabetik şekilde dizerek getirin
    2) Yermi yaşından büyük öğrencileri isme göre dizerek getirin
    3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    4) Sadece 'New York' da yaşamayan öğrencileri getirin
    '''


def answers(cursor):
    print("--------------Answers---------------")

    # 1) Bütün kursların bilgilerini getirin
    cursor.execute("SELECT * FROM Courses")
    result = cursor.fetchall()
    print(result)

    # 2) Sadece eğitmenlerin ve derslerin isimlerini getirin
    cursor.execute("SELECT course_name, instructor FROM Courses")
    result = cursor.fetchall()
    print(result)

    # 3) Sadece 21 yaşındaki öğrencileri getirin
    cursor.execute("SELECT * FROM Students WHERE age = 21")
    result = cursor.fetchall()
    print(result)

    # 4) Sadece Chicago'da yaşayan öğrencileri getirin
    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago'")
    result = cursor.fetchall()
    print(result)

    # 5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    cursor.execute("SELECT * FROM Courses WHERE instructor = 'Dr. Anderson'")
    result = cursor.fetchall()
    print(result)

    # 6) İsmi 'A' ile başlayan öğrencileri getirin
    cursor.execute("SELECT * FROM Students WHERE name LIKE 'A%'")
    result = cursor.fetchall()
    print(result)

    # 7) 3 ve üzeri kredi alan kursları getirin
    cursor.execute("SELECT * FROM Courses WHERE credits >= 3")
    result = cursor.fetchall()
    print(result)

    # Detaylı 1) Öğrencileri alfabetik şekilde dizerek getirin
    cursor.execute("SELECT * FROM Students ORDER BY name ASC")
    result = cursor.fetchall()
    print(result)

    # Detaylı 2) 20 yaşından büyük öğrencileri isme göre dizerek getirin
    cursor.execute("SELECT * FROM Students WHERE age > 20 ORDER BY name ASC")
    result = cursor.fetchall()
    print(result)

    # Detaylı 3) New York veya Chicago'da yaşayan öğrencileri getirin
    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago' OR city = 'New York'")
    #cursor.execute("SELECT name,city FROM Students WHERE city IN('New York','Chicago')")
    result = cursor.fetchall()
    print(result)

    # Detaylı 4) New York'da yaşamayan öğrencileri getirin
    cursor.execute("SELECT * FROM Students WHERE city != 'New York'")
    result = cursor.fetchall()
    print(result)













def main():
   conn, cursor = create_database()
   try:
       create_tables(cursor)
       insert_sample_data(cursor)
       basic_sql_operations(cursor)
       sql_update_delete_insert_opereations(conn,cursor)
       aggregate_functions(cursor)
       answers(cursor)
       conn.commit() # apply things that cursor have done.
   except sqlite3.Error as e:
       print(e) #print exception

   finally:
       conn.close() # important !




if __name__ == "__main__":
    main()
   #conn, cursor = create_database() # it will create database and give us connection and control to process
  # cursor.execute('''CREATE TABLE students (''') to run sql commands