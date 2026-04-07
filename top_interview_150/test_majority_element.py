import pytest
from top_interview_150.majority_element import Solution


def majority(nums: list[int]) -> int:
    return Solution().majorityElement(nums)


def test_example1():
    assert majority([3, 2, 3]) == 3


def test_example2():
    assert majority([2, 2, 1, 1, 1, 2, 2]) == 2


def test_single_element():
    assert majority([1]) == 1


def test_all_same():
    assert majority([5, 5, 5]) == 5


def test_two_elements():
    assert majority([1, 1, 2]) == 1


def test_large_majority():
    assert majority([4, 4, 4, 4, 1, 2, 3]) == 4


def test_majority_at_end():
    assert majority([1, 2, 3, 3, 3]) == 3
