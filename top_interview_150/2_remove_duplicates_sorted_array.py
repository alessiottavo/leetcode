""" Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory. """

from typing import List


class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        if len(a) <= 2:
            return len(a)
        k = 2
        for p in range (2, len(a)):
            if a[p] == a[k - 2]:
                continue
            else:
                a[k] = a[p]
                k += 1
        return k


def judge(nums, expected):
    k = Solution().removeDuplicates(nums)
    assert k == len(expected)
    assert nums[:k] == expected


def test_example1():
    judge([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3])


def test_example2():
    judge([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3])


def test_empty():
    judge([], [])


def test_single_element():
    judge([1], [1])


def test_two_elements():
    judge([1, 1], [1, 1])


def test_no_duplicates():
    judge([1, 2, 3, 4], [1, 2, 3, 4])


def test_all_same():
    judge([5, 5, 5, 5, 5], [5, 5])


def test_two_groups_over_twice():
    judge([1, 1, 1, 2, 2, 2], [1, 1, 2, 2])


def test_negatives():
    judge([-3, -3, -3, -1, 0, 0, 0, 1], [-3, -3, -1, 0, 0, 1])
