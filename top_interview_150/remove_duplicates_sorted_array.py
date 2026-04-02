""" Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored. """

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        f = 1
        for p in range(1, len(nums)):
            if nums[p] == nums[f-1]:
                continue
            else:
                nums[f] = nums[p]
                f += 1
        return f


def judge(nums, expected_nums):
    k = Solution().removeDuplicates(nums)
    assert k == len(expected_nums)
    assert nums[:k] == expected_nums


def test_example1():
    judge([1, 1, 2], [1, 2])


def test_example2():
    judge([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])


def test_empty_array():
    judge([], [])


def test_single_element():
    judge([1], [1])


def test_no_duplicates():
    judge([1, 2, 3, 4], [1, 2, 3, 4])


def test_all_duplicates():
    judge([7, 7, 7, 7], [7])


def test_two_distinct():
    judge([1, 1, 2, 2], [1, 2])


def test_negatives():
    judge([-3, -3, -1, 0, 0, 1], [-3, -1, 0, 1])
