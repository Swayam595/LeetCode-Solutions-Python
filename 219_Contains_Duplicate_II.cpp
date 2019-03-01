def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0: return False       # if length of the input list is empty then return False

        dictonary = {}                        # create a dictonary 
        
        for i in range(len(nums)):            # iterate over the length of the input list
            if nums[i] in dictonary:          # if the element at i is in dictonary 
                dictonary[nums[i]].append(i+1)  # then append the index inside the element's list of indices 
            else:                             # if the element at i is not in dictonary 
                dictonary.update({nums[i]:[i+1]}) # then add the element and its index inside the dictonary 
    
        for x in nums:                        # iterate over all the elements of nums
            if len(dictonary[x]) > 1:         # if the element x has more than 1 index
                i = 0                         # to store the first index 
                for j in range(1,len(dictonary[x])):    # iterate over the length of the index list
                    if dictonary[x][j] - dictonary[x][i] <= k:    # if the difference of two indxe is less than 
                        return True           # or equal to the target then return TRUE
                    i = j                     # make i equal to j
        
        return False                          # if there is no two index of an element's which are not at most k units apart 
                                              # then return FALSE 
