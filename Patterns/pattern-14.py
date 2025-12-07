# Pattern 14

# A
# AB
# ABC
# ABCD
# ABCDE
 
class Solution:
    def pattern14(self, N):
        
        for i in range(N+1):
            ch = 65
            for j in range(i):
                print(chr(ch), end=' ')
                ch+=1

            print()     
                

sol = Solution()
N = 5 
sol.pattern14(N)