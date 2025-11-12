class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = ""
        for i in range(len(words)-1,0,-1):
            ip = words[i] + " "
            ans+=ip
        return ans + words[0]