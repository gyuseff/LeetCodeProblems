# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# Status: Accepted and beats 37%

# Problem statement: There is a rectangular island that is connected to the Pacific Ocean in the north and west; and with the Atlantic Ocean east and south.
# The island is divided into a grid of square cells, and each of this has a height. 
# If it rains in one of these squares, water flows from to adjacent squares if their heights are less or equal to the current. And it propagates until it no longer can or if it reaches an ocean
# Given the heights matrix, return a list of coordinates where if it rains in one of these squares, it reaches both oceans

#My solution: My solution states running Depth-First-Search twice and taking into account previous information gathered.
#First we create a set with the tiles that flows into the Pacific (north/west borders) and one that flows into the Atlantic (east/south borders)

#The first DFS checks if a tile flows into the pacific, we create a stack with the north/west borders.
#In each iteration, take the first element of the stack, check each neighbour, if the height of the neighbour is greater or equal, then that neighbour flows into the pacific; add it to the set and the stack if it was not already in them and continue until the stack is empty.

#Then we do the same in the second DFS with the ones that flows into the Atlantic, however in each iteration we also check if the tile is in the pacific set; if so we add it to the output

class Solution:
    
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m : int = len(heights)
        n : int = len(heights[0])

        floods_into_pacific : set[tuple[int,int]] = {(x,y) for x in range(m) for y in range(n) if x == 0 or y == 0}
        floods_into_atlantic : set[tuple[int,int]] = {(x,y) for x in range(m) for y in range(n) if x == m-1 or y == n-1}

        def valid_coordinate(node: tuple[int,int]) -> bool:
            x = node[0]
            y = node[1]
            if x < 0 or x > m-1 or y < 0 or y > n-1:
                return False
            return True

        def DFS_1() -> None:
            visited : set[tuple[int,int]] = set()
            stack : list[tuple[int,int]] = list(floods_into_pacific)

            while stack:
                current_node : tuple[int,int]= stack.pop()
                if current_node not in visited:
                    visited.add(current_node)
                    current_x : int= current_node[0]
                    current_y : int= current_node[1]

                    candidates : list[tuple[int,int]] = [(current_x - 1, current_y), (current_x + 1, current_y), (current_x, current_y - 1), (current_x, current_y + 1) ]

                    for c in candidates:
                        if valid_coordinate(c) and c not in visited:
                            if heights[current_x][current_y] <= heights[c[0]][c[1]]:
                                stack.append(c)
                                floods_into_pacific.add(c)
        
        DFS_1()

        output : list[list[int]] = []

        def DFS_2() -> None:
            visited : set[tuple[int,int]] = set()
            stack : list[tuple[int,int]] = list(floods_into_atlantic)

            while stack:
                current_node : tuple[int,int]= stack.pop()
                if current_node not in visited:
                    visited.add(current_node)
                    current_x : int= current_node[0]
                    current_y : int= current_node[1]

                    if current_node in floods_into_pacific:
                        output.append(list(current_node))

                    candidates : list[tuple[int,int]] = [(current_x - 1, current_y), (current_x + 1, current_y), (current_x, current_y - 1), (current_x, current_y + 1) ]

                    for c in candidates:
                        if valid_coordinate(c) and c not in visited:
                            if heights[current_x][current_y] <= heights[c[0]][c[1]]:
                                stack.append(c)
                                floods_into_atlantic.add(c)
                            
            
        DFS_2()
    
        return output
                            
    """
    def _pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m : int = len(heights)
        n : int = len(heights[0])

        floods_into_pacific : set[tuple[int,int]] = {(x,y) for x in range(m) for y in range(n) if x == 0 or y == 0}
        floods_into_atlantic : set[tuple[int,int]] = {(x,y) for x in range(m) for y in range(n) if x == m-1 or y == n-1}

        def valid_coordinate(node: tuple[int,int]) -> bool:
            x = node[0]
            y = node[1]
            if x < 0 or x > m-1 or y < 0 or y > n-1:
                return False
            return True

        def DFS_pacific_atlantic(start_node: tuple[int,int], ocean: set[tuple[int,int]]) -> None:
            visited : set[tuple[int,int]] = {start_node}
            stack : list[tuple[int,int]] = [start_node]

            while stack:
                current_node : tuple[int,int]= stack.pop()
                if current_node in ocean:
                    ocean.add(start_node)
                    return
                else:
                    current_x : int= current_node[0]
                    current_y : int= current_node[1]

                    candidates : list[tuple[int,int]] = [(current_x - 1, current_y), (current_x + 1, current_y), (current_x, current_y - 1), (current_x, current_y + 1) ]

                    for c in candidates:
                        if valid_coordinate(c) and c not in visited:
                            if heights[current_x][current_y] >= heights[c[0]][c[1]]:
                                stack.append(c)
                                visited.add(c)
                                
        for i in range(0, m):
            for j in range(0, n):
                DFS_pacific_atlantic((i,j), floods_into_pacific)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == 1 and j == 3:
                    pass
                DFS_pacific_atlantic((i,j), floods_into_atlantic)
        
        output : list[list[int]] = []

        for sq in floods_into_atlantic:
            if sq in floods_into_pacific:
                output.append(list(sq))
            
        return sorted(output, key=lambda x: x[0])
    """



if __name__ == "__main__":
    testcase_1: list[list[int]] = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    testcase_2 : list[list[int]] = [[1]]

    testcases : list[list[list[int]]] = [testcase_1, testcase_2]

    for ts in testcases:
        print(Solution.pacificAtlantic(self=None, heights=ts))