import pytest

from grid_functions import create_grid
from grid_functions import score_grid
from grid_functions import spawn_number
from grid_functions import slide_right
from grid_functions import slide_left
from grid_functions import slide_down
from grid_functions import slide_up


def test_creation():
    with pytest.raises(ValueError):
        create_grid(0)

    with pytest.raises(ValueError):
        create_grid(-1)

    size = 4
    grid = create_grid(size)
    assert grid is not None
    assert len(grid) == size
    assert len(grid[0]) == size

    size = 10
    grid = create_grid(size)
    assert grid is not None
    assert len(grid) == size
    assert len(grid[0]) == size


def test_spawn_number():
    # Create our board and make sure it starts with zero score
    size = 4
    grid = create_grid(size)
    assert score_grid(grid) == 0

    # Spawn a number for each grid location
    for i in range(4 * 4):
        success = spawn_number(grid, 2)
        assert success
        assert score_grid(grid) == i * 2 + 2

    # All grid locations should be full,
    # make sure we can't spawn anything
    success = spawn_number(grid, 2)
    assert not success


def test_slide_right():
    # Create our board and make sure it starts with zero score
    size = 4
    grid = create_grid(size)
    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 0, 0, 2]

    changed = slide_right(grid)
    assert not changed
    assert grid[0] == [0, 0, 0, 2]

    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 0, 0, 4]

    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 0, 2, 4]

    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 0, 4, 4]

    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 0, 2, 8]

    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 0, 4, 8]

    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 2, 4, 8]

    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 4, 4, 8]

    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 2, 8, 8]

    grid[0][0] = 2
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 0, 4, 16]

    grid = [[0, 4, 4, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 0, 4, 8]

    grid = [[0, 8, 4, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    changed = slide_right(grid)
    assert changed
    assert grid[0] == [0, 0, 8, 8]


def test_slide_left():
    # Create our board and make sure it starts with zero score
    size = 4
    grid = create_grid(size)
    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [2, 0, 0, 0]

    changed = slide_left(grid)
    assert not changed
    assert grid[0] == [2, 0, 0, 0]

    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [4, 0, 0, 0]

    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [4, 2, 0, 0]

    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [4, 4, 0, 0]

    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [8, 2, 0, 0]

    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [8, 4, 0, 0]

    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [8, 4, 2, 0]

    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [8, 4, 4, 0]

    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [8, 8, 2, 0]

    grid[0][3] = 2
    changed = slide_left(grid)
    assert changed
    assert grid[0] == [16, 4, 0, 0]


def test_slide_down():
    # Create our board and make sure it starts with zero score
    size = 4
    grid = create_grid(size)
    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [2, 0, 0, 0]]

    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [4, 0, 0, 0]]

    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [2, 0, 0, 0],
                    [4, 0, 0, 0]]

    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [4, 0, 0, 0],
                    [4, 0, 0, 0]]

    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [2, 0, 0, 0],
                    [8, 0, 0, 0]]

    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [4, 0, 0, 0],
                    [8, 0, 0, 0]]

    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [2, 0, 0, 0],
                    [4, 0, 0, 0],
                    [8, 0, 0, 0]]

    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [4, 0, 0, 0],
                    [4, 0, 0, 0],
                    [8, 0, 0, 0]]

    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [2, 0, 0, 0],
                    [8, 0, 0, 0],
                    [8, 0, 0, 0]]

    grid[0][0] = 2
    changed = slide_down(grid)
    assert changed
    assert grid == [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [4, 0, 0, 0],
                    [16, 0, 0, 0]]


def test_slide_up():
    # Create our board and make sure it starts with zero score
    size = 4
    grid = create_grid(size)
    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[2, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[4, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[4, 0, 0, 0],
                    [2, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[4, 0, 0, 0],
                    [4, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[8, 0, 0, 0],
                    [2, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[8, 0, 0, 0],
                    [4, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[8, 0, 0, 0],
                    [4, 0, 0, 0],
                    [2, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[8, 0, 0, 0],
                    [4, 0, 0, 0],
                    [4, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[8, 0, 0, 0],
                    [8, 0, 0, 0],
                    [2, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid[3][0] = 2
    changed = slide_up(grid)
    assert changed
    assert grid == [[16, 0, 0, 0],
                    [4, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    grid = [[0, 0, 0, 2],
            [2, 0, 2, 4],
            [0, 0, 4, 16],
            [0, 0, 8, 2]]
    changed = slide_up(grid)
    assert changed
    assert grid == [[2, 0, 2, 2],
                    [0, 0, 4, 4],
                    [0, 0, 8, 16],
                    [0, 0, 0, 2]]
