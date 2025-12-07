# Pattern 12

# 1              1 
# 1 2          2 1 
# 1 2 3      3 2 1 
# 1 2 3 4  4 3 2 1 
 
class Solution:
    def pattern12(self, N):
        for i in range(N):
            for j in range(i+1):
                print(j+1, end=' ')
            print('  ' * 2 * (N-(i+1)), end=' ')
            for j in range(i+1, 0, -1 ):
                print(j, end=' ') 
            print()
                 
                

sol = Solution()
N = 4
sol.pattern12(N)