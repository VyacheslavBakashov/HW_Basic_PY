# Task 1----------------------------------------------------------------
print('Задание 1: Dating service.', end='\n' * 2)

# # Ввод списков, вариант 1 (имена через пробел вводит пользователь)
# boys = input('Список парней: ').split()  # Peter Alex John Arthur Richard (for copy/past)
# girls = input('Список девушек: ').split()  # Kate Liza Kira Emma Trisha (for copy/past)
# print()

# Ввод списков, вариант 2 (списки уже заданы)
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
print('Список парней:', *boys, sep='\n', end='\n'*2)
print('Список девушек:', *girls, sep='\n', end='\n'*2)

# Составление пар
dif = len(boys)- len(girls)
if dif == 0:
    boys.sort(), girls.sort()
    couples = [(f'{boy.capitalize()} и {girl.capitalize()}') for boy, girl in zip(boys, girls)]
    print('Идеальные пары:', *couples, sep='\n')  
elif dif > 0:
    print(f'Предупреждение! Кто-то из парней останется без пары! Пригласите девушек: {dif} ')
else:
    print(f'Предупреждение! Кто-то из девушек останется без пары! Пригласите парней: {abs(dif)} ')

############################################ нашел как записать короче
# print('Список парней:') 
# for boy in boys:
#     print(boy)
  
# print('Список девушек:') 
# for girl in girls:
#     print(girl)

# print('Идеальные пары:')
# for boy, girl in zip(boys, girls):
#     print(f'{boy.capitalize()} и {girl.capitalize()}') 
  
  ###########################################


  




    
  
  

        
    
    
    
    

