# x = 0
# while x < 100:
#     print('I can\'t stop!', x)
#     x += 1

distance_to_target = float(input('enter distance KM: '))
current_position = 0
step = 0.6
cnt = 0

while current_position < distance_to_target * 1000:
    current_position += step
    cnt += 1

print(f'{cnt} steps')