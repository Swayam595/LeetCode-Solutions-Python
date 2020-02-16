def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        if len(paths) == 0: return [1] * N
        
        output = [1] + [0] * (N - 1)
        flower = [1,2,3,4]
        graphs = [[] for _ in range(N)]
        
        for x,y in paths:
            graphs[x - 1].append(y - 1)
            graphs[y - 1].append(x - 1)
            
        
        for i in range(1,N):
            f = 0
            j = 0
            while j < len(graphs[i]):
                if output[graphs[i][j]] != flower[f]:
                    j += 1
                else:
                    f += 1
                    j = 0
                
            output[i] = flower[f]
            
        return output
