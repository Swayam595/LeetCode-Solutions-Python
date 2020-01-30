def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len (matrix) == 1 or len(matrix[0]) == 1:
            return True
        total_elements = len(matrix) * len(matrix[0]) - 2
        m = len(matrix) - 2
        n = 0
        
        while total_elements > 0:
            x = m + 1
            y = n + 1
            
            while x < len(matrix) and y < len(matrix[0]):
                if matrix[m][n] != matrix[x][y]:
                    return False
                x += 1
                y += 1
            
            if m != 0:
                m -= 1
            else:
                n += 1
        
            total_elements -= 1
            
        return True
