# Task 1----------------------------------------------------------------
print('Задание 1', end='\n' * 2)

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
commands = {
    'p': 'people - выводит имя человека по номеру документа',
    's': 'shelf - выводит номер полки по номеру документа',
    'l': 'list - выводит список всех доступных документов',
    'a': 'add - добавляет новый документ в каталог и в перечень полок',
    'd': 'delete - удаляет документ по номеру',
    'm': 'move - перемещает документ по номеру и целевой полки',
    'as': 'add shelf - добавляет полку по номеру',
    'q': 'quit - выход из программы'
}

print('Список доступных команд:')
for command_, description in commands.items():
    print(f'{command_} - {description}')
print()


def make_note(key):  # notes
    note = None
    if key in 'type':
        note = 'Введите тип документа: \n'
    elif key in 'number':
        note = 'Введите номер документа: \n'
    elif key in 'name':
        note = 'Введите имя владельца: \n'
    elif key in 'shelf_number':
        note = 'Введите номер полки: \n'
    return note


def check_docnum(docs, shelves, command):  # Проверка номера документа
    docnum_list_1 = [item.get('number') for item in docs]
    docnum_list_2 = [v_1 for v in shelves.values() for v_1 in v]
    docnum = input(f'{make_note("number")}').strip()
    if docnum not in set(docnum_list_1 + docnum_list_2):
        return print('Команда прервана. Такого документа нет в каталоге и на полках', end=2 * '\n')
    elif docnum not in docnum_list_1 and command in ['p']:
        return print('Этот документ есть на полке, но данные не занесены в каталог! \n')
    return docnum


def check_shelf(docs, shelves, command, docnum=None):  # Проверка полок
    shelf_keys = list(shelves.keys())
    shelves_a, shelf_cur = [], ''
    if docnum:
        shelf_cur = get_shelfnum(docs, shelves, command, docnum)
        shelves_a = list(shelves.keys())
        shelves_a.remove(shelf_cur)
    while True:
        shelf_num = input(f'{make_note("shelf_number")}').strip()
        if not shelf_num.isdigit() or int(shelf_num) <= 0:
            print('Внимание! Введите число > 0!')
        elif shelf_num not in shelf_keys:
            if command in ['a']:
                print(f'Такой полки пока нет. Выберите из существующих: {shelf_keys}')
            elif command == 'as':
                return shelf_num
            elif command == 'm':
                print(f'Такой полки пока нет. Выберите из доступных: {shelves_a}')
        else:
            if command in ['a']:
                return shelf_num
            elif command == 'as':
                print(' Такая полка уже есть.', f' Сейчас в каталоге {list(shelves.keys())}', sep='\n')
            elif command == 'm':
                if shelf_num != shelf_cur:
                    return shelf_num, shelf_cur
                print(f'Документ уже на этой полке, выберете из {shelves_a}')


def get_listdocs(docs):  # Функция для list
    return [f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"' for doc in docs]


def get_name(docs, shelves, command):  # Функция для people
    docnum = check_docnum(docs, shelves, command)
    return ''.join([doc.get('name') for doc in docs if docnum == doc.get('number')])


def get_shelfnum(docs, shelves, command, docnum=None):  # Функция для shelf
    if not docnum:
        docnum = check_docnum(docs, shelves, command)
    return ''.join([k for k, v in shelves.items() if docnum in v])


def add_doc(docs, shelves, command):  # Функция для add
    doc_keys = list(docs[0].keys())  # доб-ние в documents; doc_keys = ['type', 'number', 'name']
    doc_values = [input(f'{make_note(key)}').strip() for key in doc_keys]
    doc_new = dict(zip(doc_keys, doc_values))
    docs.append(doc_new)
    shelf_num = check_shelf(docs, shelves, command)  # добавление в directories
    shelves.get(shelf_num).append(doc_new.get('number'))
    return docs, shelves


def add_shelf(docs, shelves, command):  # Функция для as
    shelf_num = check_shelf(docs, shelves, command)
    shelves.setdefault(shelf_num, [])
    return shelf_num, shelves


def del_doc(docs, shelves, command):  # Функция для delete doc
    docnum = check_docnum(docs, shelves, command)
    for key, item in list(shelves.items()):  # Удаление с полки
        if docnum in item:
            shelves[key].remove(docnum)
            break
    for doc in list(docs):  # Удаление из списка документов
        if docnum == doc.get('number'):
            docs.remove(doc)
            break
    return docs, shelves


def move_doc(docs, shelves, command):  # Функция для move
    docnum = check_docnum(docs, shelves, command)
    if not docnum:
        return
    shelf_num, shelf_cur = check_shelf(docs, shelves, command, docnum)
    shelves[shelf_cur].remove(docnum)
    shelves[shelf_num].append(docnum)
    return shelves


def main(docs, shelves, commands_):  # Ф-ия вызова команды
    while True:
        command = input('Введите команду: ').lower().strip()
        if command not in commands_.keys():
            print('!!!Такая команда недоступна, введите заново!!! \n')
        elif command == 'l':
            print(*get_listdocs(docs), sep='\n', end=2 * '\n')
        elif command == 'p':
            print(get_name(docs, shelves, command), end='\n' * 2)
        elif command == 's':
            print(get_shelfnum(docs, shelves, command), end='\n' * 2)
        elif command == 'a':
            add_doc(docs, shelves, command)
            print('Документ внесён.', *docs, *list(shelves.items()), sep='\n', end=2 * '\n')
        elif command == 'as':
            shelf_new, shelves = add_shelf(docs, shelves, command)
            print('Полка добавлена. Проверьте:', *list(shelves.items()), sep='\n', end=2 * '\n')
        elif command == 'd':
            docs, shelves = del_doc(docs, shelves, command)
            print('Список доступных документов:', *docs, sep='\n', end=2 * '\n')
            print('Список доступных документов на полках:', *shelves.values(), sep='\n', end=2 * '\n')
        elif command == 'm':
            move_doc(docs, shelves, command)
            print('Список доступных документов на полках:', *shelves.items(), sep='\n', end=2 * '\n')
        elif command == 'q':
            print('Выход')
            break


main(documents, directories, commands)
