class Solution:
    def maxArea(self, height: list[int]) -> int:

        

        l_pnt = 0
        r_pnt = len(height) - 1

        max = 0

        while l_pnt < r_pnt:

            left = height[l_pnt]
            right = height[r_pnt]

            shortest_height = min(left, right)

            area = shortest_height * (r_pnt - l_pnt)

            max = area if area > max else max

            if left < right:
                l_pnt += 1
            else:
                r_pnt -= 1
        
        return max

        
