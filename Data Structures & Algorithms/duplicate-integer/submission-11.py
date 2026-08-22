class Solution:
    def hasDuplicate(self, nums:list[int]) -> bool:
        #hashset since we want to find unique values

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
        