# Task 2----------------------------------------------------------------
print('Задание 2: Определение знака зодиака по дате рождения.', end='\n' * 2)

ERROR = '!!!!!НЕПРАВИЛЬНЫЙ ВВОД. НАЧНИТЕ СНАЧАЛА!!!!!'
list_m = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

print('Введите дату своего рождения:')
month = input('  Месяц (словом) - ').strip().lower()[:3]
if month in list_m:
    month = list_m.index(month) + 1
else:
    print(ERROR)
date = int(input('  Число - '))

if  (month == 12 and 22 <= date <= 31) or (month == 1 and 1 <= date <= 20):
    znak = 'Козерог'
if (month == 1 and 21 <= date <= 31) or (month == 2 and 1 <= date <= 19):
    znak = 'Водолей'
if (month == 2 and 20 <= date <= 29) or (month == 3 and 1 <= date <= 20):
    znak = 'Рыбы'  
if (month == 3 and 21 <= date <= 31) or (month == 4 and 1 <= date <= 20):
    znak = 'Овен'
if (month == 4 and 21 <= date <= 30) or (month == 5 and 1 <= date <= 20):
    znak = 'Телец'
if (month == 5 and 21 <= date <= 31) or (month == 6 and 1 <= date <= 21):
    znak = 'Близнецы'
if (month == 6 and 22 <= date <= 30) or (month == 7 and 1 <= date <= 22):
    znak = 'Рак'
if (month == 7 and 23 <= date <= 31) or (month == 8 and 1 <= date <= 23):
    znak = 'Лев'
if (month == 8 and 24 <= date <= 31) or (month == 9 and 1 <= date <= 23):
    znak = 'Дева'
if (month == 9 and 24 <= date <= 30) or (month == 10 and 1 <= date <= 23):
    znak = 'Весы'
if (month == 10 and 24 <= date <= 31) or (month == 11 and 1 <= date <= 22):
    znak = 'Скорпион'
if (month == 11 and 23 <= date <= 30) or (month == 12 and 1 <= date <= 21):
    znak = 'Стрелец'
print('Ваш знак зодиака:', znak, end='\n'*3)


# Task 4----------------------------------------------------------------
print('Задание 4: Ссылка на аккаунт:', end='\n' * 2)
print('https://www.hackerrank.com/vvbakashov')