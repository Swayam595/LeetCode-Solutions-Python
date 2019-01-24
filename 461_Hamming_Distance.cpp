def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        hamming = bin(x ^ y)[2:]        #   Find the excor of the give number because odd bits 1 in exor
        count = 0                       #   To store number of 1's
        
        for i in hamming:               #   Iterate over all the character of hamming 
            if i == '1':                #   If 1 is detected then increment count
                count += 1
                
        return count                    #   Return count value
