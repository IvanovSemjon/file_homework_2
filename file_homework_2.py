from pprint import pprint


file_path = 'recipes.txt'


def read_cooking_book():
    """Читает текстовый файл и возвращает словарь."""
    cook_book = {}
    ingridients = []
    try:
        with open(file_path, encoding='utf-8') as f_obj: # открываем файл
            contents = f_obj.read().split('\n') # читаем файл и разбиваем его сплитом
            for content in contents: # проходим построчно 
                ingridients.append(content) # создаём спиисок для дальнейшей работы

            for i, c in enumerate(ingridients): # нумеруем список
                if c.isdigit(): # если строка состоит только из чисел берем наменование на строку выше
                    cook_book[contents[i-1]] = []

                    for ingr in ingridients[i+1:i+int(c)+1]: # определяем строки с ингридиентами через сплит и добавляем их
                        if len(ingr.split('|')) == 3:
                            ing = ingr.split('|')[0]
                            qua = int(ingr.split('|')[1])
                            mea = ingr.split('|')[2]

                            cook_book[contents[i-1]].append({
                                                            'ingredient_name':ing,
                                                            'quantity':qua,
                                                            'measure':mea,
                                                            })
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден. Убедитесь что файл на месте и повторите ввод.")
    
    return cook_book


def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    """Функция получает список блюд и количество персон, после чего выдаёт список и количество ингридиентов."""
    dishes_dict = {}
    for key in cooking_book.keys(): # итерируем словарь по ключам
        for dish in dishes: # итерируемся по списку блюд
            if dish == key:
                for dict_ in cooking_book[key]:
                    ing_name = dict_['ingredient_name'] # получаем имя словаря и сохраняем его в перменной 

                    try:
                        dishes_dict[ing_name]['quantity'] += (dict_['quantity'] * person_count) # если уже есть ингридиент то умножаем 
                    except:
                        dishes_dict[ing_name] = {'measure': dict_['measure'],
                                              'quantity': dict_['quantity'] * person_count} # если нет то умножаем и добавляем

    return dishes_dict


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], read_cooking_book(), 2))
