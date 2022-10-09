# Task 1----------------------------------------------------------------
print('Задание 1', end='\n' * 2)

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
country = 'Россия'
for i, trip in enumerate(geo_logs[:]):
    if country not in trip['visit' + str(i + 1)]:
        geo_logs.remove(trip)
      
print(*geo_logs, sep='\n', end='\n' * 3)


# Task 2----------------------------------------------------------------
print('Задание 2', end='\n' * 2)

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
unic = set()
for v in ids.values():
    unic.update(v)
print(list(unic), end='\n' * 3)

# Task 3----------------------------------------------------------------
print('Задание 3', end='\n' * 2)

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'какая обстановка в мире',
    'рефераты по истории России',
    'как приготовить суп',
    'как выбрать видеокарту'
]

querie_num = len(queries)
words_num = []

for querie in queries:
    words_num.append(len(querie.split()))
letter = ['запроса' if i < 5 else 'запросов' for i in range(querie_num)]

print(f'Общее количество поисковых запросов {querie_num}, из них:')
for i in range(1, max(words_num) + 1):
    perc = words_num.count(i) / querie_num * 100
    if perc != 0:
        print(f'  {words_num.count(i)} {letter[words_num.count(i)]} состоящих из {i} слов - {perc:.2f} %')
print(end=2*'\n')


# Task 4----------------------------------------------------------------
print('Задание 4', end='\n' * 2)

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98, 'sber': 120}

# решение 1, м.б. не совсем верное, в случае одинаковых стат данных, что-нибудь удалит
stats_1 = {v: k for k, v in stats.items()}
key = max(stats_1)
print(stats_1[key])  # лишились яндекса

# решение 2, выводит одну из компаний
print(max(stats, key=stats.get))

# решение 3, при наличии одинаковых стат данных выводит список
stats_2 = [k for k, v in stats.items() if v == max(stats.values())]
print(*stats_2, sep=', ', end=3*'\n')


# Task 5----------------------------------------------------------------
print('Задание 5', end='\n' * 2)

my_list = ['2018-01-01', 'yandex', 'cpc', 100]
my_list.reverse()
first = my_list[0]
for item in my_list[1:]:
    first = {item: first}
print(first)
