'''
#6 Max Points On A Line
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Created on 2014.9.10
@author: valthonis

A nlgn solution for this problem
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
        maxLines = []
        for point in points:
            slopeList = sorted([self.slope(point, otherPoint) for otherPoint in points if otherPoint is not point])
            maxLines.append(self.MaxLine(slopeList))
        return max(maxLines)
    
    def MaxLine(self, slopeList):
        # Given a sorted list of slopes, choose max points on a line
        maxPoints = 0
        count = 0
        prevSlope = 'not begin'
        samePoints = 0
        for slope in slopeList:
            # handle same points with this points
            if slope == -float('inf'):
                samePoints += 1
                continue
            # init prevSlope and count        
            if prevSlope == 'not begin':
                prevSlope = slope
                count = 1
            # maxPoints is to store max num of points on one line, 
            # count is to store present num of points on present line
            else:
                if self.slopeEqual(slope, prevSlope):
                    count += 1
                else:
                    maxPoints = count if count > maxPoints else maxPoints
                    prevSlope = slope
                    count = 1
        else:
            maxPoints = count if count > maxPoints else maxPoints
        return maxPoints + 1 + samePoints
                    
        
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
    
    def slopeEqual(self, slopeA, slopeB):
        if slopeA == slopeB:
            return True
        return abs(slopeA - slopeB) < 0.000001
    
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
