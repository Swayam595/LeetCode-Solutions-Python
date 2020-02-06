def calPoints(self, ops: List[str]) -> int:
        stack = []
        total = 0
        
        for i in ops:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
                total += int(i)
            elif i =="C" and len(stack) != 0:
                top = stack.pop()
                total -= top
            elif i == "D" and len(stack) != 0:
                top = stack[-1]
                top *= 2
                total += top 
                stack.append(top)
            elif i == "+" and len(stack) > 1:
                t1 = stack[-1]
                t2 = stack[-2]
                top = t1 + t2
                total += top
                stack.append(top)
        
        return total
