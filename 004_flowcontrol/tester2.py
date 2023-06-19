# # isikukood = '38803160272'
# #
# # if len(isikukood) == 11:
# #     print(isikukood, 'OK')
# # elif len(isikukood) < 11:
# #     print('Code is too short')
# # else:
# #     print('Code is too long')
# #
# isikukood = '38803160272'
#
# if len(isikukood) == 11:
#     print(isikukood, 'OK')
# else:
#     if len(isikukood) < 11:
#         print('Code is too short')
#     else:
#         print('Code is too long')

# y = 14
# if y % 7 == 0 and y % 14 == 0:
#     print('Y divided by 7 and 14')
# elif y % 14 ==0:
#     print('Y divided by 14')
# elif y % 7 == 0:
#     print('Y divided by 7')
#  num1 = 10
#  num2 = 5
#
#  if num1 > 5 and num2 >= 5 and num1 - num2 == 5:  # AND dolzno bqt vse uslovija vernq no OR tiolko odno iz nih
#      print('OK')
#  else:
#      print('NOK')

user_name = input('Please enter your name: ')
if len(user_name) > 5:
    print(f'Hi {user_name}. You have a long name.')
else:
    print(f'Hi {user_name}. You have a short name.')