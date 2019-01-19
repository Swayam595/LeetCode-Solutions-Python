class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        row = 0
        column = 0
        
        while row < len(A):               #  Iterate over all the rowas of A
            while column < len(A[row]):        #  Iterate over all the columns of a row in A
                A[row][column] = 1 - A[row][column] #  Reverse the elements value of the row 
                column = column + 1               #  Increment j to go to next column
            A[row].reverse()              #  After reverseing the element value in a row, reverse the row
            column = 0                        #  Make the column pointer to 0 for next row first column
            row = row + 1                   #  Go to the next row 
                
        return A
    
    
    
    
            
        
        
