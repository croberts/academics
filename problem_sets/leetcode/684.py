"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
 The graph is represented as an array edge_dict of length n where edge_dict[i] = [ai, bi]
  indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.


Constraints:

n == edge_dict.length
3 <= n <= 1000
edge_dict[i].length == 2
1 <= ai < bi <= edge_dict.length
ai != bi
There are no repeated edge_dict.
The given graph is connected.
"""

from collections import defaultdict

class Solution:
  visited = []

  def findRedundantConnection(self, edges):
    edge_dict = defaultdict(list)
    redundant_edges = []
    self.visited = []

    for edge in edges:
      from_node = edge[0]
      to_node = edge[1]

      if from_node in edge_dict and to_node in edge_dict:
        redundant_edges.append(edge)

      edge_dict[from_node].append(to_node)
      edge_dict[to_node].append(from_node)

    last_edge = self.try_remove(edge_dict, redundant_edges)

    #print(edge_dict)
    #print(last_edge)

    return last_edge

  def try_remove(self, edge_dict, redundant_edges):
    i = len(redundant_edges) - 1
    no_islands = False

    while i > -1:
      edge = redundant_edges[i]
      edge_dict[edge[0]].remove(edge[1])
      edge_dict[edge[1]].remove(edge[0])

      no_islands = self.dfs(edge_dict, next(iter(edge_dict)))

      if no_islands:
        return edge
      else:
          edge_dict[edge[0]].append(edge[1])
          edge_dict[edge[1]].append(edge[0])
          self.visited = []
      i -= 1

  def dfs(self, edge_dict, root_node):
    #print(edge_dict)
    #print("root: ", root_node)
    self.visited.append(root_node)

    #print(self.visited)
    for new_node in edge_dict[root_node]:
      if new_node not in self.visited:
        self.dfs(edge_dict, new_node)
    return set(self.visited) == set(edge_dict.keys())



s = Solution()

edge_dict_1 = [[1,2],[1,3],[2,3]]
edge_dict_2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
edge_dict_3 = [[1,3],[3,4],[1,5],[3,5],[2,3]]
edge_dict_4 = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]

solution = s.findRedundantConnection(edge_dict_2)
print(solution)

"""

1   3
|   |
5 - 8 -- 6 -- 2
    |
4   |
| \ |
9 - 10
|
7

Problem:
if you remove the 6-8 connection you no longer have a connected graph w/ 2.

When looking at a new problem, I'd say attack a test case w/ the complexity
you're most familiar with, + 1 level. Not max, not min. Min takes too long
exhastively to reach the highest level, and highest level may be too
complex that you don't make any progress.


Solved!

"""