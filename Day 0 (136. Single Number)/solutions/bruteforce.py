class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums = sorted(nums)
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]
        return nums[-1]
    
print(Solution.singleNumber(Solution, [4,1,2,1,2]))        