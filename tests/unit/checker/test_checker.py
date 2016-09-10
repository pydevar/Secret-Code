from src.checker.checker import Checker


def test_check_red():
    # Check all wrong
    assert Checker([1, 2, 3, 4]).check_red([0, 0, 0, 0]) == 0

    # Check 1 for all
    assert Checker([1, 2, 3, 4]).check_red([1, 0, 0, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_red([0, 1, 0, 0]) == 0
    assert Checker([1, 2, 3, 4]).check_red([0, 0, 1, 0]) == 0
    assert Checker([1, 2, 3, 4]).check_red([0, 0, 0, 1]) == 0

    # Check 1 good for all
    assert Checker([1, 2, 3, 4]).check_red([1, 0, 0, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_red([0, 2, 0, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_red([0, 0, 3, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_red([0, 0, 0, 4]) == 1

    assert Checker([1, 2, 3, 4]).check_red([1, 2, 0, 0]) == 2
    assert Checker([1, 2, 3, 4]).check_red([1, 0, 3, 0]) == 2
    assert Checker([1, 2, 3, 4]).check_red([1, 0, 0, 4]) == 2
    assert Checker([1, 2, 3, 4]).check_red([0, 2, 3, 4]) == 3
    assert Checker([1, 2, 3, 4]).check_red([4, 3, 2, 1]) == 0


def test_check_yellow():
    # Check all wrong
    assert Checker([1, 2, 3, 4]).check_yellow([0, 0, 0, 0]) == 0

    # Check 1 for all
    assert Checker([1, 2, 3, 4]).check_yellow([1, 0, 0, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_yellow([0, 1, 0, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_yellow([0, 0, 1, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_yellow([0, 0, 0, 1]) == 1

    # Check 1 good for all
    assert Checker([1, 2, 3, 4]).check_yellow([1, 0, 0, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_yellow([0, 2, 0, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_yellow([0, 0, 3, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_yellow([0, 0, 0, 4]) == 1

    # Other checks
    assert Checker([1, 2, 3, 4]).check_yellow([1, 2, 0, 0]) == 2
    assert Checker([1, 2, 3, 4]).check_yellow([1, 0, 3, 0]) == 2
    assert Checker([1, 2, 3, 4]).check_yellow([1, 0, 0, 4]) == 2
    assert Checker([1, 2, 3, 4]).check_yellow([0, 2, 3, 4]) == 3

    # All good
    assert Checker([1, 2, 3, 4]).check_yellow([4, 3, 2, 1]) == 4

    # Other cases
    assert Checker([1, 2, 3, 4]).check_yellow([0, 1, 1, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_yellow([0, 2, 2, 0]) == 1
    assert Checker([1, 2, 3, 4]).check_yellow([0, 1, 3, 4]) == 3
    assert Checker([1, 2, 3, 4]).check_yellow([2, 1, 1, 4]) == 3

def test