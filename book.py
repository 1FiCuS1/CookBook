from pprint import pprint
import os
book_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

def read_bk():
    f_path = os.path.join(os.getcwd(), 'book_book.txt')
    ck_bk = {}
    with open(f_path, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            count = int(f.readline())
            ingredients_list = []
            for _ in range(count):
                ingredient = {}
                ingredient_name, quantity, measure = map(str.strip, f.readline().split('|'))
                ingredient['ingredient_name'] = ingredient_name
                ingredient['quantity'] = int(quantity)
                ingredient['measure'] = measure
                ingredients_list.append(ingredient)
            f.readline()  # Read the empty line
            ck_bk[dish_name] = ingredients_list
    return ck_bk

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}
    for dish_name in dishes:
        if dish_name in ck_bk:
            for ingredient in ck_bk[dish_name]:
                if ingredient['ingredient_name'] not in ingredients_list:
                    ingredients_list[ingredient['ingredient_name']] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    ingredients_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
        else:
            print('Такого блюда нет в книге')
    return ingredients_list

def rewrite_file(path_1=None, path_2=None, path_3=None):
    if path_1 is None or path_2 is None or path_3 is None:
        path_1 = '1.txt'
        path_2 = '2.txt'
        path_3 = '3.txt'
    os.chdir('sorted')
    outoutfile = "rewrite.txt"
    paths = [path_1, path_2, path_3]
    files = []

    for path in paths:
        with open(path, 'r', encoding='utf-8') as f:
            files.append((path, len(f.readlines()), f.readlines()))

    max_file = max(files, key=lambda x: x[1])
    min_file = min(files, key=lambda x: x[1])

    with open(outoutfile, 'w', encoding='utf-8') as f_total, open(min_file[0], 'w', encoding='utf-8') as f_write:
        f_total.write(f"{min_file[0]}\n{min_file[1]}\n")
        f_write.writelines(min_file[2])
        f_total.write('\n')
        for file in files:
            if file != min_file and file != max_file:
                f_total.write(f"{file[0]}\n{file[1]}\n")
                f_total.writelines(file[2])
                f_total.write('\n')
        f_total.write(f"{max_file[0]}\n{max_file[1]}\n")
        f_total.writelines(max_file[2])
        f_total.write('\n')

if __name__ == '__main__':
    filename = 'book_book.txt'
    ck_bk = read_bk()
    print('Задача № 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    pprint(ck_bk)
    print('Задача № 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    pprint(get_shop_list_by_dishes(['Омлет'], 2))
    print('Задача № 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    rewrite_file()
