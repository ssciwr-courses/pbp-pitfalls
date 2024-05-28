from chapter4 import mutable_default as md


def test_mutable_default():
    # run the ingredients function once
    ingredients = md.ingredients("flour")
    # now call again and make sure it returns only the new ingredient
    ingredients = md.ingredients("sugar")
    assert ingredients == ["sugar"]