string_sample1 = "Hello world world"
string_sample2 = "first letTer is loWercase"
string_sample3 = "***extra symbols   "
german_sample = 'der fluß'


print(string_sample1[1])
print("world"[0])
print(len("world"))
# [START:END]
print(string_sample1[0:4])
print(string_sample1[0:])  # [:12]
print(string_sample1[-1])
#  w o r l d
#  0 1 2 3 4
# -5-4-3-2-1
print(string_sample1[-5:-1])
# [START:END:STEP]
print(string_sample1[2:14:2])  # OT 2 DO 14 BERET KAZDQI VTOROI
print(string_sample1[::-1])  # PEREVERNUTAJA STROKA
print(len("world"))
print('world' in string_sample1)
print(string_sample2 in string_sample1)
print('World' in string_sample1)

# print(string_sample1.upper())
# print(string_sample1)
# # string_sample1 = string_sample1.upper()
# # print(string_sample1)

print(german_sample.lower())
print(german_sample.casefold())

print(string_sample2.capitalize())
print(string_sample2.title())
name = "jevgenia-sofia"
print(name.title())

print(string_sample3.strip())  # uberet tolko liwnie probelq
print(string_sample3.strip("* "))
print(string_sample1.replace("world", "planet", 1))  # pervoe slovo menjaem na vtoroe
print(string_sample1.replace("world ", "", 1).replace(" ", "*"))

print(string_sample1.split())
print(string_sample1.split('w'))
a, b, c = "80, 60, 90".split(", ")
print(a, b, c)

print(string_sample1.count("o"))  # skolko raz vstrechaetsja v etoi stroke
print(string_sample1.find("world"))  # na kakoi stroke vstrechaetsja slovo vpervqe
print(string_sample1.count("world",7))

a = 'th\\sa\tma\nat\'s'
print(a)
print(len(a))

print('hello'
      'world')
print('''rom
to   be
        car''')

print('\\n')
print('\n')

salary = 1000
text = 'Johns salary is {1}, {0}'

print(text.format(salary, True))

text = '{name:}s salary is {sal:.2f}'
print(text.format(name='Jack', sal=salary))

name = 'John'
print(f'{name.upper()}\'s salary is {salary:.2f} eur.')

# byte_sting =