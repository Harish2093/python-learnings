while True:
    try:
        x = int(input("x: "))
        break
    except ValueError:
        print("Not an integer")
        continue
    #else:
    #    break

print(f"x is {x}")