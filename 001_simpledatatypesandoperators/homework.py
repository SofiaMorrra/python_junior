# # years
# current_year = 2022
# year_of_birth = 1988
# # code parts
# code_1 = '354'
# code_3 = 132
# # name
# user_name = 'John'
# user_surname = 'Smith'
# # code 2 data
# x = 152
# y = 132

current_year = 2022
year_of_birth = 1988
user_age = (int(current_year) - int(year_of_birth))
print(user_age)

x = 152
y = 132
# code_2 = float(int(((x/y)*13)**0.5))  # vernqi variant no pokazqvaet s tochkoi 3.0
# code_2 = print(int(((x//y)*13)**0.5))  # ne nuzno bqlo pisat print pokazqvaet None vmesto chisla
code_2 = int(((x//y)*13)**0.5)  # mog bqt float no stal int
print(code_2)

code_1 = '354'  # str
code_3 = 132  # int
# print(str(code_1) + str(-) + str(code_2) + str(-) + str(code_3))  # ..
# print((code_1), str(code_2), (code_3), sep="-")   #verno
# secret_code = (str(code_1), int(code_2), int(code_3), sep="-")  #ne verno
print(str(code_1), str(code_2), str(code_3), sep = "-", end = "\n")
# result = int(str(code_1), str(code_2), str(code_3), sep = "-")
result = "354-3-132"
# Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.

user_name = 'John'
user_surname = 'Smith'

# print("Hello" + " " + str(user_name) + " " + str(user_surname) + "." + " Your are " + str(user_age) + " years old.")
print("Hello {0} {1}. Your are {2} years old. Your secret code {3}".format(str(user_name), str(user_surname), str(user_age), str(result)))