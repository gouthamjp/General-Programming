# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l,r = 0,(len(s)-1)
        
        while(l < (len(s))//2):
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
            
        