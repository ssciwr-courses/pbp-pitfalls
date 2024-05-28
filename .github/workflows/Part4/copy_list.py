import copy


# change the function "lists1" so that it returns two different lists
# where the first returned list is equal to mylist and the second is 
# mylist with an appended 4
def lists1(mylist):
    mylist2 = mylist.copy()
    print(mylist)
    print(mylist2)
    mylist2.append(4)
    print(mylist)
    print(mylist2)
    # both lists now have 4 appended 
    # notice that both point to the same physical address
    print(id(mylist))
    print(id(mylist2))
    mylist = [1,2,3]
    return mylist, mylist2

# shallow copy
def shallow_copy(mylist):
    mylist3 = mylist.copy()
    print(mylist3)
    mylist3.append("x")
    print(mylist)
    print(mylist3)
    mylist3[3] = "r"
    print(mylist)
    print(mylist3)

# why is it a shallow list? Consider nesting:
def deep_copy(deeplist):
    deeplist2 = deeplist.copy()
    deeplist[2][0] = "x"
    print(deeplist)
    print(deeplist2)
    # notice that at the nested level both lists have changed
    # this is because they are referencing the same physical addresses for the list items:
    for item, item2 in zip(deeplist, deeplist2):
        print(id(item))
        print(id(item2))

    # for this you need a deep copy:
    deeplist3 = copy.deepcopy(deeplist)
    deeplist[2][1] = "y"
    print(deeplist)
    print(deeplist3)
    for item, item2 in zip(deeplist, deeplist3):
        print(id(item))
        print(id(item2))

if __name__ == "__main__":
    input_list = [1, 2, 3]
    list_tuple = lists1(input_list)
    # shallow_copy(input_list)
    # deep_list = ["a", "b", [0, 1]]
    # deep_copy(deep_list)