def greater_than_2(n):
    return True if n > 2 else False

h1 = [1, 2, 3, 4, 5, 6, 7]
out = filter(greater_than_2, h1)
print(out)
print(list(out))
print(list(map(greater_than_2, h1)))