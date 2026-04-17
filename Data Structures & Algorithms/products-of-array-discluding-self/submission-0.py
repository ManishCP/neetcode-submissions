class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero_counter = 0
        product = 1
        length = len(nums)

        for i in range(length):
            if nums[i] == 0:
                zero_counter += 1
            else:
                product *= nums[i]
        
        for j in range(length):
            if (zero_counter > 1):
                nums[j] = 0
            elif(zero_counter == 1):
                if nums[j] == 0:
                    nums[j] = product
                else:
                    nums[j] = 0
            else:
                nums[j] = int(product / nums[j])

        return nums