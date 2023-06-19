#
# list = input("please write words: ").split()
#
# print(list)
# print(list.reverse())

user_list = input('Please enter list elemet separeted with ',': ').split(', ')

    for item in user_list[::-1]:
        print(item)