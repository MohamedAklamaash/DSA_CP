
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 0:
            return None
        maxLeft , maxRight = [] , []
        maxval = height[0]
        for i in height:
            if maxval < i:
                maxval = i
            maxLeft.append(maxval)
        maxval = height[-1]
        for i in range(len(height)-1,-1,-1):
            if maxval < height[i]:
                maxval = height[i]
            maxRight.append(maxval)
        maxRight.reverse()
        if len(maxLeft)!=len(maxRight):
            return # this if shouldn't happen at any cost
        out = 0
        for i in range(len(height)):
            minval = min(maxLeft[i],maxRight[i])
            if minval - height[i] > 0:
                out += minval - height[i]
        return out

