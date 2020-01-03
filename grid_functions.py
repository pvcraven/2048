import random

from typing import List

BOARD_SIZE = 4


def create_grid(size: int) -> List:
    if size < 1:
        raise ValueError("Grid size must be positive.")

    grid = [[0 for _ in range(size)] for _ in range(size)]
    return grid


def spawn_number(grid: List, number: int) -> bool:
    # Find empty locations
    possible_locations = []
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 0:
                location = column, row
                possible_locations.append(location)

    if len(possible_locations) == 0:
        return False

    selected_location = random.choice(possible_locations)
    column, row = selected_location
    grid[row][column] = number
    return True


def print_grid(grid: List):
    for row in grid:
        for cell in row:
            print(f"{cell:5}", end="")
        print()
    print()


def score_grid(grid: List) -> int:
    total = 0
    for row in grid:
        total += sum(row)
    return total


def slide_right(grid: List) -> bool:
    changed = False
    has_merged = False
    for row in grid:
        for column_no in range(0, len(row) - 1):
            if row[column_no] and not row[column_no + 1]:
                row[column_no + 1] = row[column_no]
                row[column_no] = 0
                changed = True
            elif row[column_no] and not has_merged and row[column_no] == row[column_no + 1]:
                # Merge
                row[column_no + 1] = row[column_no] * 2
                changed = True
                has_merged = True

                # Shift cells to the right
                c = column_no
                while c > 0:
                    row[c] = row[c - 1]
                    c -= 1
                row[0] = 0
            else:
                has_merged = False

    return changed


def slide_left(grid: List) -> bool:
    changed = False
    has_merged = False
    for row in grid:
        for column_no in range(len(row) - 1, 0, -1):
            if row[column_no] and not row[column_no - 1]:
                row[column_no - 1] = row[column_no]
                row[column_no] = 0
                changed = True
            elif row[column_no] and not has_merged and row[column_no] == row[column_no - 1]:
                # Merge
                row[column_no - 1] = row[column_no] * 2
                changed = True
                has_merged = True

                # Shift cells to the left
                c = column_no
                while c < len(row) - 1:
                    row[c] = row[c + 1]
                    c += 1
                row[len(grid) - 1] = 0
            else:
                has_merged = False

    return changed


def slide_down(grid: List) -> bool:
    changed = False
    has_merged = False
    for column_no in range(len(grid)):
        for row_no in range(1, len(grid)):
            if grid[row_no - 1][column_no] and not grid[row_no][column_no]:
                grid[row_no][column_no] = grid[row_no - 1][column_no]
                grid[row_no - 1][column_no] = 0
                changed = True
            elif grid[row_no][column_no] and not has_merged and grid[row_no][column_no] == grid[row_no - 1][column_no]:
                # Merge
                grid[row_no][column_no] = grid[row_no][column_no] * 2
                changed = True
                has_merged = True

                # Shift cells down
                r = row_no - 1
                while r > 0:
                    grid[r][column_no] = grid[r - 1][column_no]
                    r -= 1
                grid[0][column_no] = 0
            else:
                has_merged = False

    return changed


def slide_up(grid: List) -> bool:
    changed = False
    has_merged = False
    for column_no in range(len(grid)):
        for row_no in range(len(grid) - 1, 0, -1):
            if grid[row_no][column_no] and not grid[row_no - 1][column_no]:
                grid[row_no - 1][column_no] = grid[row_no][column_no]
                grid[row_no][column_no] = 0
                changed = True
            elif grid[row_no][column_no] and not has_merged and grid[row_no][column_no] == grid[row_no - 1][column_no]:
                # Merge
                grid[row_no][column_no] = grid[row_no][column_no] * 2
                changed = True
                has_merged = True

                # Shift cells down
                r = row_no
                while r < len(grid):
                    grid[r - 1][column_no] = grid[r][column_no]
                    r += 1
                grid[-1][column_no] = 0
            else:
                has_merged = False

    return changed
