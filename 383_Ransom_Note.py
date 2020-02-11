def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = dict()
        magazine_dict = dict()
        
        for i in ransomNote:
            if i not in ransom_dict:
                ransom_dict[i] = 1
            else:
                ransom_dict[i] += 1
        
        for i in magazine:
            if i not in magazine_dict:
                magazine_dict[i] = 1
            else:
                magazine_dict[i] += 1
                
        for i in ransom_dict:
            if i in ransom_dict and i in magazine_dict and ransom_dict[i] <= magazine_dict[i]:
                continue
            else:
                return False
        
        return True
