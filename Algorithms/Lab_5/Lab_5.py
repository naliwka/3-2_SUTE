class Person:
    total_persons = 0

    def __init__(self, name, age, address):
        self.name = name
        self._age = age
        self.address = address
        self.faculty = None
        Person.total_persons += 1

    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative.")
        else:
            self._age = age

    def get_age(self):
        return self._age

    age = property(get_age, set_age)


class Student(Person):
    total_students = 0

    def __init__(self, name, age, address, group):
        super().__init__(name, age, address)
        self.group = group
        Student.total_students += 1

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Address: {self.address}, Group: {self.group}"


class Teacher(Person):
    total_teachers = 0

    def __init__(self, name, age, address, department, position):
        super().__init__(name, age, address)
        self.department = department
        self.position = position
        Teacher.total_teachers += 1

    def __str__(self):
        return f"Teacher: {self.name}, Age: {self.age}, Address: {self.address}, Department: {self.department}, Position: {self.position}"


def add_person():
    person_type = input("Enter person type (Student/Teacher): ").lower()
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    address = input("Enter address: ")

    if person_type == "student":
        group = input("Enter group: ")
        return Student(name, age, address, group)
    elif person_type == "teacher":
        department = input("Enter department: ")
        position = input("Enter position: ")
        return Teacher(name, age, address, department, position)
    else:
        print("Invalid person type.")
        return None


def print_persons(persons):
    print("\nList of Persons:")
    for person in persons:
        print(person)
    print(f"\nTotal Students: {Student.total_students}")
    print(f"Total Teachers: {Teacher.total_teachers}")


def main():
    persons = []

    while True:
        choice = input("\nEnter 'add' to add a person or 'done' to finish: ").lower()
        if choice == "add":
            person = add_person()
            if person:
                persons.append(person)
        elif choice == "done":
            break
        else:
            print("Invalid choice.")

    print_persons(persons)
    print("\nEntered data about persons:")
    for person in persons:
        print(person)

if __name__ == "__main__":
    main()