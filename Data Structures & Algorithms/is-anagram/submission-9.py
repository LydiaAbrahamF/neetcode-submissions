class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = set()
        if len(s) == len(t):
            for l in s:
                letters.add(l)
            for m in t:
                if m not in letters:
                    return False
            return True
        return False