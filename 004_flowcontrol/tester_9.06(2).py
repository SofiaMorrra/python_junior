sample2 = {'name': 'Jack', 'surname': 'Smith'}

sample2.update({'name': 'Michael', 'age': 26})
print(sample2)

del sample2['name']
print(sample2)
x = sample2.pop('surname')
print(sample2)
print(x)