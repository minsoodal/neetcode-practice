class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # Time: O(nlogn) + O(n^2) -> O(n^2)
        res = []

        # First, sort the array
        # three pointers needed: a, l, r
        # O(n^2): only two loops -> for a, we loop l and r (two-sum)
        # (1) If a is already > 0, then stop (the array is all sorted)
        # (2) If a (<0) is same as the one before, then skip (no duplicate)
        # (3) then do two sum with l, r
        
        for i, a in enumerate(nums):

            if i > 0 and a == nums[i-1]: #(2)
                continue

            l, r = i + 1, len(nums)-1
            while l < r:
                threeS = a + nums[l] + nums[r]
                if threeS > 0: 
                    r -= 1 
                elif threeS < 0:
                    l += 1 
                else:
                    res.append([a, nums[l], nums[r]])
                    # Update the pointers
                    # [-2, -2, 0, 0, 2, 2]
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r: # (2) duplicates
                        l += 1
            
        return res




