'''
#6 Max Points On A Line
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Created on 2014.9.10
@author: valthonis

A n^2 solution for this problem
'''

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points:
            return 0
        if len(points) == 1:
            return 1
        maxLines = []
        for point in points:
            slopeDict = {}
            a = 0
            for otherPoint in points:
                slope = self.slope(point, otherPoint)
                if slope == 'A':
                    a += 1
                else:
                    if slope not in slopeDict:
                        slopeDict[slope] = 1
                    else:
                        slopeDict[slope] += 1
            print slopeDict
            if not slopeDict:
                maxLines.append(a)
            else:
                maxLines.append(max(slopeDict.values())+a)
        return max(maxLines)
        
    def slope(self, pointB, pointA):
        # Calculate the slope between two points
        
        # mark same points
        if pointB.x == pointA.x and pointB.y == pointA.y:
            return -float('inf')
        # mark vertical slope
        if pointB.x == pointA.x:
            return float('inf')
        # mark horizontal slope
        if pointB.y == pointA.y:
            return 0.0
        # normal situation
        return (pointA.y - pointB.y) / (pointA.x - pointB.x + 0.0)
        
if __name__ == '__main__':
#     input = [Point(tuple) for tuple in [(4,0),(4,-1),(4,5)]]
    A = Point(2, 3)
    B = Point(3, 3)
    C = Point(-5, 3)
#     D = Point(2, 2)
#     E = Point(4, -1)
#     points = [A, B, C, D, E]
    input = [A, B, C]
    Solution = Solution()
    print Solution.maxPoints(input)
