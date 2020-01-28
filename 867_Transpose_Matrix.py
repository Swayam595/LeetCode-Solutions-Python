def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        columns = len(A[0])
        result = []
        j = 0
        
        while j < columns:
            i = 0
            temp = []
            while i < rows:
                temp.append(A[i][j])
                i += 1
            result.append(temp)
            j += 1
            
        return result
