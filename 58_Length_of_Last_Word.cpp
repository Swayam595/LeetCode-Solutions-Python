 ### My solution to Find the length of the last word ###
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:             # if the input string is empty then return 0
            return 0

        ans = 0                     # A variable to store the outpt
    
        for i in range(len(s) - 1 , -1 , -1):   # Start iterating at the end of the string
            if s[i] == " " and ans:             # If there is a last word then ans wont be zero and upon encountering a " " break out of the loop 
                break;
            
            if s[i] != " ":         # If the current character is not an empty space then incremnet ans
                ans = ans + 1
        
        return ans                  # Return ans
        
        """"
        ### LeetCode Solution to find the ength of the last word ###
    def lengthOfLastWord(self, s):
        try:            #   Try if the string has elements
            return len(s.split()[-1])   #   Split each word of the input string into different string and stroe into a list and reutn the length of the last element in the list
        except:         #   If the input string has no elements then return 0
            return 0
            """
