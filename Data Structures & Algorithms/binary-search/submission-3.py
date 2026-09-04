class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1

        while i <= j:
            center = (i+j)//2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                i = center+1
            else:
                j = center-1
        
        return -1

        