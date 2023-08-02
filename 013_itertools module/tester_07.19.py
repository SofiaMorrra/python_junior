import itertools

# cnt = itertools.count(start=20, step=-2)

# print(next(cnt))
# print(next(cnt))

# data = [100, 200, 300, 400]
# data2 = ['Mon', 'Tue', 'Wed', 'Thu']

# print(list(zip(data, data2, [1, 2, 3, 4])))

# print(list(itertools.zip_longest(data2, range(10))))

# cnt = itertools.cycle(['on', 'off'])

# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(list(zip([1, 2, 3, 4, 5], cnt)))

# cnt = itertools.repeat(['on', 'off'])
#
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))
# print(next(cnt))

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
selectors = [True, False, False, True]
names = ['Jack', 'Sarah', 'Bob']

def more_than_two(x):
    if x > 2:
        return True
    return False

# res = itertools.takewhile(more_than_two, numbers2)
res = itertools.dropwhile(more_than_two, numbers2)  # poka uslovie vqpolnjaetsja ignoriruem, kak tolko poivljaetsja False, pokazat vse ostalnoe
for x in res:
    print(x)


# result = itertools.compress(letters, selectors)
# for item in result:
#     print(item)
#
# def more_than_two(x):
#     if x > 2:
#         return True
#     return False
#
# res = itertools.filterfalse(more_than_two, numbers2)   # te kotorqe vozvrowjaut False
# for x in res:
#     print(x)

# res = filter(more_than_two, numbers2)
# for x in res:
#     print(x)

# result = itertools.combinations(letters, 2)    # ne imeet znachenie porjadok, povtorjatsja mozno

# result = itertools.permutations(letters, 4)  # imeet znachenie porjadok

# result = itertools.product(letters, numbers, repeat=2)  # porjadok imeet znachenie i mozno povtojat simvolq

# result = itertools.combinations_with_replacement(numbers, 4)  # porjadok ne imeet znachenija, simvolq mozno povtorjat
# for entry in result:
#     print(entry)

