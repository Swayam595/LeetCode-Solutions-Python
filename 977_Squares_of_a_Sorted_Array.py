def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(len(A)):     # Iterate over all the elements of A
            A[i] = A[i] ** 2        # Square all the elements 
            
        A.sort()                    # Sort the list
            
        return A                    # Return the list
