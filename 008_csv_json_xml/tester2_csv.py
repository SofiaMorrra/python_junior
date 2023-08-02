import csv

# with open('test.csv', 'r', encoding='UTF8') as file:
#     csv_reader = csv.reader(file)
#     headers = next(csv_reader)
#     # csv_reader = list(csv_reader)
#
#     # print(list(csv_reader))
#     for line in csv_reader:
#         print(line)
#     print(headers)
#  # print('Town: ' + line[2])
# # normal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # normal_iterator = iter(normal)

# with open('test.csv', 'r', encoding='UTF8') as file:
#     csv_reader = csv.reader(file)   #(test, delimiter='*')  ukazqvaju chto delitelem javljaetsja '*' a ne zapjataja
#
#     with open('test_copy.csv', 'w', encoding='UTF8') as wfile:
#         csv_writer = csv.writer(wfile, lineterminator='\n')  #delimiter='*'
#
#         for line in csv_reader:
#             csv_writer.writerow(line)


with open('test.csv', 'r', encoding='UTF8') as file:  # tolko esli pervaja strochka naimenovanii
    csv_data = csv.DictReader(file)

    # for line in csv_data:
    #     print(line)
    with open('test_copy.csv', 'w', encoding='UTF8') as wfile:
        fieldnames = ['Name', 'Date of birth', 'Town']

        csv_writer = csv.DictWriter(wfile, fieldnames=fieldnames, lineterminator='\n')

        csv_writer