"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and so on.
 The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
 Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# ref code:
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import defaultdict


  class Solution:
    adj_list = []
    visited = defaultdict(int)

    #def build_graph(self, adj_list):
    #  for edge in adj_list:

    def cloneGraph(self, node):

      self.dfs(node)

      return self.adj_list

    def dfs(self, node):
      self.visited[node.val] = 1

      if node.neighbors:
        for neighbor in node.neighbors:
          if self.visited[neighbor.val]:
            edge = [node.val, neighbor.val]
            #reverse_edge = [neighbor.val, node.val]

            if edge not in self.adj_list:
              self.adj_list.append(edge)
              self.dfs(neighbor)


"""
build a graph from a node ref.
if that doesnt work, and maybe eventually anyways, build a graph from an adjacency list.
"""



#graph_1 = [[2,4],[1,3],[2,4],[1,3]]
sol = Solution()
adj_list = sol.cloneGraph(graph_1)

