# Pattern 5
# * * * * * 
# * * * *
# * * *
# * *
# *

class Solution:
    def pattern5(self, N):
        for i in range(N,0,-1): # 5 to 1 (excluding the 0)
            print('* ' * i)

sol = Solution()
N = 5
sol.pattern5(N)