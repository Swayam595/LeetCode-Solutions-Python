 """" LeetCode Solution
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        return bin(int(a,2)+int(b,2))[2::]      #   First convert the binary number to there decimal equivalent, 
                                                #   then add the numbers and bind there binary 
                                                #   and then every element in the output binary number from index 2 onwards
        """ 

"""   My Solution to Add two binary   """
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        
        if int(a) + int(b) == 0:return "0"      #   If both the binary numbers are zero then there sum is 0 thus return 0
        if not len(a) and not len(b): return "0"    #   If both the binary numbers are empty then return 0
            
        ans = ""        #   A empty string to store the output
        i = len(a)      #   Size of first binary number
        j = len(b)      #   Size of second binary number
        bits_sum = 0    #   A temp variable to store the sum of each bits
        carry = 0       #   A variabe to store the carry bits
        
        while i and j:  #   Iterate from end to beginning of each binary number
            i -= 1      #   Decrement i and j pointer to access the last element of the binary numbers
            j -= 1
            bits_sum = int(a[i]) + int (b[j]) + carry   #   Find the sum of bits with carry
            carry = 0   #   After adding carry bit in finding sum make it zero
            if bits_sum == 3:   #   If the sum is 3 then a[i], b[i] and carry are all 1 while finding sum
                carry = 1   #   Since the ninary only support only 0's and 1's we can represent 3 as carry 1 and sum is 1
                ans = str(1) + ans  #   store the sum in the ans string
            elif bits_sum == 2: #   If the sum is 2 then either any two numbers in a[i], b[i] and carry are 1
                carry = 1   #   Represent 2 as carry 1 and sum 0
                ans = str(0) + ans  #   Store the sum in the ans string
            else:       #   Else sum is either O or 1 then 
                ans = str(bits_sum) + ans   #   Store the sum in the ans string
        
        while i:        #   If there are still binnary bits in 'a'
            i -= 1      #   Decremnet i to access the next element
            bits_sum = int(a[i]) + carry    #   Find the sum of bits with carr
            carry = 0   #   After adding carry bit in finding sum make it zero
            if bits_sum == 2:   #   If the sum is 2 then either any two numbers in a[i], b[i] and carry are 1
                carry = 1    #   Represent 2 as carry 1 and sum 0
                ans = str(0) + ans  #   Store the sum in the ans string
            else:       #   Else sum is either O or 1 then 
                ans = str(bits_sum) + ans   #   Store the sum in the ans string
            
        while j:        #   If there are still binnary bits in 'b'
            j -= 1      #   Decremnet j to access the next element
            bits_sum = int(b[j]) + carry    #   Find the sum of bits with carr
            carry = 0   #   After adding carry bit in finding sum make it zero
            if bits_sum == 2:   #   If the sum is 2 then either any two numbers in a[i], b[i] and carry are 1
                carry = 1    #   Represent 2 as carry 1 and sum 0
                ans = str(0) + ans  #   Store the sum in the ans string
            else:       #   Else sum is either O or 1 then 
                ans = str(bits_sum) + ans   #   Store the sum in the ans string
                
        if carry: return str(carry) + ans   #   If there is a carry bit then append the carry bit in the fornt of the ans string
        else: return ans        #   If there is not carry bits then return just the ans string
        
   
        
        
