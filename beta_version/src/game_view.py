import arcade
import math
import random

from game_parameters import *
from map import load_map
from player import Player
import friendly_npcs
from enemies import Enemy
<<<<<<< HEAD
from utils import normal_or_boosted_speed, draw_player_health, set_ability_icon
from object_tags import *
=======
from finalKnight import FinalKnight
from sound_player import SoundPlayer
>>>>>>> 4f199567b0800391342eaf307fe606816310e58d


class Game(arcade.View):
    def __init__(self):
        super().__init__()

        self.sound_player = SoundPlayer()
        # Set up the player info
        self.ability_icon = None
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
        self.map_enemies_killed = {1: True, 2: False, 3: False, 4: False, 5: True}

    def change_map(self, map_number, x_pos, y_pos):
        if self.map_enemies_killed[map_number] is False:
            self.create_enemy('skeleton')
            self.create_enemy('mushroom')
            self.create_enemy('slime')
        self.engine = None
        self.player_sprite.map_number = map_number
        self.scene = self.maps[map_number]
        self.player_sprite.center_x = x_pos
        self.player_sprite.center_y = y_pos

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
        draw_player_health(self)

        if self.ability_icon is not None:
            self.ability_icon.draw()

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
        self.final_knight = FinalKnight()

        self.change_map(1, 150, 550)
        self.engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("colisiones"))

    def create_enemy(self, enemy_type='skeleton'):
<<<<<<< HEAD
        enemy_strength = random.randint(1, 20) * 0.1
        enemy_sprite = Enemy(enemy_type, enemy_strength, int(3 * enemy_strength))
=======
        enemy_strength = random.randint(4, 20) * 0.1
        enemy_sprite = Enemy(enemy_type, enemy_strength, int(3*enemy_strength))
