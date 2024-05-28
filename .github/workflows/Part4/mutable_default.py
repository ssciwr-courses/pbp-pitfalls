import time
from datetime import datetime

# rewrite the function "ingredients" to use a mutable default argument
def ingredients(ingredient, all_ingredients=None):
    if all_ingredients is None:
        all_ingredients = []
    all_ingredients.append(ingredient)
    return all_ingredients


def display_time(time_to_print=datetime.now()):
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))


def myfunc(a={"b": 0}):
    a["b"] += 5
    print(a)


if __name__=="__main__":
    # method 1
    # a list is mutable
    # print(ingredients.__defaults__)
    all_ingredients = ingredients("flour")
    print(all_ingredients)
    # print(ingredients.__defaults__)
    all_ingredients = ingredients("sugar")
    print(all_ingredients)
    # print(ingredients.__defaults__)
    all_ingredients = ingredients("butter")
    print(all_ingredients)
    # myfunc()
    # display_time()
    # default argument only evaluated once
    # print(display_time.__defaults__)
    # time.sleep(1)
    # display_time()






