class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_words = ["".join(sorted(word)) for word in strs]
        hashmap_word = {}

        for i in range(len(sorted_words)):
            if sorted_words[i] not in hashmap_word:
                hashmap_word[sorted_words[i]] = [strs[i]]
            else:
                hashmap_word[sorted_words[i]].append(strs[i])
        
        return list(hashmap_word.values())