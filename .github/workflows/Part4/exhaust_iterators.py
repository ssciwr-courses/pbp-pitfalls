
def exhaust_my_iterators(days, lunch):
    menu = list(zip(days, lunch))
    print(menu)
    full_menu = []
    for item in menu:
        print("On {} we offer {} for lunch.".format(item[0], item[1]))
        full_menu.append((item[0], item[1]))
    return full_menu

if __name__ == "__main__":
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    lunch = ["Pizza", "Salad", "Pasta", "Sushi", "Sandwich"]
    menu = exhaust_my_iterators(days, lunch)
    print(menu)

