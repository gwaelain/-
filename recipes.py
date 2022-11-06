from pprint import pprint

cookbook = {}
list = ['ingredient_name', 'quantity', 'measure']
with open('recipes.txt', encoding='UTF-8') as file:
    for line in file:
        name = line.strip()
        ingredient_count = int(file.readline().strip())
        list2 = []
        for i in range(ingredient_count):
            line = file.readline().strip().split(' | ')
            couples = dict(zip(list, line))
            list2.append(couples)
        file.readline()
        cookbook[name] = list2
pprint(cookbook)

dishes = ['Омлет', 'Утка по-пекински', 'Запеченный картофель', 'Фахитос']
def get_shop_list_by_dishes(dishes, person_count):
    new_dict = {}
    for i in dishes:
        for j in cookbook[i]:
            if j['ingredient_name'] in new_dict:
                new_dict[j['ingredient_name']]['quantity'] += int(j['quantity']) * person_count
            else:
                new_dict[j['ingredient_name']] = {
                    'measure': j['measure'],
                    'quantity': int(j['quantity']) * person_count
            }
    pprint(new_dict)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)



file_name = 'recipes.txt'


def cooking(file_name: str) -> dict:
    with open(file_name, encoding='utf-8') as file_obj:
        main_name = ['ingredient_name', 'quantity', 'measure']
        result = {}
        for line in file_obj:
             dish = line.strip()
             foods = []
             amount_ingredients = file_obj.readline()
             for item in range(int(amount_ingredients)):
                 food_primary = file_obj.readline()
                 food = food_primary.split(" | ")
                 ingredient = dict(zip(main_name, food))
                 foods.append(ingredient)
             result[dish] = foods
             file_obj.readline()

        return result


cook_book = cooking(file_name)


def get_shop_list_by_dishes(dishes, person_count):
    order_dishes = []
    list_of_dishes = []
    for dish in cook_book:
        list_of_dishes.append(dish)


    for check in list_of_dishes:
        number = 0
        count = dishes.count(check)
        number = +1
        if count > 0:
             add = {check : count}
             order_dishes.append(add)


    list_ingrediends = []
    for dish in order_dishes:
        for dish_1, amount in dish.items():
            for current_dish in cook_book:
                if current_dish == dish_1:
                     for ingredient in cook_book[current_dish]:
                         ingredients_on_dish = {ingredient['ingredient_name']:{'measure' : ingredient['measure'],
                         'quantity' : int(ingredient['quantity'])* int(amount) *person_count}}
                         list_ingrediends.append(ingredients_on_dish)
    pprint(list_ingrediends)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Омлет'], 2)
get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель', 'Запеченный картофель', 'Омлет'], 2)