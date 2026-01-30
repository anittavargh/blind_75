class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        counter = 0
        n = len(grid)
        row_count = Counter(tuple(row) for row in grid) #
       
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            counter += row_count[col]
        return counter