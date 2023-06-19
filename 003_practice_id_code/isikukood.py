while True:
    idcode = input('please enter ID: ')

    if idcode.lower() == 'exit':
        print('good bye!')
        quit()

    if len(idcode) != 11:
        if len(idcode) > 11:
            print('too long')
        else:
            print('too short')
        continue
    else:
        while True:
            user_menu = input('please select:\n'
                              '1.gender\n'
                              '2.date of birth\n'
                              '3.region\n'
                              '4.validate\n'
                              '5.change ID\n'
                              '0.exit\n'
                              '--->')
            if user_menu == '1':
                if int(idcode[0]) % 2 == 0:
                    print('you are FEMALE')
                else:
                    print('your are female')
            elif user_menu == '2':
                if idcode[0] == '1' or idcode[0] == '2':
                    bcent = '18'
                elif idcode[0] == '3' or idcode[0] == '4':
                    bcent = '19'
                elif idcode[0] == '5' or idcode[0] == '6':
                    bcent = '20'
                elif idcode[0] == '7' or idcode[0] == '8':
                    bcent = '21'
                else:
                    bcent = None

                if bcent is None:
                    print(f'{idcode[5:7]}.{idcode[3:5]}.{idcode[1:3]}')
                else:
                    print(f'{idcode[5:7]}.{idcode[3:5]}.{bcent}{idcode[1:3]}')
            elif user_menu == '3':
                if int(idcode[7:10]) in range(1, 11):
                    print("Kuresare haigla")
                elif int(idcode[7:10]) in range(11, 20):
                    print("tartu")
                elif int(idcode[7:10]) in range(21, 151):
                    print("ida-tallinna")
            elif user_menu == '4':
                chk1 = [1, 2, 34567891]
                chk2 = [3456789123]
                # 38803160272
            elif user_menu == '5':
                break
            elif user_menu == '0':
                print('good bye!')
                quit()
            else:
                print('choice is out of range!')
                continue
print('good bye!')



# for x in range(10):
#     if x == 5:
#         continue
#     elif x == 7:
#         break
#     print(x)


