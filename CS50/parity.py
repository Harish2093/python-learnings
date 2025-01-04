# code to check if a number is even or odd

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Better way to write this code have a main function and a function to check if the number is even or odd

def main():
    number = int(input("Enter a number: "))
    if is_even_much_better(number):
        print("Even")
    else:
        print("Odd")
# def is_even(number: int) -> str:
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# def is_even_better(number: int) -> str:
#     return "Even" if number % 2 == 0 else "Odd"


def is_even_much_better(number: int) -> bool:
    return number % 2 == 0

if __name__ == "__main__":
    main()