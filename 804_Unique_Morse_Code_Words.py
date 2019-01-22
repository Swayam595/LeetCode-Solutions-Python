class Solution:    
    ####    My Solution to find Unique Morse Code  ####
    """"def uniqueMorseRepresentations(self, words):
        ""
        :type words: List[str]
        :rtype: int
        ""
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]   #   Morse code of the alphabets in alphabetical order
        
        result = []         #   Result List
        
        for i in words:     # Iterate over all the elements of the input list
            code = ""       # Take an empty constant to store the morse code of each word in the input list
            for j in i:     #  Iterate over all the letters of a particular word of the input list
                code = code + morse[ord(j) - 97]    #   create the morse code 
            if code not in result:      #   Check if the created code is present or not
                result.append(code)     # If not then append the code into the result list
                
        return len(result)          #   Return the lenght of result containing unique codes 
        """
    
    ####    LeetCode Solution   ####
    def uniqueMorseRepresentations(self, words):
        s = set()      #   We choose set because a set store only unique elements 
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]   #   Morse code of the alphabets in alphabetical order
        
        letter = "abcdefghijklmnopqrstuvwxyz"
        
        d = dict()  # To store alphabet and there corresponding morse code
        
        for i in range(len(letter)):    #   Store the alphabet and there corresponding morse code
            d[letter[i]] = morse[i]
            
        for i in words:     # Iterate over all the elements of the input list
            code = ""       # Take an empty constant to store the morse code of each word in the input list
            for j in i:     #  Iterate over all the letters of a particular word of the input list
                code = code + d[j]    #   create the morse code 
            s.add(code)     # Add code into the set s
        
        return len(s)       #   Return the lenght of set s containing unique codes
        
