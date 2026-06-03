from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        myMap = defaultdict(list)
        for s in strs:
            myMap[str(sorted(s))].append(s)
        return list(myMap.values())