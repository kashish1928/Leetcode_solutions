class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat = {}
        stg = {}
        st = s.split()
        if(len(pattern) != len(st)):
            return False
            
        for i in range(len(pattern)):
            if(pattern[i] not in pat):
                pat[pattern[i]] = [i]
            else:
                pat[pattern[i]].append(i)
            if(st[i] not in stg):
                stg[st[i]] = [i]
            else:
                stg[st[i]].append(i)


        print(pat)
        print(stg)
        print(pat.values())
        print(stg.values())
        if(len(pat) != len(stg)):
            return False
        if(list(pat.values()) != list(stg.values())):
            return False
        
        return True