def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            diff = stones[-1] - stones[-2]
            stones = stones[:-2]
            
            if diff == 0 and len(stones) == 0:
                return 0
            elif diff == 0 and len(stones) != 0:
                continue
            else:
                stones.append(diff)
            
                
        return stones[0]
