def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 0
        n = 0
        while candies != 0:
            if i == num_people:
                i = 0
            n += 1
            if n <= candies:
                result[i] += n
                candies -= n
                i += 1
            else:
                result[i] += candies
                candies = 0
                
        return result
