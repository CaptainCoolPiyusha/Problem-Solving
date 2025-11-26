# Pattern 5
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1

class Solution:
    def pattern6(self, N):
        for i in range(N, 0, -1): # 5 to 0
            for j in range(1, i+1):
                print(j, end=' ')
            print() 

sol = Solution()
N = 5
sol.pattern6(N)