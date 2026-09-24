class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx_map = {}

        for i, num in enumerate(nums):
            remaining = target - num 
            if remaining in idx_map:
                return [idx_map[remaining], i]
            
            idx_map[num] = i