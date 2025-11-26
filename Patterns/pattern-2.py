# Pattern 2
# * 
# * * 
# * * * 
# * * * * 
# * * * * *

class Solution:
    def pattern2(self, N):
        for i in range(N): # 0 to 5 
            print('* ' * (i+1))

sol = Solution()
N = 5
sol.pattern2(N)