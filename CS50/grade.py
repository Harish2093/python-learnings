score = int(input("Score: "))

#instructor solved this using if, elif and else. Let's try using a for loop

boundaries = [60, 70, 80, 90, 100]
grades = ['F', 'D', 'C', 'B', 'A']

for i in range(len(boundaries)):
    if score < boundaries[i]:
        print(grades[i])
        break