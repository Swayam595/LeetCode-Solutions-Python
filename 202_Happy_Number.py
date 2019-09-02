class Solution:
##### LeetCode Solution #####
    def isHappy(self, n: int) -> bool:
        hash_table = {} 
        sum_of_square = 0
        
        while sum_of_square != 1:
            sum_of_square = 0
            for i in str(n):
                sum_of_square += int(i)**2
            n = sum_of_square
            if n not in hash_table:
                hash_table[n] = True
            else:
                return False
        return True
    
    ##### My Solution by finding unit digits using modulus and taking its square ##### 
    #def isHappy(self, n: int) -> bool:
    #    hash_table = {} 
    #    if n == 1:
    #       return True
    #    while True:
    #        sum_of_digits = 0
    #        while n > 0:
    #            unit = n % 10
    #            sum_of_digits = sum_of_digits + unit**2
    #            n = n // 10
    #        if sum_of_digits == 1:
    #            return True
    #        elif sum_of_digits in hash_table:
    #            return False
    #        else:
    #            hash_table[sum_of_digits] = True
    #            n = sum_of_digits
