def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        count_U = 0
        count_D = 0
        count_R = 0
        count_L = 0
        
        for i in moves:     # Iterate over moves 
            if i == "U":    # Everytime "U" is detected then increment count_U
                count_U = count_U + 1
            elif i == "D":  # Everytime "D" is detected then increment count_D
                count_D = count_D + 1
            elif i == "L":  # Everytime "L" is detected then increment count_L
                count_L = count_L + 1
            elif i == "R":  # Everytime "R" is detected then increment count_R
                count_R = count_R + 1
        
        if (count_L - count_R) == 0 and (count_U - count_D) == 0:       #If the difference of count_U , count_U and count_U , count_U are 0 then Robot Return to Origin
            return True
        else:   #   Else Robot doesnt Return to Origin
            return False
            """
        k = moves.count("U") - moves.count("D")
        s = moves.count("L") - moves.count("R")
        
        if k or s:
            return False
        else:
            return True
        """
