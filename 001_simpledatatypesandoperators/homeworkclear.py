current_year = 2022
year_of_birth = 1988
user_age = (int(current_year) - int(year_of_birth))
print(user_age)

x = 152
y = 132
code_2 = int(((x % y)*13)**0.5)  # mog bqt float no stal int
print(code_2)

code_1 = '354'  # str
code_3 = 132  # int
result = str(code_1) + "-" + str(code_2) + "-" + str(code_3)
print(str(code_1), str(code_2), str(code_3), sep="-", end="\n")

user_name = 'John'
user_surname = 'Smith'

print("Hello {0} {1}. Your are {2} years old. Your secret code {3}".format(str(user_name), str(user_surname), str(user_age), str(result)))

age = str(current_year - year_of_birth)
print(age)

code2_part1 = x % y
code2_part2 = code2_part1 * 13
code2_part3 = code2_part2 ** 0.5  # import math
code2 = int(code2_part3)
print(code2)

code = code_1 + '-' + str(code2) + '-' + str(code_3)

print('hello ' + user_name + ' ' + user_name + '. Your are' +
      str(age) + ' years old. Your secret code is ' + code + '.')