>>>>>>> 4f199567b0800391342eaf307fe606816310e58d
        enemy_sprite.center_x = random.randint(0, SCREEN_WIDTH)
        enemy_sprite.center_y = random.randint(0, SCREEN_HEIGHT)
        self.enemy_list.append(enemy_sprite)

    """--------------------------------------------MAP LOGIC---------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""

    def player_at_first_map_exit(self):
        # return False
        return (SCREEN_WIDTH - PLAYER_WIDTH - 6 <= self.player_sprite.center_x < SCREEN_WIDTH) and (
                330 < self.player_sprite.center_y < 390)

    def first_map_logic(self):
        self.start_engine()
        if self.mr_bean_sprite not in self.npc_list:
            self.npc_list.append(self.mr_bean_sprite)
        if self.player_at_first_map_exit():
            self.change_map(2, 20, 380)
            self.npc_list.remove(self.mr_bean_sprite)  # remove mr_bean from npc list if first map_pngs is left

        if self.mr_bean_sprite.is_near(self.player_sprite.center_x, self.player_sprite.center_y):
            if self.mr_bean_sprite.talked_to_bean is False:
                self.mr_bean_sprite.talk_to_bean()
                self.window.open_bean_cutscene()
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
        if len(self.enemy_list) == 0:
            self.map_enemies_killed[2] = True
            if self.player_at_second_map_entry():
                self.change_map(1, SCREEN_WIDTH - 20, 380)
                self.npc_list.append(self.mr_bean_sprite)  # add mr_bean to npc list if first map_pngs is entered
            elif self.player_at_second_map_exit():
                self.change_map(3, 400, 560)

    """--------------------------------------------------------------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""

    def player_at_third_map_entry(self):
        # TODO BUG: Inconsistency with the screen sizes. Check size of map_pngs
        # The very top of the game seems to be 567 and not 600 as defined in game_parameters.
        return 370 < self.player_sprite.center_x < 430 and self.player_sprite.center_y >= 587

    def player_at_third_map_exit(self):
        return self.player_sprite.center_x >= SCREEN_WIDTH - PLAYER_WIDTH and 130 < self.player_sprite.center_y < 280

    def third_map_logic(self):
        self.start_engine()
        if len(self.enemy_list) == 0:
            self.map_enemies_killed[3] = True
            if self.player_at_third_map_entry():
                self.change_map(2, 400, 60)
            elif self.player_at_third_map_exit():
                if self.final_knight not in self.enemy_list:
                    self.enemy_list.append(self.final_knight)
                self.change_map(4, 20, 200)

    """--------------------------------------------------------------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""

    def player_at_fourth_map_entry(self):
        return self.player_sprite.center_x <= PLAYER_WIDTH and 130 < self.player_sprite.center_y < 280

    def player_at_fourth_map_exit(self):
        return self.player_sprite.center_x >= SCREEN_WIDTH - PLAYER_WIDTH and 300 < self.player_sprite.center_y < 380

    def fourth_map_logic(self):
        self.start_engine()
        if len(self.enemy_list) == 0:
            self.map_enemies_killed[4] = True
            if self.player_at_fourth_map_entry():
                self.change_map(3, SCREEN_WIDTH - 20, 200)
            elif self.player_at_fourth_map_exit():
                self.change_map(5, 20, 350)

    """--------------------------------------------------------------------------------------------------------------"""
    """--------------------------------------------------------------------------------------------------------------"""

    def player_at_fifth_map_exit(self):
        return self.player_sprite.center_y <= PLAYER_HEIGHT

    def fifth_map_logic(self):
        self.start_engine()
        if self.player_at_fifth_map_exit():
            self.window.open_credits()
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

        elif self.player_sprite.map_number == 4:
            self.draw_scene_and_sprites()
            # arcade.draw_line(SCREEN_WIDTH-10, 380, SCREEN_WIDTH-10, 300, arcade.color.BLUE)

        elif self.player_sprite.map_number == 5:
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
        elif self.player_sprite.map_number == 5:
            self.fifth_map_logic()

        # Move the player
        self.player_list.update()
        self.player_list.update_animation()
        if self.engine is not None:
            self.engine.update()

        if self.player_sprite.power_up == POWERUP_ENABLED:
            self.ability_icon = set_ability_icon(self.player_sprite.item_picked)

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
                    self.window.open_game_over()
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
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.face_direction = FACING_TOP
                self.player_sprite.change_y = normal_or_boosted_speed(self.player_sprite.power_up,
                                                                      self.player_sprite.item_picked)
        elif key == arcade.key.S:
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.face_direction = FACING_BOTTOM
                self.player_sprite.change_y = -normal_or_boosted_speed(self.player_sprite.power_up,
                                                                       self.player_sprite.item_picked)
        elif key == arcade.key.A:
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.face_direction = FACING_LEFT
                self.player_sprite.change_x = -normal_or_boosted_speed(self.player_sprite.power_up,
                                                                       self.player_sprite.item_picked)
        elif key == arcade.key.D:
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.face_direction = FACING_RIGHT
                self.player_sprite.change_x = normal_or_boosted_speed(self.player_sprite.power_up,
                                                                      self.player_sprite.item_picked)
        elif key == arcade.key.K:
<<<<<<< HEAD
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.attack = ATTACK
=======
            self.player_sprite.attack = ATTACK
            # self.sound_player.play_sound(sound_name="attack_sound")
>>>>>>> 4f199567b0800391342eaf307fe606816310e58d
        elif key == arcade.key.ESCAPE:
            self.window.open_pause()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.K:
            self.player_sprite.attack = WAITING_ATTACK
        elif key == arcade.key.P:
            self.player_sprite.picking = PICKING

        # View character powerup, to change player use marked properties below
        elif key == arcade.key.T:
            if self.player_sprite.item_picked == PINK_CONSUMABLE:
                self.player_sprite.power_up = POWERUP_DISABLED # <-
                self.player_sprite.item_picked = EMPTY # <-
                self.player_sprite.scale = SPRITE_SCALING # <-
                self.ability_icon = None # <-
            else:
                self.player_sprite.power_up = POWERUP_ENABLED # <-
                self.player_sprite.item_picked = PINK_CONSUMABLE # <-
        elif key == arcade.key.Q:
            if self.player_sprite.item_picked == DEFAULT_CONSUMABLE:
                self.player_sprite.power_up = POWERUP_DISABLED # <-
                self.player_sprite.item_picked = EMPTY # <-
                self.player_sprite.health_points -= 1 # <-
                self.player_sprite.scale = SPRITE_SCALING # <-
                self.ability_icon = None
            else:
                self.player_sprite.power_up = POWERUP_ENABLED # <-
                self.player_sprite.item_picked = DEFAULT_CONSUMABLE # <-
                self.player_sprite.health_points += 1 # <-

    def print_player_pos(self):
        print(f"X:{self.player_sprite.center_x} --- Y:{self.player_sprite.center_y}")
