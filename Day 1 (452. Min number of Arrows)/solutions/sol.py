class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:  
        # Sorts by the second element in the tuple
        points.sort(key=lambda x: x[1])  
        arrow = 1
        end = points[0][1]
        print(end)
        
        for interval in points[1:]:
            if interval[0] > end: 
                arrow += 1
                end = interval[1]  
        return arrow

print("Arrows: ")
print(Solution.findMinArrowShots(Solution, [[1,2],[3,4],[5,6],[7,8]]))