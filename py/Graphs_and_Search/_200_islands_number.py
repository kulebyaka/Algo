"""
200. Number of Islands

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""
from typing import List

class Node:
    def __init__(self, row_index, col_index):
        self.row_index = row_index
        self.col_index = col_index
    def set_val(self, grid:List[List[str]], val):
        grid[self.row_index][self.col_index] = val
    def get_val(self, grid:List[List[str]]):
        return grid[self.row_index][self.col_index]

class Solution:
    queue = []
    grid:List[List[str]]

    def get_neighbours(self, node: Node):
        neighbours = []
        if node.col_index-1>=0:
            neighbours.append(Node(node.row_index, node.col_index-1))
        if node.col_index+1<len(self.grid[0]):
            neighbours.append(Node(node.row_index, node.col_index+1))
        if node.row_index-1>=0:
            neighbours.append(Node(node.row_index-1, node.col_index))
        if node.row_index+1<len(self.grid):
            neighbours.append(Node(node.row_index+1, node.col_index))
        return neighbours

    def visit(self, n:Node):
        self.grid[n.row_index][n.col_index] = "v"

    def visited(self, n:Node):
        return self.grid[n.row_index][n.col_index] == "v"

    def bfs(self, node):  # function for BFS
        self.visit(node)
        self.queue.append(node)
        while self.queue:
            current_node = self.queue.pop(0)
            for n in self.get_neighbours(current_node):
                if (not self.visited(n)) and (n.get_val(self.grid)=="1"):
                    self.visit(n)
                    self.queue.append(n)


    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        res=0
        for row_index, row in enumerate(grid):
            for col_index, element in enumerate(row):
                val = self.grid[row_index][col_index]
                if val=="1":
                    res+=1
                    self.bfs(Node(row_index, col_index))
        print(self.grid)
        return res

def main():
    print("expected: 1")
    print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print("expected: 3")
    print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

if __name__ == "__main__":
    main()