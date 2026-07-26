class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        for i in range(len(height)):
            leftMax = 0
            for j in range(i + 1):
                leftMax = max(leftMax, height[j])
            
            rightMax = 0
            for j in range(i, len(height)):
                rightMax = max(rightMax, height[j])

            water = min(leftMax, rightMax) - height[i]

            if water > 0:
                res += water
        return res
         