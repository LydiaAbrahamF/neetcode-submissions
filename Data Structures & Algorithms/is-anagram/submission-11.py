class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = {}
        letters2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            letters1[s[i]] = 1 + letters1.get(s[i], 0)
            #{'r': 1}----> {'r' : 1+1}
            letters2[t[i]] = 1 + letters1.get(t[i], 0)

        for c in letters1:
            if letters1[c] != letters2.get(c,0):
                return False
        return True

        

