import csv
# with open("students.csv", "a") as file:
#     while True:
#         name = input("Enter student name: ")
#         if name == "exit":
#             break
#         file.write(name + "\n")

students = []
# with open("students.csv", "r") as file:
#     for line in file:
#         name, year = line.split(",")
#         students.append({"name": name, "year": year})

with open("students.csv", "r") as file:
    reader = csv.reader(file) # csv.DictReader(file) will return a dictionary instead of a list, row['name']
    for name, year in reader:
        students.append({"name": name, "year": year})

# def get_name(student):
#     return student["name"]

for student in sorted(students, key=lambda student:student['name']):
    print(f"{student['name']} was in year {student['year']}")


