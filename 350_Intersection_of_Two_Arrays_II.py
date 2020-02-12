###### My Solution Usning sorting and less space #######
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        nums1.sort()
        nums2.sort()
        
        i = 0
        j = 0
        result = []
        
        while i < len(nums1):
            if j < len(nums2) and nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif j < len(nums2) and nums1[i] < nums2[j]:
                i += 1
            elif j < len(nums2):
                j += 1
            else:
                break
        
        return result
        
 ###### Leetcode Solution using dictionary #######
 def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_table1 = dict()
        hash_table2 = dict()
        result = list() 
        
        for num in nums1:
            if num in hash_table1:
                hash_table1[num] += 1
            else:
                hash_table1[num] = 1
        
        for num in nums2:
            if num in hash_table1:
                c = hash_table1[num]
                if num in hash_table2:
                    hash_table2[num] += 1
                    if hash_table2[num] <= c:
                        result.append(num)
                else:
                    hash_table2[num] = 1
                    result.append(num)
                    
        return result
