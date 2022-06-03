
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
    pass

  def dfs(self, node):
    pass


