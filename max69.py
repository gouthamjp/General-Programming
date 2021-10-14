#https://leetcode.com/problems/maximum-69-number/
class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        l = []
        f = 0
        while(temp > 0):
            new = temp%10
            l.append(new)
            temp = temp//10
 
        l.reverse()
  
        for x,i in enumerate(l):
            if(f == 1):
                break
        
            if (l[x] != 9):
                l[x] = 9
                f = 1
                
                
        l = [str(integer) for integer in l]

        a_string = "".join(l)

        return int(a_string)