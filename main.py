from elem import *
from simulation import *

# this is just for testing ↓
if __name__ == "__main__":
    walled = Cell(wall=Wall(1, 1))
    fenced = Cell(fence=Fence(1, 1))

    grid = [
            [Cell(crop=Crop(1, 1)), Cell(crop=Crop(1, 1)), walled],
            [Cell(crop=Crop(1, 1)), walled, Cell(crop=Crop(1, 1))],
            [Cell(crop=Crop(1, 1)), walled, Cell(crop=Crop(1, 1))]
    ]

    print_grid(grid)
    sim = Simulation(grid)
    for _ in range(4):
        sim.flood((0, 0))
        print_grid(grid)
        sim.drought()
        print_grid(grid)