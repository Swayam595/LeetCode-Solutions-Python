def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        hash_table = dict()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    hash_table[(i,j)] = []
        
        if len(hash_table) == 1:
            return 4
                    
    
        perimeter = 0
        
        for cor in hash_table:
            i = cor[0]
            j = cor[1]
            
            xu = i - 1
            yu = j
            if (xu, yu) not in hash_table:
                perimeter += 1
                
            xr = i 
            yr = j - 1
            if (xr, yr) not in hash_table:
                perimeter += 1
                
            xd = i + 1
            yd = j
            if (xd, yd) not in hash_table:
                perimeter += 1
                
            xl = i
            yl = j + 1
            if (xl, yl) not in hash_table:
                perimeter += 1
                    
        return perimeter
