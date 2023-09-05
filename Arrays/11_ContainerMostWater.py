class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxnum = 0
        r = len(height)-1
        l = 0
        while(l < r):
            curArea = min(height[l], height[r]) * (r-l)
            maxnum = max(maxnum, curArea)
            
            if(height[r] < height[l]):
                r -= 1
            else:
                l+=1

        return maxnum
