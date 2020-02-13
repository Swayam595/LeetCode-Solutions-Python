##### My Solution using a hash table for char and their index #####
def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        char_table = {ch:idx for idx, ch in enumerate(string.ascii_lowercase)}
        lines = 1
        units = 0
        
        for i in S:
            units += widths[char_table[i]]
            if units > 100:
                lines += 1
                units = widths[char_table[i]]
            elif units == 100:
                lines += 1
                units = 0
        
        return [lines, units]





##### Leetcode Solution #####
def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        if len(S) < 1: return [0, 0] 
        #ascii_table = {ch:idx for idx, ch in enumerate(string.ascii_lowercase)}
        lines = 1
        units = 0
        
        for i in S:
            units += widths[ord(i) - ord('a')]
            if units > 100:
                lines += 1
                units = widths[ord(i) - ord('a')]
            elif units == 100:
                lines += 1
                units = 0
        
        return [lines, units]
