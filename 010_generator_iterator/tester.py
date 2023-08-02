def squares(start, stop):
    for num in range(start, stop):
        yield num ** 2

x = squares(1, 100)
print(x)

print(next(x))
print(next(x))
print(next(x))

for i in x:
    print(i)