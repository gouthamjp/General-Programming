#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for x in nums :
            x = chr(x)
        count = 0   
        l = 0
        r = l+1
        
        while(r < len(nums)):
            if(nums[l] == nums[r]):
                nums[r] = '_'
                r += 1
            else:
                l = r
                r = l+1

        for x in nums:
            if(isinstance(x, int) != True):
                nums.remove(x)
        
        print(nums)

# The main logic of this program is complete , yet there is an issue with sorting the final
# result , do send in a pull request if you get a solution
        