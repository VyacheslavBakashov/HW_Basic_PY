from pprint import pprint

file_name_ = 'recipes.txt'


def cookbook_reader(file_name: str) -> dict:
    with open(file_name, encoding='utf-8') as file:
        cook_book = {}
        items = ['ingredient_name', 'quantity', 'measure']
        for line in file:
            dish_name = line.strip()
            ingredients = []
            i_quantity = file.readline()
            for _ in range(int(i_quantity)):
                ingredient_list = [int(i) if i.isdigit() else i for i in file.readline().strip().split(' | ')]
                ingredient = dict(zip(items, ingredient_list))
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book


catalog = cookbook_reader(file_name_)
pprint(catalog, width=120)
print()


def get_shop_list(dishes, person_count):
    cook_book = cookbook_reader(file_name_)
    q, name = 'quantity', 'ingredient_name'
    res = {}
    for dish in dishes:
        if dish not in cook_book:
            return f'!!!Проверьте вводимые блюда\nВыберете из {*list(cook_book),}'
        for ingredient in cook_book[dish]:
            ingredient[q] *= person_count
            a = ingredient.copy()
            item = a.pop(name)
            if not res.get(item):
                res[item] = a
            else:
                res[item][q] += a[q]
    return res


shop_list = get_shop_list(['Пицца', 'Фахитос'], 3)
pprint(shop_list)

# shop_list_1 = get_shop_list(['Пицца', 'Пицца', 'Пицца'], 1)
# pprint(shop_list_1)
