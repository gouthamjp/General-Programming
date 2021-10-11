# https://leetcode.com/problems/two-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i,x in enumerate(nums):
            b = target - x
            if  b in prev:
                return [prev[b],i]
            prev[x] = i