"""
GUI for 2048 Clone

Paul Vincent Craven
"""

# Required libraries
import math
import random
import arcade

# Import image tools used to create our tiles
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from typing import List

# Functions for manipulating the grid
from grid_functions import create_grid
from grid_functions import spawn_number
from grid_functions import slide_down
from grid_functions import slide_left
from grid_functions import slide_right
from grid_functions import slide_up
from grid_functions import print_grid

# Colors
BACKGROUND_COLOR = 119, 110, 101
EMPTY_CELL = 205, 193, 180
TEXT_COLOR_DARK = 119, 110, 101
TEXT_COLOR_LIGHT = 249, 246, 242
SQUARE_COLORS = (205, 193, 180), \
                (238, 228, 218), \
                (237, 224, 200), \
                (242, 177, 121), \
                (245, 149, 99), \
                (246, 124, 95), \
                (246, 94, 59), \
                (237, 207, 114), \
                (237, 204, 97), \
                (237, 200, 80), \
                (237, 197, 63), \
                (237, 194, 46), \
                (62, 57, 51)

# Sizes
BOARD_SIZE = 4
SQUARE_SIZE = 150
MARGIN = 10
TEXT_SIZE = 50
WINDOW_WIDTH = BOARD_SIZE * (SQUARE_SIZE + MARGIN) + MARGIN
WINDOW_HEIGHT = BOARD_SIZE * (SQUARE_SIZE + MARGIN) + MARGIN

# Font
FONT = "arial.ttf"


def create_textures() -> List:
    """
    Create a series of images that will be used for each tile in the game.
    :return: List if images
    """
    texture_list = []

    width = SQUARE_SIZE
    height = SQUARE_SIZE

    img = Image.new('RGB', (SQUARE_SIZE, SQUARE_SIZE), color=SQUARE_COLORS[0])
    texture = arcade.Texture("0", img)
    texture_list.append(texture)

    i = 2
    i2 = 1
    while i <= 2048:
        img = Image.new('RGB', (SQUARE_SIZE, SQUARE_SIZE), color=SQUARE_COLORS[i2])
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT, TEXT_SIZE)
        text = f"{i}"
        text_w, text_h = d.textsize(text, font)
        x = width - width / 2 - text_w / 2
        y = height - height / 2 - text_h / 2
        if i <= 8:
            color = TEXT_COLOR_DARK
        else:
            color = TEXT_COLOR_LIGHT
        d.text((x, y), text, fill=color, font=font)
        texture = arcade.Texture(f"{i}", img)
        texture_list.append(texture)
        i *= 2
        i2 += 1

    return texture_list


def create_grid_sprites() -> arcade.SpriteList:
    """
    Return a SpriteList of Sprites to go on the screen.
    :return:
    """

    my_sprite_grid = arcade.SpriteList()
    width = SQUARE_SIZE
    height = SQUARE_SIZE

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):

            my_sprite = arcade.Sprite()

            my_sprite.center_x = column * (width + MARGIN) + width / 2 + MARGIN
            my_sprite.center_y = (BOARD_SIZE - row - 1) * (height + MARGIN) + height / 2 + MARGIN

            my_sprite_grid.append(my_sprite)

    return my_sprite_grid


def update_grid_textures(grid: List,
                         sprite_list: arcade.SpriteList,
                         texture_list: List):
    """
    Takes each Sprite in the SpriteList and flips its texture to the appropriate
    one depending on the backing grid.
    :param grid:
    :param sprite_list:
    :param texture_list:
    :return:
    """
    for row_no in range(len(grid)):
        for column_no in range(len(grid[0])):
            if grid[row_no][column_no] == 0:
                index = 0
            else:
                index = int(math.log2(grid[row_no][column_no]))

            loc = row_no * len(grid) + column_no
            # print(f"{row_no} {column_no} => {loc} = {grid[row_no][column_no]}")
            sprite_list[loc].texture = texture_list[index]


class MyGame(arcade.Window):
    """
    Main Game Class
    """
    def __init__(self):
        """
        Initializer for MyGame
        """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "2048")
        self.my_grid_sprites = None
        self.my_textures = None
        self.my_grid = None

        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        """
        Set the game up for play. Call this to reset the game.
        :return:
        """
        self.my_grid_sprites = create_grid_sprites()
        self.my_textures = create_textures()
        self.my_grid = create_grid(BOARD_SIZE)

        self.spawn()
        print_grid(self.my_grid)

        update_grid_textures(self.my_grid, self.my_grid_sprites, self.my_textures)

    def spawn(self):
        """
        Spawn a new number on the grid. 90% of the time it will be a 2, 10%
        of the time a 4.
        :return:
        """
        if random.random() <= 0.1:
            number = 4
        else:
            number = 2
        spawn_number(self.my_grid, number)

    def on_draw(self):
        """
        Draw the grid
        :return:
        """
        arcade.start_render()
        self.my_grid_sprites.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        """
        User I/O
        :param symbol:
        :param modifiers:
        :return:
        """
        success = False
        if symbol == arcade.key.LEFT:
            success = slide_left(self.my_grid)
        elif symbol == arcade.key.RIGHT:
            success = slide_right(self.my_grid)
        elif symbol == arcade.key.UP:
            success = slide_up(self.my_grid)
        elif symbol == arcade.key.DOWN:
            success = slide_down(self.my_grid)

        if success:
            print("\nSLIDE")
            print_grid(self.my_grid)
            print("\nSPAWN")
            self.spawn()
            print_grid(self.my_grid)

            update_grid_textures(self.my_grid, self.my_grid_sprites, self.my_textures)
