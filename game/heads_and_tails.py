import random

print('Игра "Орел и решка" ')
print('Кидаем монету 100 раз')

coin = ['Орел', 'Решка']
heads = 0
tails = 0

for _ in range(100):
    if random.choice(coin) == 'Орел':
        heads += 1
    else:
        tails += 1

print(f'За 100 бросков выпало "Орел" - {heads} раз, а "Решка" - {tails} раз')
