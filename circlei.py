def create_grid(grid_data):
    """
    Creates a grid representation of the candy game.

    Args:
        grid_data: A list of lists representing the candy grid.

    Returns:
        A list of lists representing the candy grid.
    """
    grid = []
    for row in grid_data:
        grid_row = []
        for candy in row:
            grid_row.append(candy)
        grid.append(grid_row)
    return grid

def print_grid(grid):
    """
    Prints the candy grid to the console.

    Args:
        grid: A list of lists representing the candy grid.
    """
    for row in grid:
        for candy in row:
            print(candy, end=" ")
        print()

# Sample candy grid data
grid_data = [
    ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["1", "blue", "orange", "green", "blue", "purple", "yellow", "blue", "orange", "green"],
    ["2", "orange", "green", "blue", "purple", "yellow", "blue", "orange", "green", "blue"],
    ["3", "green", "blue", "purple", "yellow", "blue", "orange", "green", "blue", "purple"],
    ["4", "blue", "purple", "yellow", "blue", "orange", "green", "blue", "purple", "yellow"],
    ["5", "purple", "yellow", "blue", "orange", "green", "blue", "purple", "yellow", "blue"],
    ["6", "yellow", "blue", "orange", "green", "blue", "purple", "yellow", "blue", "orange"],
    ["7", "blue", "orange", "green", "blue", "purple", "yellow", "blue", "orange", "green"],
    ["8", "orange", "green", "blue", "purple", "yellow", "blue", "orange", "green", "blue"],
    ["9", "green", "blue", "purple", "yellow", "blue", "orange", "green", "blue"]
]