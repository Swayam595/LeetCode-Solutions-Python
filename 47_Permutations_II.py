###### My Solution ######
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            return self.perm(nums, 0)
        
    def perm(self, nums, m):
        if m == len(nums)-1:
            return [[nums[m]]]
        else:
            temp_perm = self.perm(nums, m + 1)
            result = []
            for i in temp_perm:
                pos = 0
                j = 0
                temp = [0] * (len(i)+1)
                while pos <= len(i):
                    if pos == j:
                        temp[pos] = nums[m]
                        pos += 1
                        while j < len(i):
                            temp[j+1] = i[j]
                            j += 1
                        if temp not in result: result.append(temp)
                        temp = [0] * (len(i)+1)
                        j = 0
                    else:
                        temp[j] = i[j]
                        j += 1
                        
            return result
            
###### Leetcode Solution #######
 def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            nums.sort()
            solution = []
            combination = []
            
            self.perm(nums, solution, combination)
            
            return solution
        
    def perm(self, nums, solution, combination):
        if nums == []:
            solution.append(list(combination))
            return
        else:
            i = 0
            while i < len(nums):
                if i > 0 and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                else:
                    combination.append(nums[i])
                    new_nums = nums[:i] + nums[i+1:]
                    self.perm(new_nums, solution, combination)
                    combination.pop()
                    i += 1
