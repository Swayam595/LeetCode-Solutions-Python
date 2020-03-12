#### My LeetCode Solution ####
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mode = 0
        total_data = 0
        data_len = 0
        min_flag = 1
        index = 0
        minimum = 0
        maximum = 0
        max_count = 0
        data_array = []
        
        while index < len(count):
            if count[index] != 0:
                data_len += count[index]
                total_data += (count[index] * index)
                if min_flag:
                    minimum = index
                    min_flag = 0
                if max_count < count[index]:
                    max_count = count[index]
                    mode = index
                maximum = index
                
            index += 1
            
        mean = total_data / data_len
        mid = data_len//2
        
        index, left_over = self.median_index(mid, count)
        
        if data_len % 2 == 0:
            if left_over:
                    median = index
            else:
                median = (index + index + 1)/2
        else:
            median = index
            
        return [minimum, maximum, mean, median, mode]
    
    def median_index(self, mid, count):
        left_over = 0
        index = -1 
        
        while mid != 0:
            index += 1
            if mid - count[index] >= 0:
                mid -= count[index]
            else:
                mid = 0
                left_over = count[index] - mid
        
        return [index, left_over]
        
#### Leetcode Soultion ####
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minC = 0
        while count[minC]==0:
            minC +=1
        maxC = len(count)-1
        while count[maxC]==0:
            maxC -=1
        
        meanC = sum([i*count[i] for i in range(len(count))]) / sum(count)
        
        modeC = count.index(max(count))
        
        cumCount=[count[0]] *len(count)
        for i in range(1,len(count)):
            cumCount[i]=cumCount[i-1]+count[i]
            
        median1 = bisect.bisect_right(cumCount, (sum(count)-1)/2)
        median2 = bisect.bisect_right(cumCount,sum(count)/2)

        return [float(minC), float(maxC), float(meanC), float((median1+median2)/2), float(modeC)]
