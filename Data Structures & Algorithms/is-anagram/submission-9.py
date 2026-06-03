class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram, think sort
        
        return sorted(s) == sorted(t)
        