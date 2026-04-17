class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        result = [0] * n

        for temp in range(n):
            for checkTemp in range (temp+1, n):
                if temperatures[checkTemp] > temperatures[temp]:
                    result[temp] = checkTemp - temp
                    break

        return result 
                 
        