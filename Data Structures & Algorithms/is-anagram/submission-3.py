class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = set()
        for l in s:
            letters.add(l)

        for m in t:
            if (m not in letters) and (len(s) == len(t)):
                return False
        return True