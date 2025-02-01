from typing import List, Set
from elem import *
from event import *
from collections import  deque


def print_grid(grid: List[List["Cell"]]):
    for row in grid:
        for cell in row:
            if cell.wall:
                # Let's make walls occupy the same width
                print(f"{'W':>6}", end="")
            elif cell.fence:
                print(f"{'F':>6}", end="")
            elif cell.crop:
                # If HP is <= 0, print "X" right-aligned in 6 chars
                if cell.crop.is_dead():
                    print(f"{'X':>6}", end="")
                else:
                    # Otherwise print HP in 6 chars, two decimals, right-aligned
                    print(f"{cell.crop.hydration:6.0f}", end="")
            else:
                print(f"{' ':>6}", end="")
        print()
    print()



class Simulation:
    def __init__(self, grid: List[List["Cell"]]):
        self.grid = grid
        self.decay = 5
        self.events = []


    def simulate(self):
        for row in self.grid:
            for cell in row:
                for elem in cell.elems:
                    elem.step()

    def flood(self, flood: "Flood"):
        print("flooding")

        ix, iy = flood.source
        if ix != 0 and iy != 0 and ix != len(self.grid) - 1 and iy != len(self.grid[0]) - 1:
            raise ValueError("Start must be on the edge of the grid")
        queue = deque([flood.source])
        visited = set([flood.source])
        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            if self.grid[x][y].fence or self.grid[x][y].wall:
                continue
            self.grid[x][y].flood()
            for dx, dy in ds:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]):
                    if (nx, ny) in visited:
                        continue
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        self.simulated_event(flood)

    def drought(self, drought: "Drought"):
        print("droughting")
        for row in self.grid:
            for cell in row:
                cell.dry()
        self.simulated_event(drought)
    

    def heat_wave(self, heat: "HeatWave"):
        print("heating")
        if heat.offset < 3:
            heat.offset += 1
            return
        for row in self.grid:
            for cell in row:
                if cell.crop:
                    cell.crop.hydration -= heat.temperature / self.decay
        self.simulated_event(heat)
        return
    
    def cold_snap(self, cold: "ColdSnap"):
        print("cooling")
        for row in self.grid:
            for cell in row:
                if cell.crop:
                    cell.crop.hydration -= abs(cold.temperature) / self.decay
        self.simulated_event(cold)
        return

    
    def simulated_event(self, event: "Event"):
        event.duration -= 1
        if event.duration == 0:
            self.events.remove(event)

    
    def add_event(self, event: "Event"):
        self.events.append(event)
    

                    
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
            self.crop.soak()
        
    def dry(self):
        if self.crop:
            self.crop.dry()