# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

# with open('sample_text.txt', 'r') as file:
#     print(file.name)
#     print(file.mode)
#     print(file.encoding)
#     print(file.closed)
#     # #print(file.close())
#
# print(file.closed)

# with open('sample_text.txt', 'r') as file:
#     file_content = file.read()
#     print(file_content)
#     print(type(file_content))

# with open('sample_text.txt', 'r') as file:
#     file_content = file.readlines()
#     print(file_content)
#     print(len(file_content))

with open('sample_text.txt', 'r') as file:
    file_content = file.readline()
    print(file_content)
    file_content2 = file.readline()
    print(file_content2)

# with open('sample_text.txt', 'r') as file:
#     data = file.read()
#
#
# with open('sample123.txt', 'w') as file:   #sozdaet novqi fail
#     file.write(data)
#     file.write('hello')

