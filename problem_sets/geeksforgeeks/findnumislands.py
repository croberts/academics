"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. 
For example, the below matrix contains 5 islands
Example: 
 

Input : mat[][] = {{1, 1, 0, 0, 0},
           {0, 1, 0, 0, 1},
           {1, 0, 0, 1, 1},
           {0, 0, 0, 0, 0},
           {1, 0, 1, 0, 1}}
Output : 5
This is a variation of the standard problem: “Counting the number of connected components in an undirected graph”. 
 
Before we go to the problem, let us understand what is a connected component. 
A connected component of an undirected graph is a subgraph in which every two vertices are connected to each other by a path(s),
 and which is connected to no other vertices outside the subgraph. 
For example, the graph shown below has three connected components. 

A graph where all vertices are connected with each other has exactly one connected component, consisting of the whole graph. 
Such a graph with only one connected component is called a Strongly Connected Graph.
The problem can be easily solved by applying DFS() on each component. In each DFS() call, a component or a sub-graph is visited.
 We will call DFS on the next un-visited component. The number of calls to DFS() gives the number of connected components.
  BFS can also be used.
What is an island? 
A group of connected 1s forms an island. For example, the below matrix contains 4 islands
 
https://www.geeksforgeeks.org/find-number-of-islands/
"""

"""
Plan A: Brute Force

Assumptions:
+ Doesn't wrap

- Build the graph based on input.
  a. get edges now or in another loop?
    now = n*9
    later = n^2
    -> now.
  
- Choose a root node, pref 0,0.
- Call DFS on each component



"""

class Graph: 
  visited = []
  subgraphs = None

  def __init__(self, graph):
    for row_index, row_value in enumerate(graph):
      for col_index, cell_value in enumerate(row_value):
        if cell_value == 1:
          cell_value = self.get_adjacent_list(graph, row_index, col_index)

          print(row_index, col_index, cell_value)
    print(graph)
  
  def get_adjacent_list(self, graph, row_index, col_index):
    adjacent = []
    for i in range(-1, 2):
      for j in range(-1, 2):
        try:
          if i + row_index != -1 and j + col_index != -1 and [i,j] != [0,0]:
            if graph[row_index + i][col_index + j] == 1:
              adjacent.append([row_index + i, col_index + j])
        except IndexError:
          pass
    return adjacent
  
  def dfs():
    root = None


  class Node:
    adjacent = []

  #def numIslands(self, grid):
  #  pass 

graph_1 = [
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [1, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1]
]

from pprint import pprint
pprint(graph_1)
  
g = Graph(graph_1)

