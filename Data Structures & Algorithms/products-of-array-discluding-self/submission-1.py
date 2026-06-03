import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if zerocnt is greater than 1, all are zero
        prod, zc = 1, 0
        for num in nums:
            if num == 0:
                zc += 1
            else:
                prod *= num
        if zc > 1:
            return [0] * len(nums)
        res = [0] * len(nums)
        for i in range(len(nums)):
            if zc:
                res[i] = prod
                if nums[i]:
                    res[i] = 0
            else:
                res[i] = prod // nums[i]
        return res
            
            