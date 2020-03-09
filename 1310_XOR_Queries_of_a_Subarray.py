#### leetcode solution using prefix array ####
def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        prefix = [0] * (len(arr)+1)
        
        for i in range(len(arr)):
            prefix[i+1] = prefix[i] ^ arr[i]
            
        for l,r in queries:
            temp = prefix[l] ^ prefix[r + 1]
            result.append(prefix[l] ^ prefix[r + 1])
            
        return result
