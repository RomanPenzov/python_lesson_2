# циклы for

i = 0
for i in range(10):
    print(i)
    if i == 5: break

answer = None

for i in range(10):
    answer = input('Какая лучше марка автомобиля?')
    if answer == 'Volvo':
        print('Вы абсолютно правы')
        break

for i in range(10):
    if i == 9: break
    if i < 3: continue
    else: print(i)