'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #This is normally solved with Boyer–Moore majority vote algorithm -> find majority when m appears more than n/2

        a = {}
        p = 0

        for p in range(len(nums)):
            if nums[p] in a:
                a[nums[p]] += 1
            else:
                 a[nums[p]] = 1
        
        return max(a, key=a.get)