# employees - список работников, Bob больше не работает в этой комании
# удалите его из списка
employees = ['Jack', 'Mary', 'Samantha', 'Michael', 'Bob']
employees.remove('Bob')

# как известно кортеж (tuple) неизменяемый тип данных
# сделайте так чтобы кортеж german_cars был отсортирован в алфавитном порядке
german_cars = ('Volkswagen', 'BMW', 'Skoda', 'Mercedes-Benz', 'Seat', 'Audi')
german_cars = list(german_cars)
german_cars.sort()
german_cars = tuple(german_cars)
print(german_cars)

# Создайте новый список на основе списка some_numbers
# в новом списке не должно быть дубликатов, все цифры должны быть в порядке убывания
some_numbers = [1, 1, 2, 3, 3, 5, 5, 7, 8, 8, 8]
new_numbers = list(set(some_numbers))
new_numbers.sort(reverse=True)
print(new_numbers)

# в списке actions занятия которыми занимался Jack летом
# используйте данный список чтобы вывести в консоль строку
# "I am Bob and this summer I was cycling, camping, hiking, swiming.
actions = ['Cycling', 'Camping', 'Hiking', 'Swiming']
message = f'I am Bob and this summer i was {", ".join(actions)}.'
print(message)

# Используя индексацию в [] выведете только четные числа
# Второй вывод пусть выведет только нечетные
# Третий вывод пусть выведет этот же список но наоборот
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1::2])

print(numbers[::-1])
# Задано два множества, выведете в консоль фрукты которые любят и Jack и Mary
# Выведете в консоль фрукты которые любит только Jack
# Выведете в консоль фрукты которые любит только Mary
jacks_favourite_fruits = {'Banana', 'Orange', 'Apple'}
marys_favourite_fruits = {'Mango', 'Grapefruit', 'Banana'}
print(jacks_favourite_fruits.intersection(marys_favourite_fruits))
print(jacks_favourite_fruits.difference(marys_favourite_fruits))
print(marys_favourite_fruits.difference(jacks_favourite_fruits))
