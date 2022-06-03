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
  def cloneGraph(self, original_root_node):
    self.clone = {}
    self.visited = defaultdict(set)

    if original_root_node is None:
      return original_root_node

    new_root_node = Node(original_root_node.val)
    self.clone[1] = new_root_node

    self.dfs(new_root_node, original_root_node)

    #print(self.visited)

    #self.print_clone()
    return self.clone[1]

  def dfs(self, new_node, original_node):
    self.visited[original_node.val] = 1
    #new_node = Node(original_node.val)
    #self.clone.append(new_node)

    for original_neighbor in original_node.neighbors:
      if not self.visited[original_neighbor.val]:

        # create a new node,
        # append it to the current node's neighbors,
        # append it to the clone,
        # visit it.
        new_neighbor = Node(original_neighbor.val)
        self.clone[original_neighbor.val] = new_neighbor
        new_node.neighbors.append(new_neighbor)

        nbrs = []
        for neighbor in new_node.neighbors:
          nbrs.append(neighbor.val)

        #print("node: ", new_node.val, nbrs)

        # traverse into the new neighbors.
        self.dfs(new_neighbor, original_neighbor)
      else:
          # append the existing node to the current node's list of neighbors.
          new_node.neighbors.append(self.clone[original_neighbor.val])

  def print_clone(self):
    for node in self.clone.values():
      nbrs = []
      for neighbor in node.neighbors:
        if neighbor:
          nbrs.append(neighbor.val)

      print("node: ", node.val, "nbrs:", nbrs)

"""
build a graph from a node ref.
if that doesnt work, and maybe eventually anyways, build a graph from an adjacency list.
"""


def build_graph(adj_list):
  graph = [Node(index + 1) for index, value in enumerate(adj_list)]
  for index, node in enumerate(graph):
    for edge in adj_list[index]:
      node.neighbors.append(graph[edge - 1])

  return graph

def print_edge_graph(g):
  for x in g:
    n = []
    for y in x.neighbors:
      n.append(y.val)
    print(x.val, ": ", n)


example_1 = [[2,4],[1,3],[2,4],[1,3]]
example_2 = [[]]
example_3 = [[2,3,4],[1,7],[1],[1,5,6,8],[4],[4],[2],[4]]
#           [[2,3,4],[1,7],[1],[1,5,6,8],[3],[3],[2],[3]]

graph_1 = build_graph(example_3)

sol = Solution()

clone = sol.cloneGraph(graph_1[0])

