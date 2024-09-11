#MAP function

# map (funciton_to_apply, list of inputs)

h1 = [1,2,3,4]
sq = []


for item in h1:
    sq.append(item**2)

#print(sq)

def square(n):
    return n**2

m = map(square, h1)
print(m)
print(list(m))
