
dish = None
amount_ingredients = None

# load_cook_book = {}
finish_cook_book = {}
# ingredients = []
with open('Dishes.txt', encoding = 'utf-8') as CookBook:
    for line_dish in CookBook:
        ingredients = []
        # dish = line_dish.strip()
        # print(dish)
        amount_ingredients = int(CookBook.readline())
        i = 0
        while i < amount_ingredients:
            load_cook_book = {}
            line_ingredient = CookBook.readline().split('|')
            for k,line, in enumerate(line_ingredient):
                # print(type(k))
                if k == 0:
                    load_cook_book.update({'ingridient_name' : line.strip()})
                    # print(line, " k = 0", load_cook_book)
                if k == 1:
                    load_cook_book.update({'quantity' : int(line.strip())})
                    # print(line, " k = 1",load_cook_book)
                if k == 2:
                    load_cook_book.update({'measure' : line.strip()})
                    # print(line, " k = 2", load_cook_book)
                    ingredients.append(load_cook_book)
                    finish_cook_book.update({line_dish.strip() : ingredients})
                    # print("как заполняется словарь, который пойдет в список", load_cook_book)
                    # print("список словарей ингредиентов здесь пишется ", ingredients)
            i += 1

        CookBook.readline()
        # print("Название блюда {},кол-во ингредиентов {}, название блюда {}".format(dish, amount_ingredients, line_ingredient))

# print(finish_cook_book)
for dish_for_print in finish_cook_book:
    print(dish_for_print,finish_cook_book[dish_for_print])




# print(ingredients)