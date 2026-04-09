import pytest
from top_interview_150.rotate_array import Solution


def rotate(nums: list[int], k: int) -> list[int]:
    Solution().rotate(nums, k)
    return nums


def test_example1():
    assert rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]


def test_example2():
    assert rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]


def test_k_zero():
    assert rotate([1, 2, 3], 0) == [1, 2, 3]


def test_k_equals_length():
    assert rotate([1, 2, 3], 3) == [1, 2, 3]


def test_k_greater_than_length():
    assert rotate([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]


def test_single_element():
    assert rotate([1], 1) == [1]


def test_two_elements():
    assert rotate([1, 2], 1) == [2, 1]
