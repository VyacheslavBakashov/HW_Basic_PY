# Task 1----------------------------------------------------------------
print('Задание 1', end='\n' * 2)

print('Введите длину стороны квадрата: ', end='')
square_side = int(input())
perimeter_sq = 4 * int(square_side)

print(f'Периметр: {perimeter_sq}')
print(f'Площадь: {int(square_side)**2}')
print()

rectungle_length = int(input('Введите длину прямоугольника: '))
rectungle_width = int(input('Введите ширину прямоугольника: '))
area_rect = rectungle_length * rectungle_width

print(f'Периметр: {2 * (rectungle_length + rectungle_width)}')
print('Площадь: ', area_rect)
print('\n' * 2)


# Task 2----------------------------------------------------------------
print('Задание 2', end='\n' * 2)

salary = int(input('Введите заработную плату: '))
mortage_percent = int(input('Введите, какой процент(%) уходит на ипотеку: ')) / 100
live_percent = int(input('Введите, какой процент(%) уходит на жизнь: ')) / 100
print()

num_month = 12
val_mortage = salary * mortage_percent * num_month
val_savings = salary * (1 - live_percent - mortage_percent) * num_month

print(f'На ипотеку было потрачено: {round(val_mortage)} рублей')
print(f'Было накоплено: {round(val_savings)} рублей')
print('\n' * 2)


# Task 3----------------------------------------------------------------
print('Задание 3', end='\n' * 2)

symbol = input('Введите символ разделителя: ')
quantity = perimeter_sq + area_rect

print(symbol * quantity)
print('\n' * 2)


# Task 4----------------------------------------------------------------
print('Задание 4', end='\n' * 2)
print('https://www.hackerrank.com/vvbakashov')