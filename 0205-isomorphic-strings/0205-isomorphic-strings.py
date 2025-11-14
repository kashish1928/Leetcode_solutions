class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for i in range(len(s)):
            self.countHash(s[i],s_hash)
            self.countHash(t[i],t_hash)
            s_list = list(s_hash.values())
            t_list = list(t_hash.values())
            if(s_list != t_list):
                return False
        return True
    
    def countHash(self, char, hash_):
        if(char not in hash_):
            hash_[char] = 1
        else:
            hash_[char]+=1