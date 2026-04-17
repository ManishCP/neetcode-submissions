class Solution:
    def isValid(self, s: str) -> bool:
        stackReader = []

        for string in s:
            match string:
                case "(":
                    stackReader.append("(")
                case "{":
                    stackReader.append("{")
                case "[":
                    stackReader.append("[")
                case ")":
                    if not stackReader or stackReader.pop() != "(":
                        return False
                case "}":
                    if not stackReader or stackReader.pop() != "{":
                        return False 
                case "]":
                    if not stackReader or stackReader.pop() != "[":
                        return False
        
        return not stackReader  # stack should be empty if valid
