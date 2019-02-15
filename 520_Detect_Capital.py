""" My Solution Using iterative approach """
    def detectCapitalUse(self, word: 'str') -> 'bool':
        if len(word) == 0: return false     #   If the input word is empty then return 0     
        i = 0           # A variable to store the index  
        count = 0       # To count the number of capital words
        is_capital = True # A variable to store the if an element is capital and 
                          # with an initial value TRUE because the First character can be true
        
        while i < len(word) :   #   Iterate over all the character of word
            if word[i].isupper() and is_capital:  #   If the current character is uppercase and
                                                  #   is_capital is true then increment count value
                count += 1
            else:   #   If the current character is lower then make is_capital to FALSE
                is_capital = False
            
            if word[i].isupper() and not is_capital:  #   If a character is upper but is_capital is FALSE then return FALSE
                return False
            i += 1  #   Increment i with every iteration
        
        # When we are out of the loop 
        if (count <= 1 and not is_capital) or is_capital:     # If the word has the first character as capital 
                                                              # or all the characters of the word is capital then return TRUE 
            return True
        else:   #   Else return FALSE
            return False
            
    """ Leetcode Solution ""
    def detectCapitalUse(self, word: 'str') -> 'bool':
        return True if word.isupper() or word.istitle() or word.islower() else False   
        """
