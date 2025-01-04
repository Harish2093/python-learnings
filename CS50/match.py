name = input("what is your name? ")

match name:
    case "Harish" | "HP":
        print("You are Harish")
    case "Deepak" | "DP":
        print("You are Deepak")
    case _:
        print("I don't know who you are")