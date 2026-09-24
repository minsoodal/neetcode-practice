class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Using Hash Set
        # (1) Beginning numbers - only if no number before it
        # (2) No duplicates
        # (3) Comparison using max -> iterative updates

        nSet = set(nums) # (2)
        longest = 0

        for num in nSet:
            if (num - 1) not in nSet: # (1) num becomes the beginning
                length = 0 
                while (num + length) in nSet: # if num+1 exists
                    length += 1
                
                longest = max(longest, length)
        
        return longest
