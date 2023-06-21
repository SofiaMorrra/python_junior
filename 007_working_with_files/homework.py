# with open('trimushketera.txt', 'r') as file:
#     book = file.read()
#     print(book)

# with open('trimushketera.txt', encoding='utf-8') as file:
#     for line in file:
#         print(len(line), 'symbols.')

with open('trimushketera.txt', encoding='utf-8') as file:
    file = file.read()
    word_list = len(file.split())
    print(word_list)
    print(*sorted(list(file.lower().split())))

