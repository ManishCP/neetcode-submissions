class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_hashmap = {}

        for num in nums:
            if num in count_hashmap:
                count_hashmap[num] += 1
            else:
                count_hashmap[num] = 1

        

        # # Collect elements whose frequency > k (your logic idea)
        # for num in count_hashmap:
        #     if count_hashmap[num] > k:
        #         result.append(num)

        sorted_item = sorted(count_hashmap.items(), key=lambda x: x[1], reverse=True)

        result = []

        for ele, freq in sorted_item:
            result.append(ele)

        return result[:k]

        