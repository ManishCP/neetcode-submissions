class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        jam = sorted(s)
        jim = sorted(t)

        for i in range(len(s)):
            if jam[i] != jim[i]:
                return False
        
        return True
        