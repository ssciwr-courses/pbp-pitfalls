import os
import  unittest.mock as mock
import runpy
from chapter4 import closure

def test_closure():
    test_multiplier = closure.main()
    ref_multiplier = [2, 4, 6, 8, 10]
    assert test_multiplier == ref_multiplier
    