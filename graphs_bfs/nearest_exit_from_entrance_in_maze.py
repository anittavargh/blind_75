from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        sr, sc = entrance

        # down, top, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        q = deque()
        q.append((sr, sc, 0))
        maze[sr][sc] = '+'

        while q:
            r, c, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr >=m or nc >= n or maze[nr][nc] == '+':
                    continue

                if nr == 0 or nc == 0 or nr == m -1 or nc == n -1:
                    return steps + 1

                maze[nr][nc] = '+'
                q.append((nr, nc, steps +1))

        return -1
    

maze = [
    ["+", "+", ".", "+"],
    [".", ".", ".", "+"],
    ["+", "+", "+", "."]
]

entrance = [1, 2]

sol = Solution()
result = sol.nearestExit(maze, entrance)

print(result)



# Time: O(m × n) — each cell visited once, 4-direction check
# Space: O(m × n) — BFS queue in worst case
