#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prev = {}
        for i,x in enumerate(nums):
            if x in prev:
                return True
            prev[x] = i
        return False
        