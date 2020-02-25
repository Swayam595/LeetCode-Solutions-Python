def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        
        i = 0
        words = text.split(' ')
        
        while i <=  len(words) - 3:
            if words[i] == first and words[i + 1] == second:
                result.append(words[i+2])
                i += 2
            else:
                i += 1
                
        return result
