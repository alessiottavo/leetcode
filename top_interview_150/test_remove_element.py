import pytest
from top_interview_150.remove_element import Solution


def judge(nums, val, expected_nums):
    k = Solution().removeElement(nums, val)
    assert k == len(expected_nums)
    assert sorted(nums[:k]) == sorted(expected_nums)


def test_example1():
    judge([3, 2, 2, 3], 3, [2, 2])


def test_example2():
    judge([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4])


def test_empty_array():
    judge([], 1, [])


def test_all_elements_removed():
    judge([7, 7, 7], 7, [])


def test_no_elements_removed():
    judge([1, 2, 3], 9, [1, 2, 3])


def test_single_element_removed():
    judge([1], 1, [])


def test_single_element_kept():
    judge([1], 2, [1])


def test_val_not_present():
    judge([1, 2, 3, 4], 5, [1, 2, 3, 4])


def test_all_same_kept():
    judge([3, 3, 3], 5, [3, 3, 3])


def test_mixed():
    judge([0, 0, 1, 2, 0], 0, [1, 2])
