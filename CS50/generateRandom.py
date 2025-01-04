import random
from collections import Counter

n = random.choice([100, 1000, 10000])

out = []
for i in range(n):
    out.append(random.choice(["heads", "tails"]))
print(Counter(out))


out_int = []
for i in range(n):
    out_int.append(random.randint(1, 10))
print(Counter(out_int))