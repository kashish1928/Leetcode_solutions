class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_sorted = sorted(citations, reverse=True)
        h = 0
        for i in range(0,len(citations)):
            if(citations_sorted[i]>=i+1):
                h = i+1
        return h