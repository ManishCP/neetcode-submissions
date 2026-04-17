class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grAnagrams: Dict[str, List[str]] = {}

        for s in strs:
            sortedStrs = ''.join(sorted(s))

            if sortedStrs in grAnagrams:
                grAnagrams[sortedStrs].append(s)
            else:
                grAnagrams[sortedStrs] = [s]
            
        return list(grAnagrams.values())
        
