class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary (known as HashMap in other languages)
        seen = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in seen:
                return [seen[difference], index]
            seen[value] = index        
        