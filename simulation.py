from typing import List, Set
from elem import *
from event import *
from collections import  deque


def print_grid(grid: List[List["Cell"]]):
    for row in grid:
        for cell in row:
            if cell.wall:
                print("W", end="")
            elif cell.fence:
                print("F", end="")
            elif cell.crop:
                if cell.crop.alive:
                    print("C", end="")
                else:
                    print("X", end="")
            else:
                print(" ", end="")
        print()
    print()


class Simulation:
    def __init__(self, grid: List[List["Cell"]]):
        self.grid = grid

    def simulate(self):
                
        for row in self.grid:
            for cell in row:
                for elem in cell.elems:
                    elem.step()

    def flood(self, start: Tuple[int, int]):
        print("flooding")
        ix, iy = start
        if ix != 0 and iy != 0 and ix != len(self.grid) - 1 and iy != len(self.grid[0]) - 1:
            raise ValueError("Start must be on the edge of the grid")
        queue = deque([start])
        visited = set()
        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            visited.add((x, y))
            if self.grid[x][y].fence or self.grid[x][y].wall:
                continue
            self.grid[x][y].flood()
            for dx, dy in ds:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]):
                    if (nx, ny) in visited:
                        continue
                    queue.append((nx, ny))
                    
class Cell:
    def __init__(self, 
                 wall: "Wall" = None, 
                 fence: "Fence" = None, 
                 crop: "Crop" = None,
                 water_logged: bool = False):
        self.wall = wall
        self.fence = fence
        self.crop = crop
        self.water_logged = water_logged
        return

    def step_all(self):
        if self.wall:
            self.wall.step()
        if self.fence:
            self.fence.step()
        if self.crop:
            self.crop.step()
        return
    
    def flood(self):
        if self.crop:
            self.crop.alive = False