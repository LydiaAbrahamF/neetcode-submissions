class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = set()
        for l in s:
            if l in letters:
                return False
            letters.add(l)
        for m in t:
            if m not in letters:
                return False
        return True