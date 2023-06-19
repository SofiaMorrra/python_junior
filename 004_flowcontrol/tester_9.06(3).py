sample2 = {'name': 'Jack', 'surname': 'Smith'}

# for x in sample2:
#     print(x)
for x in sample2.values():
     print(x)


print(sample2.keys())
print(sample2.values())
print(sample2.items())

for key, value in sample2.items():
      print(key,value)