class Solution:
    def isValid(self, s: str) -> bool:
        stackReader = []
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in closeToOpen:
                if stackReader and stackReader[-1] == closeToOpen[c]:
                    stackReader.pop()
                else:
                    return False
            else:
                stackReader.append(c)
            
        return True if not stackReader else False
         