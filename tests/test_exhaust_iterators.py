from chapter4 import exhaust_iterators as ei

def test_exhaust_iterators():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    lunch = ["Pizza", "Salad", "Pasta", "Sushi", "Sandwich"]
    menu_ref = list(zip(days, lunch))
    menu_test = ei.exhaust_my_iterators(days, lunch)
    assert menu_test == menu_ref