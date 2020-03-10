#### Leetcode Solution using Integer Limitations ####
def isPowerOfThree(self, n: int) -> bool:
        return (n > 0 and 3**19 % n == 0)
    
    
#### My Solution using math module####
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0: return False
#         import math
        
#         power = round(math.log(n)/math.log(3))
        
#         return 3**power == n
        
