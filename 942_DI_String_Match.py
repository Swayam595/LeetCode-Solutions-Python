def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        A = []                  #   List to store the answer 
        lo , hi = 0 , len(S)    #   Initialize lo as 0 and hi as length of input string
        
        for i in S:             #   Iterate over each character if the input string
            if i == 'I':        #   If 'I' is detected then append lo
                A.append(lo)    
                lo = lo + 1     #   Increment lo
            else:               #   If 'D' is detected then append hi
                A.append(hi)
                hi = hi - 1     #   Decrement hi
            
        A.append(lo)            #   Append lo for the last element satisfying the given condition 
        
        return A                #   Return the answer list
