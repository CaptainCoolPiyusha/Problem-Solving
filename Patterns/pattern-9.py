# Pattern 9
#         *    
#       * * *   
#     * * * * *  
#   * * * * * * * 
# * * * * * * * * *
#   * * * * * * * 
#     * * * * *  
#       * * * 
#         *    
  
class Solution:
    def pattern9(self, N):
        self.upper_traingle(N)
        self.lower_traingle(N)

    def lower_traingle(self, N):
        for i in range(N):
            if i==0:
                continue
            j = N-i-1
            # This will be one line, one pattern
            print('  ' * (N-j-1), end='')   
            print('* ' * ((j*2)+1), end='')
            print('  ' * (N-j-1))
            # After this there will be new line 

    def upper_traingle(self, N):
        for i in range(N):
            
            # This will be one line, one pattern
            print('  ' * (N-i-1), end='')   
            print('* ' * ((i*2)+1), end='')
            print('  ' * (N-i-1))
            # After this there will be new line
                

sol = Solution()
N = 5
sol.pattern9(N)