class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        left , right = 0 , len(heights) - 1
        currArea , maxArea = 0 , 0

        while left < right:
            width = right - left
            hht = min(heights[left] , heights[right])         #considering min height because the water should not overflow 

            currArea = width * hht

            maxArea = max(maxArea, currArea)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
        
        return maxArea
        