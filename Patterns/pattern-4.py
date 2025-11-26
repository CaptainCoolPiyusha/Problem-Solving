# Pattern 4
# 1 
# 2 2
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5

class Solution:
    def pattern4(self, N):
        for i in range(N): # 0 to 5 
            for j in range(i+1):
                print(i+1, end=' ')
            print() 

sol = Solution()
N = 5
sol.pattern4(N)