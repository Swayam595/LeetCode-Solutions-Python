##################################################################
##################################################################
##
##    My Python Solution for finding the number of prime numbers between a given number
##
##    Time Complexity ---->  T(N) <= O(p * m)  
##    where m is the number of multiples of a prime number and 
##    p is the number of prime numbers
##
##################################################################
##################################################################

def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        elif n == 3:
            return 1
    
        temp_dict = dict()                    # a dictionary to keep track of the prime numbers
        count = 2                             # if n >= 4 then by default 2 and 3 are the prime number that are present
        
        for i in range(3,n):
            if i % 2 == 0 or i % 3 == 0:      # if a number is a multiple of 2 or 3 then dont add it to the dictionary
                continue
            else:
                temp_dict[i] = True
       
                
        for i in temp_dict:
            if temp_dict[i]:                # if a number is prime 
                count += 1                  # then increment the number of count
                j = 2
                prod = j*i
                
                while prod < n:           
                    if prod in temp_dict:  # make all of its multiple dictionary value to False
                        temp_dict[prod] = False
                    j += 1
                    prod = j * i
        
        return count
