from chapter4 import copy_list as cl


def test_lists1():
    input_list = [1, 2, 3]
    two_lists = cl.lists1(input_list)
    assert two_lists[0] ==  [1, 2, 3]
    assert two_lists[1] ==  [1, 2, 3, 4]
