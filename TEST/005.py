# tuple_a = (1, 2, 3, 5, 8)
# tuple_b = (8, 2, 5)
# tuple_ab = tuple_a + tuple_b

a = (1, 2, 3, 5, 8)
b = (8, 2, 5)
a = a[:2] + b + a[2:]
print(a)

a = list(a)
for element in b:
    a.insert(2, element)

a = tuple(a)
print(a)