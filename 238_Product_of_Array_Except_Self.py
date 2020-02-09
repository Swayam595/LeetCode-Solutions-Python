def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        l = [1] * len(nums)
        r = [1] * len(nums)
        
        i = 0
        j = len(nums) - 1 
        
        while i < len(nums) - 1:
            l[i+1] = l[i] * nums[i]
            r[j - 1] = r[j] * nums[j]
            
            i += 1
            j -= 1
            
        i = 0
        while i < len(nums):
            result.append(l[i]*r[i])
            i += 1
            
        return result
