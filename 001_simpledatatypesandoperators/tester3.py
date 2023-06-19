int_var = 123
float_var = 123.123
str_var = "my dear!"
bool_var = True

# print(str(None))
#
# print(bool(-0.12))  # vse krome 0 i pustoi stroki true
# # print(bool(0))   #FALSE bool(0.0) FALSE bool("")
# print(bool(None))
#
# print("Hello" + str(123))
# print("Hello" + " " + str(123))
# print(float(float_var) ** 2)
#
# user_age = input("Please enter your age: ")
# my_age = 58
# print(type(user_age))
# print(my_age - int(user_age)) # objazatelno INT bez nego vozrast prosto stroka a na chislo

# str_var = "1234.213"
# print(str_var, type(str_var))
# str_var = int(float(str_var))
# print(str_var, type(str_var))

# print(int_var, type(int_var))
# int_var = float(int_var)
# print(int_var, type(int_var))

# print(float_var, type(float_var))
# float_var = int(float_var)
# print(float_var, type(float_var))

side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))

half_perimeter = (side_a + side_b + side_c) / 2
print(half_perimeter)

area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** 0.5
print(area)
