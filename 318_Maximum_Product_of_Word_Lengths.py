#### Leetcode Solution using bit manupulation ####
def maxProduct(self, words: List[str]) -> int:
  d = {}
  for w in words:
    mask = 0
    for c in set(w):
      mask |= (1 << (ord(c) - 97))
    d[mask] = max(d.get(mask, 0), len(w))
  return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

#### My Leetcode Solution ####
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if len(words) == 0: return 0
        
        curr_words = []
        hash_table = {ch:idx for idx, ch in enumerate(string.ascii_lowercase)}
        result = 0
        
        for word in words:
            temp = [0] * 26
            for i in word:
                index = hash_table[i]
                if temp[index] == 1:
                    continue
                else:
                    temp[index] = 1
            curr_words.append(temp)
        
        i = 0
        
        while i < len(curr_words):
            j = i + 1
            while j < len(curr_words):
                flag_1 = 0
                flag_2 = 0
                x = 0
                while x < 26:
                    if curr_words[i][x] == curr_words[j][x] == 1:
                        flag_1 = 1
                        break
                    x += 1
                if not flag_1 and result < (len(words[i]) * len(words[j])):
                    result = len(words[i]) * len(words[j])
                j += 1
            i += 1
    
        return result
        
