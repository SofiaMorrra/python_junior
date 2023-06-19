# test_list = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10, 10]
#
# max_count = 0
# new_list = []
#
# for num in test_list:
#     if test_list.count(num) > max_count:
#         max_count = test_list.count(num)
# print(max_count)
#
# for num in test_list:
#     if test_list.count(num) == max_count:
#         new_list.append(num)
# print(new_list)

# empty_dict ={}
#
# for num in test_list:
#     empty_dict[num] = test_list.count(num)
#
# # print(empty_dict)
#
# result = []
# for key in empty_dict.keys():
#     if empty_dict[key] == max(empty_dict.values()):
#         result.append(key)
#
#    print(result)


# 1234565 sec = 14:6:56:5
seconds = 1234565
days = seconds // (24 * 3600)
print(days)
seconds %= 24 * 3600
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f'{days}:{hours}:{minutes}:{seconds}')