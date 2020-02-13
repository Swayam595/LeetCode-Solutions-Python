def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 7: return 0
        
        hash_table = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        
        no_of_ballons = 9223372036854775807
        
        for i in text:
            if i in hash_table:
                hash_table[i] += 1
                
        hash_table['l'] //= 2
        hash_table['o'] //= 2
                
        for i in hash_table:
            if no_of_ballons > hash_table[i]:
                no_of_ballons = hash_table[i]
        
        return no_of_ballons
