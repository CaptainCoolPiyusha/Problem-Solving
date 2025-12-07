# Pattern 8
# * * * * * * * * *
#   * * * * * * * 
#     * * * * *  
#       * * * 
#         *    
  


class Solution:
    def pattern8(self, N):
        for i in range(N):
            j = N-i-1
            # This will be one line, one pattern
            print('  ' * (N-j-1), end='')   
            print('* ' * ((j*2)+1), end='')
            print('  ' * (N-j-1))
            # After this there will be new line 
                

sol = Solution()
N = 5
sol.pattern8(N)