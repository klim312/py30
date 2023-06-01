def delete_student(conn, student_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("Студент успешно удален")


def update_student(conn, student_id, name, group, grade):
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, group=?, grade=? WHERE id=?", (name, group, grade, student_id))
    conn.commit()
    print("Информация о студенте успешно изменена")

