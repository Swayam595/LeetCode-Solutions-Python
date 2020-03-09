 #### using bit manupulation ####
 def isPowerOfFour(self, num: int) -> bool:
        return (num != 0 and (num & (num - 1) == 0 and not(num & 0xAAAAAAAA)))


###### Using Loop to find have one 1 and even number of zeros #####
#     def isPowerOfFour(self, num: int) -> bool:
#         if num == 1: return True
        
#         if num and not(num &(num - 1)):
#             count = 0
#             while num > 1:
#                 num >>= 1
#                 count += 1
            
#             if count % 2 == 0:
#                 return True
        
#         return False
