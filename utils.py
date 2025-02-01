from typing import List, Set

def print_grid_hydration(grid):
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

def print_grid_health(grid):
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
                    print(f"{cell.crop.health:6.0f}", end="")
            else:
                print(f"{' ':>6}", end="")
        print()
    print()