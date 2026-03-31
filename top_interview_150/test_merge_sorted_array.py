import pytest
from top_interview_150.merge_sorted_array import Solution


@pytest.fixture
def s():
    return Solution()


def test_basic(s):
    nums1 = [1, 2, 3, 0, 0, 0]
    s.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_empty_nums2(s):
    nums1 = [1]
    s.merge(nums1, 1, [], 0)
    assert nums1 == [1]


def test_empty_nums1(s):
    nums1 = [0]
    s.merge(nums1, 0, [1], 1)
    assert nums1 == [1]


def test_nums2_all_smaller(s):
    nums1 = [4, 5, 6, 0, 0, 0]
    s.merge(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]
