class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                
        # nums = [1,2,3,4]
        # Logic = [Prefix Multiple before i] x [Postfix Multiple after i]

        res = [1] * len(nums) 

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] # from the beginning
        # -> res =  [1, 1, 2, 6]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i] # from the end

        return res

