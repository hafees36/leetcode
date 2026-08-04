class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            nums.sort()
            if nums[i]!=i:
                return i
        return len(nums)
        