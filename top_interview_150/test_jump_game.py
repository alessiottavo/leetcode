import pytest
from top_interview_150.jump_game import Solution


def can_jump(nums: list[int]) -> bool:
    return Solution().canJump(nums)


def test_example1():
    assert can_jump([2, 3, 1, 1, 4]) is True


def test_example2():
    assert can_jump([3, 2, 1, 0, 4]) is False


def test_single_element():
    assert can_jump([0]) is True


def test_two_elements_reachable():
    assert can_jump([1, 0]) is True


def test_two_elements_unreachable():
    assert can_jump([0, 1]) is False


def test_all_zeros():
    assert can_jump([0, 0, 0]) is False


def test_large_first_jump():
    assert can_jump([10, 0, 0, 0, 1]) is True


def test_just_enough():
    assert can_jump([1, 1, 1, 1]) is True


def test_stuck_at_zero():
    assert can_jump([1, 0, 0, 1]) is False


def test_max_jump_from_middle():
    assert can_jump([1, 0, 5, 0, 0, 0, 1]) is False
