import random

from typing import List


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


def compress_right(grid: List) -> bool:
    changed = False
    for row_no in range(len(grid)):
        cur_col = len(grid) - 1
        for i in range(len(grid)):
            if grid[row_no][cur_col] != 0:
                # No zero, look further left
                cur_col -= 1
            else:
                # Found a zero, shift cells to the right
                c = cur_col
                while c > 0:
                    grid[row_no][c] = grid[row_no][c - 1]
                    if grid[row_no][c]:
                        changed = True
                    c -= 1
                grid[row_no][0] = 0
    return changed


def merge_right(grid: List) -> bool:
    changed = False
    for row_no in range(len(grid)):
        for col_no in range(len(grid) - 1, 0, -1):
            if grid[row_no][col_no] != 0 and grid[row_no][col_no] == grid[row_no][col_no - 1]:
                grid[row_no][col_no] *= 2
                grid[row_no][col_no - 1] = 0
                changed = True
    return changed


def slide_right(grid: List) -> bool:
    c1 = compress_right(grid)
    c2 = merge_right(grid)
    c3 = compress_right(grid)

    return c1 or c2 or c3


def compress_left(grid: List) -> bool:
    changed = False
    for row_no in range(len(grid)):
        cur_col = 0
        for i in range(len(grid)):
            if grid[row_no][cur_col] != 0:
                # No zero, look further left
                cur_col += 1
            else:
                # Found a zero, shift cells to the right
                c = cur_col
                while c < len(grid) - 1:
                    grid[row_no][c] = grid[row_no][c + 1]
                    if grid[row_no][c]:
                        changed = True
                    c += 1
                grid[row_no][-1] = 0
    return changed


def merge_left(grid: List) -> bool:
    changed = False
    for row_no in range(len(grid)):
        for col_no in range(len(grid) - 1):
            if grid[row_no][col_no] != 0 and grid[row_no][col_no] == grid[row_no][col_no + 1]:
                grid[row_no][col_no] *= 2
                grid[row_no][col_no + 1] = 0
                changed = True
    return changed


def slide_left(grid: List) -> bool:
    c1 = compress_left(grid)
    c2 = merge_left(grid)
    c3 = compress_left(grid)

    return c1 or c2 or c3


def compress_down(grid: List) -> bool:
    changed = False
    for col_no in range(len(grid[0])):
        row_no = len(grid[0]) - 1
        for i in range(len(grid)):
            if grid[row_no][col_no] != 0:
                # No zero, look further left
                row_no -= 1
            else:
                # Found a zero, shift cells to the right
                r = row_no
                while r > 0:
                    grid[r][col_no] = grid[r - 1][col_no]
                    if grid[r][col_no]:
                        changed = True
                    r -= 1
                grid[0][col_no] = 0
    return changed


def merge_down(grid: List) -> bool:
    changed = False
    for col_no in range(len(grid)):
        for row_no in range(len(grid) - 1, 0, -1):
            if grid[row_no][col_no] != 0 and grid[row_no][col_no] == grid[row_no - 1][col_no]:
                grid[row_no][col_no] *= 2
                grid[row_no - 1][col_no] = 0
                changed = True
    return changed


def slide_down(grid: List) -> bool:
    c1 = compress_down(grid)
    c2 = merge_down(grid)
    c3 = compress_down(grid)

    return c1 or c2 or c3


def compress_up(grid: List) -> bool:
    changed = False
    for col_no in range(len(grid[0])):
        row_no = 0
        for i in range(len(grid)):
            if grid[row_no][col_no] != 0:
                # No zero, look further
                row_no += 1
            else:
                # Found a zero, shift cells
                r = row_no
                while r < len(grid) - 1:
                    grid[r][col_no] = grid[r + 1][col_no]
                    if grid[r][col_no]:
                        changed = True
                    r += 1
                grid[-1][col_no] = 0
    return changed


def merge_up(grid: List) -> bool:
    changed = False
    for col_no in range(len(grid)):
        for row_no in range(0, len(grid) - 1):
            if grid[row_no][col_no] != 0 and grid[row_no][col_no] == grid[row_no + 1][col_no]:
                grid[row_no][col_no] *= 2
                grid[row_no + 1][col_no] = 0
                changed = True
    return changed


def slide_up(grid: List) -> bool:
    c1 = compress_up(grid)
    c2 = merge_up(grid)
    c3 = compress_up(grid)

    return c1 or c2 or c3
