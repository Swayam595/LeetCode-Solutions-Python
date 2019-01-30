def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if len(digits) == 0:            #   If the input is an empty list
            digits[0] += 1              #   Then increment add one to the list
            return digits               #   Return the digits list containing the answer
            
        n = len(digits) - 1             #   Index of the last element of the list
        
        if digits[n] == 9:              #   If the last element is 9 on adding one we get an carry
            carry = 1                   #   Make the carry as 1
            while carry and n>=0:       #   If there is a carry and then iterate over the input list 
                if n == 0 and digits[n] == 9:   #   If current element of the list is at 0 and has a value as 9
                    digits[n] = 0       #   Then make the current element value as 0
                    digits.insert(0,1)  #   Insert 1 at the begining of the list denoting the carry bit
                    return digits       #   Return the output in the digits list
                
                elif digits[n] == 9:    #   If the current elemet is 9 but the index is somewhere orther than 0 then make the current element vaule as 0 and make carry as 1
                    digits[n] = 0
                    carry = 1
                    
                else:                   #   If the previous element was 9 then add the carry bit in the present element(not 9) irespective of index
                    digits[n] += 1
                    return digits       #   Return the output in the digits list
                n -= 1
                    
        else:                           #   If the current element is not 9 then add 1 to the current element        
            digits[n] += 1 
        
        return digits                   #   Return the output in the digits list
        
