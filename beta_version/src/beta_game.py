import arcade

from game_parameters import *
from map import load_map
from player import Player
import friendly_npcs
# import enemies

# import io_functions


class BetaGame(arcade.Window):
    """Custom window class"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # Set bg color
        arcade.set_background_color(arcade.color.GREEN)

        # Set up the player info
        self.player_list = arcade.SpriteList()
        self.player_sprite = None

        # Set up the npc info
        self.npc_list = arcade.SpriteList()
        self.mr_bean_sprite = None

        # Set up the enemy info
        self.enemy_list = arcade.SpriteList()

        self.text_list = arcade.SpriteList()

        self.scene = None
        self.maps = {1: load_map(1), 2: load_map(2), 3: load_map(3), 4: load_map(4)}

    def change_map(self, map_number):
        self.player_sprite.map_number = map_number
        self.scene = self.maps[map_number]

    def setup(self):
        # Set up the player
        self.player_sprite = Player()
        # Player initial position  - Spawn Point
        self.player_sprite.center_x = 150
        self.player_sprite.center_y = 550

        # Set up MrBean
        self.mr_bean_sprite = friendly_npcs.MrBean()
        # Mr.Bean initial position  - Waiting for the Player
        self.mr_bean_sprite.center_x = SCREEN_WIDTH - 50
        self.mr_bean_sprite.center_y = 100

        self.player_list.append(self.player_sprite)
        self.npc_list.append(self.mr_bean_sprite)

        self.change_map(1)
    """--------------------------------------------MAP LOGIC---------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""
    def player_at_first_map_exit(self):
        return self.player_sprite.center_x >= SCREEN_WIDTH - 15 and 360 < self.player_sprite.center_y < 390

    def first_map_logic(self):
        if self.player_at_first_map_exit():
            self.change_map(2)
            self.npc_list.remove(self.mr_bean_sprite)  # remove mr_bean from npc list if first maps is left
            self.player_sprite.center_x = 20
            self.player_sprite.center_y = 380

        if self.mr_bean_sprite.is_near(self.player_sprite.center_x, self.player_sprite.center_y):
            self.mr_bean_sprite.celebrate()
            # TODO Text: Just a Placeholder. Will be changed later
            text = arcade.create_text_sprite("How are you my friend?", self.mr_bean_sprite.center_x - 100,
                                             self.mr_bean_sprite.center_y + 50, (0, 0, 0), font_size=10)
            self.text_list.append(text)
        else:
            self.mr_bean_sprite.wait()
            self.text_list.clear()
    """--------------------------------------------------------------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""
    def player_at_second_map_entry(self):
        return self.player_sprite.center_x <= 15 and 360 < self.player_sprite.center_y < 390

    def player_at_second_map_exit(self):
        return 370 < self.player_sprite.center_x < 430 and self.player_sprite.center_y <= 60

    def second_map_logic(self):
        if self.player_at_second_map_entry():
            self.change_map(1)
            self.npc_list.append(self.mr_bean_sprite)  # add mr_bean to npc list if first maps is entered
            self.player_sprite.center_x = SCREEN_WIDTH - 20
            self.player_sprite.center_y = 380
        elif self.player_at_second_map_exit():
            self.change_map(3)
            self.player_sprite.center_x = 400
            # TODO BUG: Inconsistency with the screen sizes. Check size of maps and refactor code
            self.player_sprite.center_y = 560
            print("Exit 2 maps")
        pass
    """--------------------------------------------------------------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""
    def player_at_third_map_entry(self):
        # TODO BUG: Inconsistency with the screen sizes. Check size of maps
        # The very top of the game seems to be 567 and not 600 as defined in game_parameters.
        return 370 < self.player_sprite.center_x < 430 and self.player_sprite.center_y >= 567

    def player_at_third_map_exit(self):
        pass

    def third_map_logic(self):
        if self.player_at_third_map_entry():
            self.change_map(2)
            self.player_sprite.center_x = 400
            self.player_sprite.center_y = 60
            print("Entry 3 maps")
        elif self.player_at_third_map_exit():
            pass
        pass
    """--------------------------------------------------------------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""
    def player_at_fourth_map_entry(self):
        pass

    def fourth_map_logic(self):
        if self.player_at_first_map_exit():
            pass
        elif self.player_at_second_map_entry():
            pass
        pass
    """--------------------------------------------------------------------------------------------------------------"""
    """--------------------------------------------MAP LOGIC END-----------------------------------------------------"""

    def on_draw(self):
        arcade.start_render()

        # Draw all the sprites.
        if self.player_sprite.map_number == 1:
            self.clear()
            self.scene.draw()
            self.player_list.draw()
            self.enemy_list.draw()
            self.npc_list.draw()
            # Draw text of MrBean
            self.text_list.draw()  # TODO Text: Quick and dirty, other solution needed
            self.player_list.draw()
            self.npc_list.draw()

        elif self.player_sprite.map_number == 2:
            self.clear()
            self.scene.draw()
            self.player_list.draw()
            self.npc_list.draw()

        elif self.player_sprite.map_number == 3:
            self.clear()
            self.scene.draw()
            self.player_list.draw()
            self.npc_list.draw()

    def on_update(self, delta_time):
        if self.player_sprite.map_number == 1:
            self.first_map_logic()
        elif self.player_sprite.map_number == 2:
            self.second_map_logic()
        elif self.player_sprite.map_number == 3:
            self.third_map_logic()
        elif self.player_sprite.map_number == 4:
            self.fourth_map_logic()

        # Move the player
        self.player_list.update()
        self.player_list.update_animation()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.face_direction = FACING_TOP
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.face_direction = FACING_BOTTOM
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.face_direction = FACING_LEFT
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.face_direction = FACING_RIGHT
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.X:
            self.player_sprite.attack = ATTACK

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.X:
            self.player_sprite.attack = WAITING_ATTACK
        elif key == arcade.key.C:
            self.player_sprite.picking = PICKING
