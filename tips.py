#1 Save memory with generators

import sys
dashline = '-' * 100


my_list = [i for i in range(1000)]
print(sys.getsizeof(my_list))
print(sum(my_list))


my_gen = (i for i in range(1000))
print(sys.getsizeof(my_gen))
print(sum(my_gen))

print(dashline)
#2 define default value  for a dictionary with get and setdefault

my_dict = {'name': 'John', 'age': 25}
#salary = my_dict.get('salary', 0)
#print(salary)


salary = my_dict.setdefault('salary', 100)
print(salary)
print(my_dict)

name = my_dict.setdefault('name', "harish")
print(name)
print(dashline)
# set default will fetch the value if the key is present else it will set the default value to the key


#3 Count hashable objects with collections.Counter
from collections import Counter
my_list = [30, 20, 10, 10, 10, 20, 40, 50, 20, 30, 10, 30]
Copunter = Counter(my_list)
print(Copunter)

print(dashline)
print(Copunter.most_common(3))


#4 Merge dictionaries with {**d1, **d2}
d1 = {'name': 'John', 'age': 25}
d2 = {'name': 'John','salary': 1000, 'age': 30}

final = {**d1, **d2}
print(final)