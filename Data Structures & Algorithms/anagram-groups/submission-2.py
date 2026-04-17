class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_hashmap = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in freq_hashmap:
                freq_hashmap[sorted_word].append(word)
            else:
                freq_hashmap[sorted_word] = [word]
        
        return list(freq_hashmap.values())

        