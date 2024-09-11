def main():
    #name = get_name()
    #house = get_house()
    student = get_student()
    #print(f"hello, {student[0]} from {student[1]}")
    print(f"hello, {student['name']} from {student['house']}")


# def get_name():
#     return input("Enter student name: ").strip()

# def get_house():
#     return input("Enter student house: ").strip()

def get_student():
    #name = input("Enter student name: ").strip()
    #house = input("Enter student house: ").strip()
    '''
    student = {}
    student["name"] = input("Enter student name: ").strip()
    student["house"] = input("Enter student house: ").strip()
    '''
    return {
        "name": input("Enter student name: ").strip(),
        "house": input("Enter student house: ").strip()
    }
 
if __name__ == "__main__":
    main()