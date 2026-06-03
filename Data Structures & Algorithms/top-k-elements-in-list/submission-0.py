class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = defaultdict(int)

        for num in nums:
            myMap[num] += 1

        # how do i make a lambda that sorts keys by their values
        # goal: sort keys into a list
        # sorted(myMap, key = lambda name: metric)
        sorted_keys = sorted(myMap, key = lambda k: -myMap[k])

        return sorted_keys[0:k]