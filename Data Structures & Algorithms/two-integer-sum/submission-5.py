class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       mymap = dict()

       for i, num in enumerate(nums):
            diff = target - num
            if diff in mymap:
                return [mymap[diff], i]
            else:
                mymap[num] = i
        
               

