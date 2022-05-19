import arcade
import math

from game_parameters import *
from map import load_map
from player import Player
from enemies import Enemy
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
        self.enemy_sprite = None

        self.text_list = arcade.SpriteList()

        self.engine = None
        self.scene = None
        self.maps = {1: load_map(1), 2: load_map(2), 3: load_map(3), 4: load_map(4), 5: load_map(5)}

    def change_map(self, map_number):
        self.engine = None
        self.player_sprite.map_number = map_number
        self.scene = self.maps[map_number]

    def start_engine(self):
        if self.engine is None:
            self.engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("colisiones"))

    def draw_scene_and_sprites(self):
        """Draws all sprites and the scene. If for any reason not all sprites should be drawn, do it manually"""
        self.clear()
        self.scene.draw()
        self.player_list.draw()
        self.enemy_list.draw()
        self.npc_list.draw()

    def setup(self):
        # Creating the scene
        self.scene = arcade.Scene()

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

        self.enemy_list = arcade.SpriteList()

        self.enemy_sprite = Enemy()
        self.enemy_sprite.center_x = SCREEN_WIDTH // 2
        self.enemy_sprite.center_y = SCREEN_HEIGHT // 2
        self.enemy_list.append(self.enemy_sprite)
        self.enemy_sprite = Enemy(enemy_type='mushroom')
        self.enemy_sprite.center_x = 213
        self.enemy_sprite.center_y = 98
        self.enemy_list.append(self.enemy_sprite)

        self.change_map(1)
        self.engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("colisiones"))
        self.set_update_rate(1/35) # TODO the engine increases the update rate. Has to be fixed
    """--------------------------------------------MAP LOGIC---------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""
    def player_at_first_map_exit(self):
        #return False
        return (SCREEN_WIDTH - PLAYER_WIDTH - 6 <= self.player_sprite.center_x < SCREEN_WIDTH) and (330 < self.player_sprite.center_y < 390)

    def first_map_logic(self):
        self.start_engine()
        if self.mr_bean_sprite not in self.npc_list:
            self.npc_list.append(self.mr_bean_sprite)
        if self.player_at_first_map_exit():
            self.change_map(2)
            self.npc_list.remove(self.mr_bean_sprite)  # remove mr_bean from npc list if first map_pngs is left
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
        return 370 < self.player_sprite.center_x < 460 and self.player_sprite.center_y <= 60

    def second_map_logic(self):
        self.start_engine()
        if self.player_at_second_map_entry():
            self.change_map(1)
            self.npc_list.append(self.mr_bean_sprite)  # add mr_bean to npc list if first map_pngs is entered
            self.player_sprite.center_x = SCREEN_WIDTH - 20
            self.player_sprite.center_y = 380
        elif self.player_at_second_map_exit():
            self.change_map(3)
            self.player_sprite.center_x = 400
            # TODO BUG: Inconsistency with the screen sizes. Check size of map_pngs and refactor code
            self.player_sprite.center_y = 560
        pass
    """--------------------------------------------------------------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""
    def player_at_third_map_entry(self):
        # TODO BUG: Inconsistency with the screen sizes. Check size of map_pngs
        # The very top of the game seems to be 567 and not 600 as defined in game_parameters.
        return 370 < self.player_sprite.center_x < 430 and self.player_sprite.center_y >= 587

    def player_at_third_map_exit(self):
        pass

    def third_map_logic(self):
        self.start_engine()
        if self.player_at_third_map_entry():
            self.change_map(2)
            self.player_sprite.center_x = 400
            self.player_sprite.center_y = 60
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
        if self.player_sprite.map_number == 1:
            self.draw_scene_and_sprites()
            # This contains the text of MrBean. For more see at first_map_logic
            self.text_list.draw()  # TODO Text: Quick and dirty, other solution needed

        elif self.player_sprite.map_number == 2:
            self.draw_scene_and_sprites()

        elif self.player_sprite.map_number == 3:
            self.draw_scene_and_sprites()

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
        if self.engine is not None:
            self.engine.update()

        enemies_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)

        for enemy_hit in enemies_hit_list:
            if self.player_sprite.attack == ATTACK:
                if enemy_hit.health_points == 1:
                    enemy_hit.health_points = 0
                    enemy_hit.enemy_dead = True
                else:
                    enemy_hit.change_x = (-ENEMY_MOVEMENT_SPEED * 21) if enemy_hit.left_or_right == 'right' else (
                            ENEMY_MOVEMENT_SPEED * 21)
                    enemy_hit.change_y = 0
                    enemy_hit.health_points -= 1
                    enemy_hit.hit = True
            else:
                enemy_hit.attack = True
                enemy_hit.attack_status = 0  # IMPORTANT ALLOW ATTACK ANIMATION TO REPEAT MULTIPLE TIMES
                enemy_hit.change_x = (-ENEMY_MOVEMENT_SPEED * 19) if enemy_hit.left_or_right == 'right' else (
                        ENEMY_MOVEMENT_SPEED * 19)
                enemy_hit.change_y = 0
                if self.player_sprite.health_points == 1:
                    self.player_sprite.health_points = 0
                    print('dead')
                else:
                    self.player_sprite.health_points -= 1

        for enemy in self.enemy_list:
            enemy.update()
            enemy.update_animation()

            # Position the start at the enemy's current location
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Get the destination location for the enemy
            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y

            # Do math to calculate how to get the enemy to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the enemy will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            if x_diff >= 0:
                # Player is on right side
                enemy.left_or_right = 'right'
            else:
                # Player is on left side
                enemy.left_or_right = 'left'

            # Move enemy towards player if is close enough
            if x_diff <= 225 and y_diff <= 225 and not enemy.hit and not enemy.destroy_enemy and not enemy.attack:
                enemy.change_x = math.cos(angle) * ENEMY_MOVEMENT_SPEED
                enemy.change_y = math.sin(angle) * ENEMY_MOVEMENT_SPEED
            else:
                enemy.change_x = 0
                enemy.change_y = 0

            if enemy.destroy_enemy:
                enemy.remove_from_sprite_lists()

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
