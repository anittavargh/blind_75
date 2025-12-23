# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row_length = len(grid)

        if row_length <= 0:
            return -1

        col_length = len(grid[0])

        fresh_orange = 0
        rotten = deque()
        minutes = 0

        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == 1:
                    fresh_orange += 1
                if grid[i][j] == 2:
                    rotten.append((i, j))

        while rotten and fresh_orange > 0:
            minutes +=1
            for _ in range(len(rotten)):
                rr, rc = rotten.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                    if(rr+dx < 0 or rr+dx >= row_length or rc+dy < 0 or rc+dy >= col_length):
                        continue
                    if grid[rr+dx][rc+dy] == 2 or grid[rr+dx][rc+dy] == 0:
                        continue
                    
                    fresh_orange -=1

                    grid[rr+dx][rc+dy] = 2

                    rotten.append((rr+dx, rc+dy))

        return minutes if fresh_orange == 0 else -1