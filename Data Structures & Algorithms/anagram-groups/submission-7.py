from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            value = s
            if key not in myMap:
                myMap[key] = []
            myMap[key].append(value)
        return list(myMap.values())