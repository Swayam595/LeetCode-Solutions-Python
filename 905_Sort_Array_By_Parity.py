class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        """"result = []     #   Create a list to store the result
        l = 0           #   Index to store the even number from 0
        r = len(A) - 1  #   Index to store the odd number from end
        
        for i in A:     # Iterate over all elemnets of A
            if i % 2:   #   If i % 2 gives a reminder then its odd 
                result.insert(r , i)        #   Insert at the end
                r = r - 1                   #   Decrement r
            else:       #   Else the number is even 
                result.insert(l,i)          #   Insert at the front
                l = l + 1                   #   Increment l
        
        return result                       #   Return the result list  """
        
        even_list = []
        odd_list = []
        
        for i in A:                         #   Iterate over all the elements of A
            if i % 2:                       #   If i % 2 gives a reminder then its odd 
                odd_list.append(i)          #   Append it to the odd_list
            else:                           #   Else the number is even 
                even_list.append(i)         #   Append it to the even_list
                
        return (even_list + odd_list)       #   Append both the list 
