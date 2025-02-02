from typing import List, Set
from elem import *
from event import *
from collections import  deque
import random
from utils import *

# TODO: get flood/disease parameters from AI
class Simulation:
    def __init__(self, grid: List[List["Cell"]], disease: Disease, flood: Flood):
        self.grid = grid
        self.decay = 5

        self.disease = disease
        self.flood = flood

    def simulate(self):
        for row in self.grid:
            for cell in row:
                for elem in cell.elems:
                    elem.step()

    # a flood must start from one of the edges of the grid
    def start_flood(self):
        print("flooding")

        ix, iy = self.flood.source
        if ix != 0 and iy != 0 and ix != len(self.grid) - 1 and iy != len(self.grid[0]) - 1:
            raise ValueError("Start must be on the edge of the grid")
        queue = deque([self.flood.source])
        visited = set([self.flood.source])
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

    def drought(self, drought: "Drought"):
        print("droughting")
        for row in self.grid:
            for cell in row:
                cell.dry()
    

    def heat_wave(self, heat: "HeatWave"):
        print("heating")
        if heat.offset < 3:
            heat.offset += 1
            return
        for row in self.grid:
            for cell in row:
                if cell.crop:
                    cell.crop.hydration -= heat.temperature / self.decay
        return
    
    def cold_snap(self, cold: "ColdSnap"):
        print("cooling")
        for row in self.grid:
            for cell in row:
                if cell.crop:
                    cell.crop.hydration -= abs(cold.temperature) / self.decay
        return
    
    # a disease can start from any of the crops, each with probability p
    # runs one time step of the disease simulation
    def start_disease(self):
        print("diseasing")
        
        n, m = len(self.grid), len(self.grid[0])
        # initialize queue with all currently infected crops (healthy_threshold < health < disease_threshold)
        queue = deque(
            [(x, y) for x in range(n) for y in range(m) 
             if self.grid[x][y].crop and self.grid[x][y].crop.health > self.disease.healthy_threshold
            ]
        )
        
        print("All infected (and not dead) crops", queue)

        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        new_infections = deque()
        while queue:
            x, y = queue.popleft()  # Process an infected crop

            # Spread to neighbors
            for dx, dy in ds:
                nx, ny = x + dx, y + dy
                if 0 < nx or nx >= n or 0 < ny or ny >= m:
                    continue
                if self.grid[nx][ny].wall or self.grid[nx][ny].fence:
                    continue
                if self.grid[nx][ny].crop.health < self.disease.healthy_threshold:  # if not infected already
                    D = self.disease.diffusion_coeff
                    # only diffuse from more infected to less infected
                    health_current = self.grid[x][y].crop.health
                    health_neighbour = self.grid[nx][ny].crop.health
                    diffusion_effect = D * abs(health_current - health_neighbour)

                    if health_current > health_neighbour:  # Spread from x,y → nx,ny
                        self.grid[nx][ny].crop.health += diffusion_effect # neighbour gets infected more
                    else: # Spread from nx,ny → x, y
                        self.grid[x][y].crop.health += diffusion_effect  

                    # if newly infected, add to queue
                    if self.grid[nx][ny].crop.health > 0 and (nx, ny) not in queue and (nx, ny) not in new_infections:
                        new_infections.append((nx, ny))
                        
            
                    # mark crop as dead if infection reaches 1
                    if self.grid[x][y].crop.health >= self.disease.disease_threshold:
                        self.grid[x][y].crop.health = 1  # cap infection
                        self.grid[x][y].crop.alive = False
        
        # allow crops to be randomly infected (e.g. from bats) if not already
        for x in range(n):
            for y in range(m):
                if self.grid[x][y].crop:
                    if self.grid[x][y].crop.health < self.disease.healthy_threshold:
                        if random.random() < self.disease.infection_p:
                            self.grid[x][y].crop.sicken() # TODO: another parameter

    
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