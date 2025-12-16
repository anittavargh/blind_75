class Solution(object):
    def canVisitAllRooms(self, rooms):
        vis, stack, count = [False for _ in range(len(rooms))], [0], 1
        vis[0] = 1
        while stack:
            keys = rooms[stack.pop()]
            for k in keys:
                if not vis[k]:
                    stack.append(k)
                    vis[k] = True
                    count = count + 1
        return len(rooms) == count