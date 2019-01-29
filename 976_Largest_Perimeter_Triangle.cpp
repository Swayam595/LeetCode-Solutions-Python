def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        A.sort()
        i = len(A) - 3          #    Index of the third last element
        
        while i >= 0:           #    Iterate till i is not less than zero
            if A[i] + A[i+1] > A[i+2]:      #   If a three consecutive elements form an triangle then return there perimeter
                return A[i] + A[i+1] + A[i+2]
            i -= 1              #    Decrement i
        return 0                #   If 3 sides dont form triangle then return 0
       
