import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
               (id INTEGER PRIMARY KEY,
                hobby TEXT,
                first_name TEXT,
                last_name TEXT,
                birth_year INTEGER,
                homework_score INTEGER)''')

students = [
    ('Sema', 'Kim', 2004, 8, 'volleyball'),
    ('Igor', 'Li', 1992, 6, 'running'),
    ('Klim', 'Shin', 2005, 12, 'painting'),
    ('Nikole', 'Shin', 1997, 9, 'sewing'),
    ('Yaroslav', 'Litvinov', 2001, 11, 'swimming'),
    ('Amiran', 'Adzhanabaev', 2003, 7, 'dancing'),
    ('Ajara', 'Tyrdalieva', 2002, 10, 'yoga'),
    ('Alexsandr', 'Ivanov', 1998, 5, 'hiking'),
    ('Danil', 'Shpringer', 2000, 13, 'cooking'),
    ('Emily', 'Kim', 1999, 15, 'photography')
]

for student in students:
    cursor.execute("INSERT INTO students VALUES (NULL, ?, ?, ?, ?, ?)", student)

conn.commit()
conn.close()


conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM students WHERE length(last_name) > 10")
students = cursor.fetchall()
print("Students with last name longer than 10 characters:")
for student in students:
    print(student)

conn.close()


conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("UPDATE students SET first_name = 'Genius' WHERE homework_score > 10")
conn.commit()
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
print("All students after changing names:")
for student in students:
    print(student)

conn.close()


conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM students WHERE first_name = 'Genius'")
students = cursor.fetchall()
print("All genius:")
for student in students:
    print(student)

conn.close()


conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM students WHERE id % 2 = 0")
conn.commit()
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
print("All students after deleting even ones:")
for student in students:
    print(student)

conn.close()
