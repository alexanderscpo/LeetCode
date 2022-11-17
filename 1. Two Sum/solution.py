class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}

        for i, value in enumerate(nums):
            if target - value in di:
                return [di[target - value], i]
            di[value] = i
        return []
