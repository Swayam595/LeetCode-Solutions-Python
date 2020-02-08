def findAnagrams(self, s: str, p: str) -> List[int]:
        #import string
#         if len(s) < len(p): return []
        
#         p = sorted(p)
        
#         result = []
#         i = 0
        
#         while i <= (len(s) - len(p)):
#             value = sorted(s[i:i+len(p)])
#             if value == p:
#                 result.append(i)
#             i += 1
#        return result
            
            
        if len(p) > len(s):
            return []
        
        hash_table = {ch:idx for idx,ch in enumerate(string.ascii_lowercase)}
        i = 0
        anagram = [0] * 26
        check = [0] * 26
        result = []
        
        for ch in p:
            anagram[hash_table[ch]] += 1
            
        
        for ch in s[:len(p) - 1]:
            check[hash_table[ch]] += 1
