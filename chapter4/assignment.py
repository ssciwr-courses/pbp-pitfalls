# global variable
mylist = [1, 2, 3]


# modify myfunc so that the global variable gets modified
# meaning that mylist should become ["x"] also in the outer
# scope
def myfunc():
    # local variable
    mylist = ["x"]
    # mylist is now shadowed
    print(mylist, "value of global variable in the inner scope")

print(mylist, "value of global variable in outermost scope")

# used for testing, please do not modify
def main():
    myfunc()
    print(mylist, "value of global variable in outer scope")
    return mylist

if __name__ == '__main__':
    main()
