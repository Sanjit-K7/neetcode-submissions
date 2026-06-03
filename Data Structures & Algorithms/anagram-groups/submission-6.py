class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # 1. map charLetterCount to list of Anagrams
       #    defaultdict handles nonexistent keys
        res = defaultdict(list)

       # 2. for the 26 constant letters, 26 0'
       #    strings are iterable by character
        for s in strs:
            count = [0] * 26
            for c in s:
                # 3. letter to index?
                # a --> 0, b -> 1, ...
                # ASCII diff char c to 'a'
                count[ord(c) - ord('a')] += 1
            # lists cant be keys --> tuple
            res[tuple(count)].append(s)
        # access values(), cast to list
        return list(res.values()) 
        # O(m * n)
            # m is #of strings
            # n is avg len of chars

        


        
