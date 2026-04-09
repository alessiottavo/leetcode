class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) #APPARENTLY rotating by k is identical to rotating by k % n
        if k == 0:
            return
        n = len(nums) - 1
        #invert the array, thenk ivert the first k, the the len - k elements
        for p in range(0, len(nums)//2):
            nums[n], nums[p] = nums[p], nums[n]
            n -= 1  
        n = k - 1
        #inverted, invert the first k elements, then invert the rest
        for p in range(0, k//2):
            nums[n], nums[p] = nums[p], nums[n]
            n -= 1
        n = len(nums) - 1
        for p in range(k,k + (len(nums) - k)//2):
            nums[n], nums[p] = nums[p], nums[n]
            n -= 1

