# Pattern 3
# 1 
# 1 2 
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5

class Solution:
    def pattern3(self, N):
        for i in range(N): # 0 to 5 
            for j in range(i+1):
                print(j+1, end=' ')
            print()

sol = Solution()
N = 5
sol.pattern3(N)