  #####   My Solution to find Peak Index in a Mountain Array  ####
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':
        for i in range(len(A)):         #   Iterate on every index of A
            if A[i] < A[i+1]:           #   If the element at the current index is less than the element in next index then continue
                continue
            else:                        #   Else Return the index
                return i
           
    """
    #####   LeetCode Solution   #####
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':
        return A.index(max(A)
    """
        
