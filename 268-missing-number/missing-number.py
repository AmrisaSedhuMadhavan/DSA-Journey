class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums) + 1
        nums.sort()
        for i in range(n):
            if i not in nums:
                return i


        