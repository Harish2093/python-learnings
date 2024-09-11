name = input("Enter student name: ").strip()
print(f"hello, {name}")

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")