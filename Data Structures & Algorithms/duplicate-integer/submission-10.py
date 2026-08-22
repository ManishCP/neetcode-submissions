class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        checkDup = {}

        for i in range(len(nums)):
            if nums[i] in checkDup:
                return True
            checkDup[nums[i]] = 1

        return False
        