#### Leetcode solution using constant data structure ####
def distributeCandies(self, candies: List[int]) -> int:
        counter = 1
        candies.sort()
        
        for i in range(len(candies) - 1):
            if candies[i] != candies[i+1]:
                counter += 1
                
        return min(counter, len(candies)//2)
        
#### Leetcode solution using set ####
def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)), len(candies)//2)
        
