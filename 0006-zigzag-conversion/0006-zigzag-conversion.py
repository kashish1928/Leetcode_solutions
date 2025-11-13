class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1 or numRows >= len(s)):
            return s
        
        l = [[] for i in range(numRows)]
        idx,d = 0,1
        for char in s:
            l[idx].append(char)
            if(idx == 0):
                d = 1
            if(idx == numRows-1):
                d=-1
            idx+=d
        for i in range(numRows):
            l[i] = "".join(l[i])
        return "".join(l)