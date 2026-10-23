class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) -1
        ar = 0
        while l<r:
            # since width will always be following this formula keep it to this
            w = r-l
            
            if heights[l] <= heights[r]:
                h = heights[l]
                a = w* h
                if a > ar:
                    ar = a
                l+=1

            elif heights[l] > heights[r]:
                h = heights[r]
                a = w* h
                if a > ar:
                    ar = a
                r-=1


        return ar


                 