class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        temp = []

        # for i in range(len(nums)):
        #     if nums[i] in temp:
        #         return True
        #     else:
        #         temp.append(i)

        for num in nums:
            if num in temp:
                return True
            else:
                temp.append(num)
        
        return False
        
         