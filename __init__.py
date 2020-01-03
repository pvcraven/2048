from grid_functions import create_grid
from grid_functions import spawn_number
from grid_functions import slide_down
from grid_functions import slide_left
from grid_functions import slide_right
from grid_functions import slide_up
from grid_functions import print_grid
from grid_functions import BOARD_SIZE

import PIL

import math
import arcade
import random

SQUARE_COLOR = (73, 109, 137)
SQUARE_SIZE = (150, 150)
MARGIN = 10
TEXT_SIZE = 30

def create_textures():
    texture_list = []

    width = SQUARE_SIZE[0]
    height = SQUARE_SIZE[1]

    img = PIL.Image.new('RGB', SQUARE_SIZE, color=SQUARE_COLOR)
    texture = arcade.Texture("0", img)
    texture_list.append(texture)

    i = 2
    while i <= 2048:
        img = PIL.Image.new('RGB', SQUARE_SIZE, color=SQUARE_COLOR)
        d = PIL.ImageDraw.Draw(img)
        font = PIL.ImageFont.truetype("arial.ttf", TEXT_SIZE)
        text = f"{i}"
        text_w, text_h = d.textsize(text, font)
        x = width - width / 2 - text_w / 2
        y = height - height / 2 - text_h / 2
        d.text((x, y), text, fill=(255, 255, 0), font=font)
        texture = arcade.Texture(f"{i}", img)
        texture_list.append(texture)
        i *= 2

    return texture_list


def create_grid_sprites():

    my_sprite_grid = arcade.SpriteList()
    width = SQUARE_SIZE[0]
    height = SQUARE_SIZE[1]

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):

            my_sprite = arcade.Sprite()

            my_sprite.center_x = column * (width + MARGIN) + width / 2 + MARGIN
            my_sprite.center_y = (BOARD_SIZE - row) * (height + MARGIN) + height / 2 - MARGIN

            my_sprite_grid.append(my_sprite)


    return my_sprite_grid


def update_grid_textures(grid, sprite_list, texture_list):
    for row_no in range(len(grid)):
        for column_no in range(len(grid[0])):
            if grid[row_no][column_no] == 0:
                index = 0
            else:
                index =  int(math.log2(grid[row_no][column_no]))

            loc = row_no * len(grid) + column_no
            # print(f"{row_no} {column_no} => {loc} = {grid[row_no][column_no]}")
            sprite_list[loc].texture = texture_list[index]

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(800, 800, "2048")

        arcade.set_background_color(arcade.csscolor.CORAL)
        self.my_grid_sprites = create_grid_sprites()
        self.my_textures =  create_textures()
        self.my_grid = create_grid(BOARD_SIZE)

        self.spawn()
        # self.my_grid[0][0] = 2
        # self.my_grid[1][0] = 4
        print_grid(self.my_grid)

        update_grid_textures(self.my_grid, self.my_grid_sprites, self.my_textures)


    def spawn(self):
        if random.random() <= 0.1:
            number = 4
        else:
            number = 2
        spawn_number(self.my_grid, number)

    def on_draw(self):
        try:
            arcade.start_render()
            self.my_grid_sprites.draw()
        except Exception as e:
            print(f"Exception: {e}")

    def on_key_press(self, symbol: int, modifiers: int):
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
            self.spawn()
            update_grid_textures(self.my_grid, self.my_grid_sprites, self.my_textures)



def main():
    grid = create_grid(BOARD_SIZE)
    my_window = MyGame()

    arcade.run()


if __name__ == "__main__":
    main()
