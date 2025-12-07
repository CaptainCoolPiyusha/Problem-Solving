# Pattern 15

# ABCDE
# ABCD
# ABC
# AB
# A
 
class Solution:
    def pattern15(self, N):
        
        for i in range(N, 0 , -1):
            ch = 65
            for j in range(i):
                print(chr(ch), end=' ')
                ch+=1

            print()     
                

sol = Solution()
N = 5 
sol.pattern15(N)