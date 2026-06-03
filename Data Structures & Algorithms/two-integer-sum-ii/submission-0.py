class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       l = 0
       r = len(numbers) - 1

       while (l <= r):
        ssum = numbers[l] + numbers[r]
        if (ssum < target):
            l += 1
            continue
        if (ssum > target):
            r -= 1
            continue
        else:
            return [l + 1, r + 1]
       return []