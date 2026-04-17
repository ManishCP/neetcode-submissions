class Solution:
    def findMin(self, nums: List[int]) -> int:

        minNum = nums[0]

        for i in range(len(nums)):
            minNum = min(nums[i], minNum)

        return minNum
        