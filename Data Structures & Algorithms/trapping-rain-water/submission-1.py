class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
            
        res = 0
        l, r = 0, len(height)-1 
        leftMax, rightMax = height[l], height[r]
        # (1) if the l/r element == 0 -> skip 
        # (2) if l height < r height, then l += 1, leftmax = max(leftmax, l height) res = (leftmax - height[l])

        while l < r:
            if leftMax < rightMax:
                l += 1 
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1 
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res

