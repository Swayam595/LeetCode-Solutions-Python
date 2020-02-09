def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hash_table = {ch:idx for idx, ch in enumerate(string.ascii_lowercase)}
        s1_table = [0] * 26
        s2_table = [0] * 26
        startIdx = 0
        
        for ch in s1:
            s1_table[hash_table[ch]] += 1
            
        for ch in s2[:len(s1)-1]:
            s2_table[hash_table[ch]] += 1
            
        for ch in s2[len(s1)-1:]:
            s2_table[hash_table[ch]] += 1
            if s1_table == s2_table:
                return True
            s2_table[hash_table[s2[startIdx]]] -= 1
            startIdx += 1
        
        return False
