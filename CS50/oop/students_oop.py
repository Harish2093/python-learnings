class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"hello, {student.name} from {student.house}")


def get_student():
    name = input("Enter student name: ").strip()
    house = input("Enter student house: ").strip()
    return Student(name, house) 

if __name__ == "__main__":
    main()