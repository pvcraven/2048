import pytest
from __init__ import create_board
from __init__ import score_grid
from __init__ import spawn_number
from __init__ import slide_right


def test_creation():
    with pytest.raises(ValueError):
        create_board(0)

    with pytest.raises(ValueError):
        create_board(-1)

    size = 4
    grid = create_board(size)
    assert grid is not None
    assert len(grid) == size
    assert len(grid[0]) == size

    size = 10
    grid = create_board(size)
    assert grid is not None
    assert len(grid) == size
    assert len(grid[0]) == size


def test_spawn_number():
    # Create our board and make sure it starts with zero score
    size = 4
    grid = create_board(size)
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
    grid = create_board(size)
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
