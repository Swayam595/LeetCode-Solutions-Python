""" My Solution O(nlogn) runtime"""
    def maximumProduct(self, nums: 'List[int]') -> 'int':
        nums.sort()     #   Sort the array 
        return max((nums[-1] * nums[-2] * nums[-3]),(nums[-1] * nums[0] * nums[1])) #   Return the maximum product of last 3 elements or first two and last element

    
    """ LeetCode Solution O(n) runtime   ""
    def maximumProduct(self, nums: 'List[int]') -> 'int':
        max1 = min(nums)  # Store the minimum value of nums list, used to store largest element
        max2 = min(nums)  # Store the minimum value of nums list, used to store 2nd largest element
        max3 = min(nums)  # Store the minimum value of nums list, used to store 3rdlargest element
        
        min1 = max(nums)  # Store the maximum value of nums list, used to store smallest element
        min2 = max(nums)  # Store the maximum value of nums list, used to store 2nd smallest element
        
        for i in nums:    # Iterate over all the elements of the list
            if i <= min1: # If the current element is less than min1 then
                min2 = min1   # Store min1 value in min1, for keeping record of second smallest element 
                min1 = i      # Store i into min1, for keeping record of smallest element
            elif i <= min2:   # If the current element is greater or not equal to min1 but less than min2 then
                min2 = i      # Store it into min2, for keeping record of 2nd smallest element
                
            if i >= max1:     # If the current element is greater than max1 then
                max3 = max2   # Store max2 into max3, for keeping record of 3rd largeest element
                max2 = max1   # Store max1 into max2, for keeping record of 2nd largeest element
                max1 = i      # Store i into max1, for keeping record of largest element
            elif i >= max2:   # If the current element is less or not equal min1 but greater or equal to max2 
                max3 = max2   # Store max2 into max3, for keeping record of 3rd largeest element
                max2 = i      # Store i into max2, for keeping record of 2nd largest element
            elif i >= max3:   # If the current element is less or not equal max1 and max2 but greater or equal to max3 
                max3 = i      # Store i into max3, for keeping record of 3rd largest element
        
        return max((max3 * max2 * max1) , (max1 * min1 * min2))"""
