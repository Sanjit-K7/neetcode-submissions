class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        myMap = defaultdict(int)

        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr

            if (diff in myMap):
                return [myMap[diff], i]
            
            myMap[curr] = i

        return []