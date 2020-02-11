def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        
        i = 0
        j = 0
        result = list()
        
        while i < len(nums1):
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    result.append(nums1[i])
                    j += 1
                    break
                elif nums1[i] < nums2[j]:
                    break
                else:
                    j += 1
            i += 1
            
        return result
