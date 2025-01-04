import bisect
a = [1,2,3,4,7,8,10]
number = 5
print(bisect.bisect(a, number))
print(bisect.insort(a, number))
print(bisect.insort_left(a, number))