# Pattern 7
#         *    
#       * * *   
#     * * * * *  
#   * * * * * * * 
# * * * * * * * * *


class Solution:
    def pattern7(self, N):
        for i in range(N):
            # This will be one line, one pattern
            print('  ' * (N-i-1), end='')   
            print('* ' * ((i*2)+1), end='')
            print('  ' * (N-i-1))
            # After this there will be new line 
                

sol = Solution()
N = 5
sol.pattern7(N)