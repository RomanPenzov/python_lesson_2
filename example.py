# задача 1 вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
print ('ЗАДАЧА # 1, вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.')
for i in range(1,6):
    print(i, 0)
print ('='*27)
print ('='*27)

# задача 2 пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.
print ('ЗАДАЧА # 2, пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5')
new_number = ''
for i in range(1,11):
    number = input('введите целое число от 0 и до ....')
    new_number = new_number + number
print(new_number, type(new_number))
new_number = int(new_number)
# print(new_number, type(new_number))
quant = 0
while new_number > 0:
    if new_number % 10 == 5:
        quant +=1
    new_number = new_number//10
print(quant)
print ('='*27)
print ('='*27)


# # Задача 3 Найти сумму чисел от 1 до 100
# sum = 0
#
# for i in range(1,101):
#     sum += i
# print(sum)

# задача 4 Найти произведение от 1 до 10
print ('ЗАДАЧА # 4, Найти произведение от 1 до 10')
mult = 1

for i in range(1,11):
    mult *= i
print(mult)
print ('='*27)
print ('='*27)

# # задача 5 Вывести цифры числа на каждой строчке
# integer_number = 2129
# while integer_number > 0:
#     # integer_number_dig = integer_number%10
#     # print(integer_number_dig)
#     print(integer_number % 10)
#     integer_number = integer_number//10
# print ('='*27)
# print ('='*27)

# задача 5.1 Вывести цифры числа в обратном порядке
print ('ЗАДАЧА # 5.1 / Вывести цифры числа в обратном порядке')
integer_number = 2129
new_integer_number = ''
while integer_number > 0:
    integer_number_dig = integer_number % 10
    new_integer_number = str(new_integer_number) + str(integer_number_dig)
    integer_number = integer_number // 10
else:
    new_integer_number = int(new_integer_number)
    while new_integer_number > 0:
        print(new_integer_number % 10)
        new_integer_number = new_integer_number // 10
print ('='*27)
print ('='*27)

# задача 6 Найти сумму цифр числа
print ('ЗАДАЧА # 6 / Найти сумму цифр числа')
number = input('введите целое число от 0 и до ....')
# print(number, type(number))
number = int(number)
# print(number, type(number))
sum = 0
while number > 0:
    sum = sum + (number%10)
    number = number//10
print(sum)
print ('='*27)
print ('='*27)

# задача 7 Найти произведение цифр числа
print ('ЗАДАЧА # 7 / Найти произведение цифр числа')
number = input('введите целое число от 0 и до ....')
number = int(number)
mult = 1
while number > 0:
    mult = mult * (number%10)
    number = number//10
print(mult)
print ('='*27)
print ('='*27)

# # задача 8 дать ответ на вопрос: есть ли среди цифр числа 5?
# integer_number = 2347
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')
# print ('='*27)
# print ('='*27)

# задача 9 Найти максимальную цифру в числе
print ('ЗАДАЧА # 9 / Найти максимальную цифру в числе')
number = input('введите целое число от 0 и до ....')
# print(number, type(number))
number = int(number)
max_number = 0
while number > 0:
    loc_number = number%10
    if loc_number > max_number:
        max_number = loc_number
    number = number//10
print(max_number)
print ('='*27)
print ('='*27)

# задача 10 Найти количество цифр 5 в числе
print ('ЗАДАЧА # 10 / Найти количество цифр 5 в числе')
number = input('введите целое число от 0 и до ....')
print(number, type(number))
number = int(number)
# print(new_number, type(new_number))
quant = 0
while number > 0:
    if number % 10 == 5:
        quant +=1
    number = number//10
print(quant)
print ('='*27)
print ('='*27)
