# Pattern 11
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
  
class Solution:
    def pattern11(self, N):
        for i in range(N):
            if i%2==0:
                #even
                start = 1
            else:
                start = 0
            for j in range(i+1):
                print(start,end=' ')
                # toggle the value of start
                start = 1 - start
            print()   
                

sol = Solution()
N = 5
sol.pattern11(N)