from elem import *
from simulation import *
from utils import *

# this is just for testing ↓
if __name__ == "__main__":
    walled = Cell(wall=Wall(1, 1))
    fenced = Cell(fence=Fence(1, 1))

    grid = [
            [Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1, health=0.6)), Cell(crop=Crop(1, 1, 1))],
            [Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1))],
            [Cell(crop=Crop(1, 1, 1, health=0.7)), Cell(crop=Crop(1, 1, 1)), Cell(crop=Crop(1, 1, 1))]
    ]
    
    # grid = [
    #         [fenced, Cell(crop=Crop(1, 1,)), walled],
    #         [Cell(crop=Crop(1, 1)), walled, Cell(crop=Crop(1, 1))],
    #         [Cell(crop=Crop(1, 1)), walled, Cell(crop=Crop(1, 1))]
    # ]

    print_grid_health(grid)
    sim = Simulation(grid, Disease(duration=1, chance=0.15, diffusion_coeff=0.5), Flood(duration=1, source=(0, 0), chance=0.5))
    for _ in range(4):
        sim.start_disease()
        print_grid_health(grid)