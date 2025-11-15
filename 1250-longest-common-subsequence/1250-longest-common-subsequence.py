class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
             a b c d e
            0 0 0 0 0 0
        a   0 1 1 1 1 1
        c   0 1 1 2 2 2
        e   0 1 1 2 2 3
        """
        ans = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if(text1[i-1] == text2[j-1]):
                    ans[j][i] = ans[j-1][i-1] + 1
                else:
                    ans[j][i] = max(ans[j][i-1],ans[j-1][i])
        return ans[-1][-1]