from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            if not stack:
                curr_area = heights[i]
                if curr_area > max_area:
                    max_area = curr_area

            ins_idx = i
            while stack and heights[i] < stack[-1][-1]:
                idx, height = stack.pop()
                ins_idx = idx
                curr_area = (i - idx) * height
                if curr_area > max_area:
                    max_area = curr_area
            stack.append((ins_idx, heights[i]))

        while stack:
            idx, height = stack.pop()
            curr_area = (len(heights) - idx) * height
            if curr_area > max_area:
                max_area = curr_area
        return max_area

sol = Solution()
heights = [2,1,5,6,2,3]
print(sol.largestRectangleArea(heights))