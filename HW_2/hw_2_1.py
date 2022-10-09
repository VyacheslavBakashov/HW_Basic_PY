# Task 1----------------------------------------------------------------
print('Задание 1', '-'*30, end='\n' * 2)
print('Для определения процентной ставки ответьте на следующий вопрос:', end='\n\n')
ERROR = '!!!!!!НЕПРАВИЛЬНЫЙ ВВОД. НАЧНИТЕ ВСЁ СНАЧАЛА!!!!!!'
NO_DISCOUNT = 0

location = input('Вы из Дальнего Востока? (да/нет) ',).lower()
if location == 'нет':
    rate_base = 14.0
    print(f'Базовая ставка по ипотеке: {rate_base} (%)', end='\n\n')
    print('Для рассчета возможных скидок ответьте на следующие вопросы, :')
  
    q_child = int(input('1. Сколько у вас детей? (0,1,2..) '))
    if q_child > 3:
        discount_1 = 1.0
    elif q_child > 0:
        discount_1 = NO_DISCOUNT
    else:
        print(ERROR)
      
    salary = input('2. У вас зарплатная карта нашего банка? (да/нет) ').lower()
    if salary == 'да':
        discount_2 = 0.5
    elif salary == 'нет':
        discount_2 = NO_DISCOUNT
    else:
        print(ERROR)
    
    insurance = input('3. Страхование будет оформлено в нашем банке? (да/нет) ').lower()
    if insurance == 'да':
        discount_3 = 1.5
    elif insurance == 'нет':
        discount_3 = NO_DISCOUNT
    else:
        print(ERROR)
      
elif location == 'да':
    rate_base = 2.0
    discount_1 = NO_DISCOUNT
    discount_2 = NO_DISCOUNT
    discount_3 = NO_DISCOUNT
else:
    print(ERROR)

print()
rate_final = rate_base - discount_1 - discount_2 - discount_3
print(f'Финальная процентная ставка с учетом всех скидок: {rate_final} %', end='\n'*2)

print('Проверка скидок:')
print(f'За количество детей > 3: -{discount_1} %')
print(f'За зарплатный проект:    -{discount_2} %')
print(f'За страховку:            -{discount_3} %')
