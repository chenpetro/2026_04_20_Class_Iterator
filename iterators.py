from intertools import count, repeat, cycle

iterator = count(start=20)

print(next(iterator))
print(next(iterator))
print(next(iterator))


iterator1 = repeat("Hello", times=3)
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))


iterator = cycle([1, 2, 3, 4])
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))