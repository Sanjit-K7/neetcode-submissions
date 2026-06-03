class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map<sorted string : list of words>
        myMap = dict()
        # list of chars to list
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if (sortedStr in myMap):
                myMap[sortedStr].append(s)
            else:
                myMap[sortedStr] = []
                myMap[sortedStr].append(s)
        toReturn = []
        for key in myMap:
            toReturn.append(myMap[key])
        return toReturn
