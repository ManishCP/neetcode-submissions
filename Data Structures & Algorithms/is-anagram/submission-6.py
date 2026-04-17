class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        jam = sorted(s)
        jim = sorted(t)

        if jam == jim:
            return True
        
        return False
        