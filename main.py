from elem import *
from simulation import *
from utils import *

# this is just for testing ↓
if __name__ == "__main__":
    walled = Cell(wall=Wall(1, 1))
    fenced = Cell(fence=Fence(1, 1))

#     grid = [
#             [Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1))],
#             [Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1))],
#             [Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1))]
#     ]
    
    grid = [
            [fenced, Cell(crop=Crop(1, 1)), walled],
            [Cell(crop=Crop(1, 1)), walled, Cell(crop=Crop(1, 1))],
            [Cell(crop=Crop(1, 1)), walled, Cell(crop=Crop(1, 1))]
    ]

    print_grid_health(grid)
    sim = Simulation(grid, Disease(diffusion_coeff=1), Flood(duration=1, source=(0, 0), flood_chance=0.5))
    sim.start_disease()
    print_grid_health(grid)
#     for _ in range(4):
#         sim.flood((0, 0))
#         print_grid(grid)
#         sim.drought()
#         print_grid(grid)
