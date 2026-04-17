class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1, max(piles)
        result = right

        while left <= right:
            middle = (left+right) // 2
            sum = 0
            for p in piles:
                sum += math.ceil(float(p) / middle)
            if sum <= h:
                result = middle
                right = middle-1
            else:
                left = middle+1
        return result


             
        
        