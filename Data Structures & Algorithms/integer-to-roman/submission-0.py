class Solution:
    def intToRoman(self, num: int) -> str:

        count = 1
        res = ""

        while num > 0:
            digit = num % 10
            if count == 1:
                one, five, ten = "I", "V", "X"
            elif count == 2:
                one, five, ten = "X", "L", "C"
            elif count == 3:
                one, five, ten = "C", "D", "M"
            else:
                one, five, ten = "M", "", ""

            if digit == 4:
                part = one + five
            elif digit == 9:
                part = one + ten
            elif digit >= 5:
                part = five + (one * (digit - 5))
            else:
                part = one * digit 
            
            res = part + res

            num //= 10
            count += 1

        return res
            

            

        