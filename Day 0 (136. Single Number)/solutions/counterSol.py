from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        numsCounter = Counter(nums)
        for num in numsCounter:
            if numsCounter[num] == 1:
                return num
            