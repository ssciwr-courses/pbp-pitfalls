from chapter4 import assignment as assign

def test_shadowing():
    mylist = assign.return_mylist()
    assert mylist == ["x"]