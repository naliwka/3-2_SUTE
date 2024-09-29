def good_students(students):
    # Обчислення середньої оцінки
    total_grade = sum(student[2] for student in students)
    average_grade = total_grade / len(students)

    # Фільтрування студентів з вище середньою оцінкою
    good_students_list = [student[0] for student in students if student[2] > average_grade]

    # Виведення результатів
    print("Студенти", ", ".join(good_students_list), "у поточному семестрі навчалися добре")


def main():
    students = (
        ("Авєріна", 20, 85),
        ("Гортенко", 21, 75),
        ("Антонова", 19, 90),
        ("Коваленко", 22, 80),
        ("Прилипко", 20, 95),
        ("Бондаренко", 21, 70),
        ("Попов", 22, 88)
    )

    good_students(students)


if __name__ == "__main__":
    main()