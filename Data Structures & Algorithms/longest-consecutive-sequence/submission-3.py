class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        # use to check for num - 1's
        toReturn = 0
        for num in (nums):
            if ((num - 1) not in numSet):
                curr = 1
                while (num + curr) in numSet:
                    curr += 1
                if curr > toReturn:
                    toReturn = curr
        return toReturn
            

        