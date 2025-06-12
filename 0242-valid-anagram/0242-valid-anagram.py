class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for x in s:
            if x not in hashmap:
                hashmap[x]=1
            else:
                hashmap[x]+=1
        for y in t:
            if y in hashmap:
                hashmap[y]-=1
            else:
                return False
        for x in hashmap:
            if hashmap[x]!=0:
                return False
        return True
        