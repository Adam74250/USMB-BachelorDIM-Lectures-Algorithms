""" Basic introduction to unit testing with Python

@brief get started with python testing by looking at https://docs.pytest.org/en/latest/getting-started.html#getstarted. Note that any script to be ran within the python testing framework (pytest) should follow the standard test discovery rules (https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
"""

import S1_algotools as algo

def test_True():
    """ one of the simplest test that does nothing..."""
    assert True

def test_bubble_sort():
    if algo.bubble_sort([0, 5, 2, 3, 1, 4]) == [0, 1, 2, 3, 4, 5]:
        assert True
    else
        assert False
