# Pattern 16

# A
# BB
# CCC
# DDDD
# EEEEE
 
class Solution:
    def pattern16(self, N):
        ch = 65
        for i in range(N):            
            for j in range(i+1):
                print(chr(ch), end=' ')
                
            print()  
            ch+=1   
                

sol = Solution()
N = 5 
sol.pattern16(N)