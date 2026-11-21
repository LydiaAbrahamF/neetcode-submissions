class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = []
        for l in s:
            letters.append(l)
        for m in t:
            if m not in letters and len(s) == len(t):
                return False
        return True