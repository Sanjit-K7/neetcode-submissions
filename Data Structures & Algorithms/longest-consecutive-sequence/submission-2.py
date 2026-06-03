class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        numSet = set(nums)
        # use to check for num - 1's
        starts = []
        for num in (nums):
            if ((num - 1) not in numSet):
                starts.append(num)
        
        toReturn = 1

        for start in starts:
            s = start
            curr = 1
            while (s + 1) in numSet:
                s += 1
                curr += 1
            if curr > toReturn:
                toReturn = curr

        return toReturn

        