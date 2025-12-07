# Pattern 17

#----A
#---ABA
#--ABCBA
#-ABCDCBA
 
class Solution:
    def pattern17(self, N):
        for i in range(N): # 0 se leke 4

            ch = ord('A')
            breakpoint = (2*i+1) // 2 # Till the half it will be increasing then decreasing
            #leading spaces
            for j in range(N-i-1): # for j=0 j<(5-0-1)<4
                print(' ', end='')
            
            for j in range(2 *i + 1):
                print(chr(ch), end='')
                
                if j < breakpoint:
                    ch+=1
                else:
                    ch-=1
            
            for j in range(N-i-1): # for j=0 j<(5-0-1)<4
                print(' ', end='')         
            print()     
                

sol = Solution()
N =4
sol.pattern17(N)    