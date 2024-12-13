from chapter4 import assignment as assign

def test_shadowing():
    mylist = assign.main()
    assert mylist == ["x"]