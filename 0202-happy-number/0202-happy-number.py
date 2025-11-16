class Solution:
    def isHappy(self, n: int) -> bool:
        s = n
        memory = set()
        memory.add(n)
        while(s != 1):
            s = self.squareDigits(s)
            if(s not in memory):
                memory.add(s)
            else:
                return False
        return True
    
    def squareDigits(self,n:int) -> int:
        s = str(n)
        l = []
        for digit in s:
            l.append(int(digit)**2)
        return sum(l)