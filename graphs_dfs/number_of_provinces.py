# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.
# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Time complexity - O(n^2)
# Space complexity - O(n)

from typing import List, collections

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        graph = collections.defaultdict(list)

        if not isConnected:
            return 0

        n = len(isConnected)
        visited = [False]*n
        count = 0

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        def dfs(val):
            for i in graph[val]:
                if visited[i] == False:
                    visited[i] = True
                    dfs(i)

        for i in range(n):
            if visited[i] == False:
                count = count + 1
                visited[i] = True
                dfs(i)
        
        return count