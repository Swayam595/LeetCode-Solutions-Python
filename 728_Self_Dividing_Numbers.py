def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        temp = 0    #   To Store the current number
        ans = []    #   To store self Dividing numbers
        digit = 0   #   To store the unit digit of the current number
        
        while left <= right:             #   Iterate till left is less than right
            temp = left                  #   Take the current number in temp
            while temp != 0:             #   Iterate till temp is not equal to 0
                digit = int(temp%10)     #   Find the unit digit of the numbers
                if digit == 0 or left % digit != 0:     #   If the digit is zero or its division with the current number reminder not eqaul to zero then the number is not self dividing break and change the current number
                    break
                else:       #   Else the number is selfdividing so remove the unit digit from the curren the number 
                    temp = int(temp/10)
            if temp == 0: ans.append(left)      # If the current digit is zero then add it to the ans list  
            left+=1         #   Take the next number
            
        return ans          #   Return the ans list
                    
