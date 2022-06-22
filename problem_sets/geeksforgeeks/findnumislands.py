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
This is a variation of the standard problem: “Counting the number of connected components in an undirected self.graph”. 
 
Before we go to the problem, let us understand what is a connected component. 
A connected component of an undirected self.graph is a subself.graph in which every two vertices are connected to each other by a path(s),
 and which is connected to no other vertices outside the subself.graph. 
For example, the self.graph shown below has three connected components. 

A self.graph where all vertices are connected with each other has exactly one connected component, consisting of the whole self.graph. 
Such a self.graph with only one connected component is called a Strongly Connected self.graph.
The problem can be easily solved by applying DFS() on each component. In each DFS() call, a component or a sub-self.graph is visited.
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

- Build the self.graph based on input.
  a. get edges now or in another loop?
    now = n*9
    later = n^2
    -> now.

  b. traverse nodes now? or in another loop?

  
- Choose a root node, pref 0,0.


- Call DFS on each component
"""

graph_1 = [
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [1, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1]
]

import pprint
from pprint import pprint

class Solution:

  graph = []

  def read_file(self, textfile):
    with open(textfile) as f:
      file = f.readlines()
      new_line = []
      for line in file:
          line = line.split(" ")
          for x in line:
            y = x.replace("\n", "").strip()
            if y:
              new_line.append(int(y))
          self.graph.append(new_line)
    #print(self.graph)
          

  def numIslands(self,grid):
    if self.graph == []:
      self.graph = grid
    islands = 0
    for row_index, row_value in enumerate(self.graph):
      for col_index, cell_value in enumerate(row_value):
        if cell_value == 1:
          islands += 1
          self.graph[row_index][col_index] = -1
          self.dfs(row_index, col_index)
        else:
          self.graph[row_index][col_index] = -1
    #print(self.graph)
    return islands

  def dfs(self, row_index, col_index):
    for i in range(-1, 2):
      for j in range(-1, 2):
        try:
          if i + row_index != -1 and j + col_index != -1 and [i,j] != [0,0]:
            if self.graph[row_index + i][col_index + j] == 1:
              self.graph[row_index + i][col_index + j] = -1
              self.dfs(row_index + i, col_index + j)
            else:
              self.graph[row_index + i][col_index + j] = -1
        except IndexError:
          pass

sol = Solution()
islands = sol.numIslands(graph_1)
print(islands)

sol = Solution()
grid = sol.read_file('islands.txt')
islands = sol.numIslands(grid)
print(islands)
