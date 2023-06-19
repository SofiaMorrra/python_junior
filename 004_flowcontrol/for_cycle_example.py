# # iterable object
# people = ['Jack', 'Mary', 'Bob', 'Simon', 'Jane']
#
# for person in people:
#     print(f'Hello {person}')
# # for x in people:
# #     print(f'Hello {x}')
# print('Good bye!')
#
# people = [('Jack', 25, 'male'), ('Sarah', 18, 'female'), ('Mary', 21, 'female'), ('Bob', 30, 'male')]
# # new_people = []
# #
# # for person in people:
# #     print(f'This is {person[0]}. He is {person[1]} years old.')
# #     # print(person)
# #     # print(type(person))
# #     new_people.append((person[0], person[2]))
# #
# # print(new_people)
#
# for person in people:
#     if person[2] == 'male':
#         print(f'This is {person[0]}. He is {person[1]} years old.')
#     elif person[2] == 'female':
#         print(f'This is {person[0]}. She is {person[1]} years old.')

# people = [('Jack', 25, 'male'), ('Sarah', 18, 'female'), ('Mary', 21, 'female'), ('Bob', 30, 'None')]
#
# for name, age, gender in people:
#     if gender == 'male':
#         print(f'This is {name}. He is {age} years old.')
#     elif gender == 'female':
#         print(f'This is {name}. She is {age} years old.')
#     else:
#         print(f'This is {name}. It is {age} years old.')

# print(list(range(10)))
# print(list(range(10, 20, 2)))  # ot kakogo, do kakogo, s kakim promezutkom

# for x in range(0,10):
#     print(x ** 2)

for num1 in range(0,10):
    for num2 in range(0, 10):
        for num3 in range(0, 10):
            for num4 in range(0, 10):
                print(num1, num2, num3, num4)
    