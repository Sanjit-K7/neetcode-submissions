class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = dict()
        for i in range(len(nums)):
            cur = nums[i]
            x = target - cur
            if (x in myMap):
                return [myMap[x], i]
            myMap[cur] = i
        return []