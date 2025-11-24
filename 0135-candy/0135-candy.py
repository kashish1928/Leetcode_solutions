class Solution:
    def candy(self, ratings: List[int]) -> int:
        if(len(ratings) == 1):
            return 1
        candies = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if(ratings[i-1] < ratings[i]):
                candies[i] = candies[i-1]+1
        for i in range(len(ratings) - 2, -1, -1):
            if (ratings[i+1] < ratings[i]):
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)