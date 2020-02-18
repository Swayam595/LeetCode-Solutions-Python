#### My Solution ####
def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        answer = list()
        
        sum_of_evens = 0
        for i in A:
            if i % 2 == 0:
                sum_of_evens += i
                
        for val,index in queries:
            if A[index] % 2 == 0:
                sum_of_evens -= A[index]
                A[index] += val
                if A[index] % 2 == 0:
                    sum_of_evens += A[index]
            elif (A[index] + val) % 2 == 0:
                A[index] += val
                sum_of_evens += A[index]
            else:
                A[index] += val

#### Leetcode Solution ####
def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        answer = list()
        
        sum_of_evens = 0
        for i in A:
            if i % 2 == 0:
                sum_of_evens += i
                
        for val,index in queries:
            if A[index] % 2 == 0:
                sum_of_evens -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                sum_of_evens += A[index]
            answer.append(sum_of_evens)
            
        return answer 
