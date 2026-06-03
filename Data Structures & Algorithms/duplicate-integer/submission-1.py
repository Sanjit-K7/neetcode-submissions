class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = dict()
        for num in nums:
            if (num in myMap):
                return True
            myMap[num] = True
        return False