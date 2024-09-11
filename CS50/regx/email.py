import re

email = input("Email: ")
#pattern = r"^.+@.+\..+$"
#pattern = r"^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
#pattern = r"^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.(com|in|edu|gov)$"
#pattern = r"^\w+@\w+\.\w+$"
pattern = r"^\w+@(\w+\.)*\w+\.\w+$"
if re.search(pattern, email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")