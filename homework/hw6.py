import sqlite3

db = sqlite3.connect('hw6.1')

c = db.cursor()

CREATE TABLE students (
id INT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
birth_year INT,
hobbies VARCHAR(255),
homework_score INT
)

INSERT INTO students (id, first_name, last_name, birth_year, hobbies, homework_score)
VALUES
(1, 'John', 'Doe', 1997, 'reading, hiking', 8),
(2, 'Jane', 'Smith', 1999, 'painting, playing guitar', 12),
(3, 'Robert', 'Johnson', 1996, 'photography, cooking', 6),
(4, 'Emily', 'Brown', 1998, 'dancing, travelling', 10),
(5, 'William', 'Anderson', 1995, 'playing basketball, watching movies', 9),
(6, 'Olivia', 'Taylor', 1997, 'listening to music, playing video games', 7),
(7, 'Alexander', 'Williams', 1999, 'drawing, writing', 11),
(8, 'Sophia', 'Davis', 1994, 'hiking, skiing', 8),
(9, 'Michael', 'Garcia', 1998, 'playing chess, coding', 13),
(10, 'Grace', 'Harrison', 1996, 'practicing yoga, reading', 6);


SELECT * FROM students WHERE LENGTH(last_name) > 10;


UPDATE students SET first_name = 'Genius' WHERE homework_score > 10;


SELECT * FROM students WHERE first_name = 'Genius';


DELETE FROM students WHERE id % 2 = 0;


db.commit()
db.close()
