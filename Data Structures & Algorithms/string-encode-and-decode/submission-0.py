class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode into string w ele and len
        toReturn = ""
        for s in strs:
            toReturn = toReturn + s + "|"
        return toReturn

    def decode(self, s: str) -> List[str]:
        toRet = []
        toAdd = ""
        for c in s:
            if c == "|":
                toRet.append(toAdd)
                toAdd = ""
            else:
                toAdd += c
        return toRet
