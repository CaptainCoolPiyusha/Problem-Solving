# Pattern 10
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
# * * * * 
# * * * 
# * * 
# * 
  
class Solution:
    def pattern10(self, N):
        self.upper_traingle(N)
        self.lower_traingle(N)

    def lower_traingle(self, N):
        for i in range(N): # 0 to 5
            if i==N-1:
                continue  
            j = N-i-1
            print('* ' * (j))

    def upper_traingle(self, N):
        for i in range(N): # 0 to 5 
            print('* ' * (i+1))
                

sol = Solution()
N = 5
sol.pattern10(N)