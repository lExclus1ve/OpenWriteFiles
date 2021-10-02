from pprint import pprint
import os


with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}

    for line in file:
        cook = line.strip()
        count = int(file.readline())

        list_ingridients = []
        for item in range(count):
            ingredient_name, quantity, measure = file.readline().split('|')
            list_ingridients.append({'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()})

        cook_book[cook] = list_ingridients
        file.readline()

    # pprint(cook_book)


    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for key, val in cook_book.items():
            for item in val:
                if key in dishes:
                    if item['ingredient_name'] not in shop_list:
                        shop_list[item['ingredient_name']] = {'measure': item['measure'], 'quantity': item['quantity'] * person_count}
                    else:
                        shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count
        return shop_list

    # pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))




# path = f'{os.getcwd()}/documents'
# file_list = []
#
# with open('final.txt', 'w', encoding='utf-8') as write_file:
#
#     for file_name in os.listdir(path):
#         path = f'{os.getcwd()}/documents/{file_name}'
#         # print(path)
#
#         with open(path, encoding='utf-8') as file:
#             length = len(file.readlines())
#
#         with open(path, encoding='utf-8') as file:
#             text = file.readlines()
#             file_list.append({'name': file_name, 'length':length, 'text':text})
#
#     file_list.sort(key=lambda dictionary: dictionary['length'])
#
#     for i in file_list:
#         write_file.write(f'{i["name"]}\n{i["length"]}\n')
#         for text_files in i['text']:
#             print(text_files)
#             write_file.write(f'{text_files.strip()}\n')






with open('final.txt', 'w', encoding='utf-8') as write_file:

    path = f'{os.getcwd()}/documents'
    file_list = []

    for file_name in os.listdir(path):
        path = f'{os.getcwd()}/documents/{file_name}'
        # print(path)

        with open(path, encoding='utf-8') as file:
            length = len(file.readlines())

        with open(path, encoding='utf-8') as file:
            text = file.readlines()
            file_list.append({'name': file_name, 'length':length, 'text':text})

    file_list.sort(key=lambda dictionary: dictionary['length'])

    for i in file_list:
        write_file.write(f'{i["name"]}\n{i["length"]}\n')
        for text_files in i['text']:
            print(text_files)
            write_file.write(f'{text_files.strip()}\n')
