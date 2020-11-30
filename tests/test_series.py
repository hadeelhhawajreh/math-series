from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import other
from math_series.series import sum_series
def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert expected == actual


def test_one():
    actual = fibonacci(1)
    expected = 1
    assert expected == actual


def test_num():
    actual = fibonacci(5)
    expected = 5
    assert expected == actual


def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert expected == actual


def test_one_lucas():
    actual = lucas(1)
    expected = 1
    assert expected == actual


def test_num_lucas():
    actual = lucas(5)
    expected = 11
    assert expected == actual

def test_other():
    actual=other(5,2,2)
    expected=16
    assert expected == actual


def test_sum_series():
    actual=sum_series(5)
    expected=5
    assert expected == actual


def test_sum_series2():
    actual=sum_series(5,2,1)
    expected=11
    assert expected == actual


def test_sum_series3():
    actual=sum_series(5,2,2)
    expected=16
    assert expected == actual

    