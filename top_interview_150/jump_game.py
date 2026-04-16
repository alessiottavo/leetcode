'''You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.'''


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        r = 0 #maximum index reacheable
        for p in range(len(nums)):
            if(p > r):
                return False
            #from p, where can i reach?
            r = max(r, nums[p] + p)
            if r >= len(nums) - 1:
                return True
        return False