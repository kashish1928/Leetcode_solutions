class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        n = len(digits)
        for i in range(0,n):
            num+=digits[i]*(10**(n-1-i))
        num+=1
        strnum = str(num)
        strlst = list(strnum)
        for i in range (0,len(strlst)):
            strlst[i] = int(strlst[i])
        return strlst