class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans: int = 0
        visited = set()

        for x, row in enumerate(grid):
            for y, col_element in enumerate(row):
                if(col_element and ((x,y) not in visited)):
                    area = 0
                    stack = [(x,y)]
                    visited.add((x,y))
                    while(stack):
                        area += 1
                        r, c = stack.pop()
                        # See if there's new connected places we need to consider
                        for new_row, new_col in ((r+1, c), (r-1, c), (r,c+1), (r,c-1)):
                            if((new_row >= 0)and (new_row < len(grid)) and (new_col >= 0) and
                              (new_col <len(grid[0])) and grid[new_row][new_col] and
                              ((new_row, new_col) not in visited)):
                                stack.append((new_row, new_col))
                                visited.add((new_row, new_col))
                        ans = max(ans, area)

        return(ans)



# Initial thoughts:
# - Thinking of doing a depth-first like search for a piece of land
# - Keep a variable for the current area assessment
# - Keep a variable for the max area of the island
# - Wouldn't want to make so many recursive calls that the program times out
# --> Keep track of any place in grid we've already visited
# --> Use a stack to track places we need to expand
# --> Use iterative solution instead of recursive
