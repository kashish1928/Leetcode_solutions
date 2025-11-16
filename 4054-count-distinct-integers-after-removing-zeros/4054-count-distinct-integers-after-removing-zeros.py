class Solution:
    def countDistinct(self, n: int) -> int:
        
        s = str(n)
        length = len(s)
        pow9 = [9**i for i in range(0,length+1)]
        result = 0

        for d in range(1,length):
            result+=pow9[d]

        for i, ch in enumerate(s):
            digit = int(ch)
            if digit == 0:
                return result
            result += (digit - 1) * pow9[length - i - 1]
        return result+1
            