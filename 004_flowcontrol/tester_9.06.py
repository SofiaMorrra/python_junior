x = 5

student = {'name': 'jack', 'age': 18, 'courses': ['math', 'art', 'english'],
           1: 'int_key', 0.2: 'float_key', x: 'variable', 'var_key': x, True: 'HELLO'}  # Dictionary (dict)

print(type(student))
print(bool(student))

print(student['courses'])
# print(student)

student['name'] = 'Bob'
student['phone'] = '536-7896'
print(student.get('address', []))
print(student)


sample = ['jack', 'smith', 18], ['mary', 'gold', 21], ['simon', 'green', 30]
people = []
for person in sample:
  some_dict = {}
  some_dict['name'] = person[0]
  some_dict['surname'] = person[1]
  some_dict['age'] = person[2]
  people.append(some_dict)

print(people)

