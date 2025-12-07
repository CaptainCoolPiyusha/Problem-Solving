# Pattern 13

# 1
# 2 3 
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
 
class Solution:
    def pattern13(self, N):
        cnt = 1
        for i in range(N):
            for j in range(i+1):
                print(cnt, end=' ')
                cnt+=1
            print()     
                

sol = Solution()
N = 5
sol.pattern13(N)