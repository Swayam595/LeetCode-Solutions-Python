#### My Solution using 2D array  ####
def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0: return 1
        
        graph = [[0] * N for _ in range(N)] 
        
        for i in trust:
            graph[i[0] - 1][i[1] - 1] = 1
        
        #print (graph)
        
        for i in range(N):
            if sum(graph[i]) == 0:
                total = 0
                for row_no in range(N):
                    total = total + graph[row_no][i]
                if total == N - 1:
                    return i + 1
        
        return -1
        
#### Leetcode Solution ####
def findJudge(self, N: int, trust: List[List[int]]) -> int:
        graph = [0] * (N + 1)
        
        for x,y in trust:
            graph[x] -= 1
            graph[y] += 1
            
        for i in range(1, N + 1):
            if graph[i] == N - 1:
                return i
        
        return -1
