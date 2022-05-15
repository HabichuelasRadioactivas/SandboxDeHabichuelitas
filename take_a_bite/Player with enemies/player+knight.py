import math
from random import randint

from entities.Player import *
from entities.PickableItem import *
from entities.Enemy_FinalKnight import *

from utils.constants import *
from utils.object_tags import *


# Open up a window
SCREEN_WIDTH = 800  # WIDTH
SCREEN_HEIGHT = 600  # HEIGHT
SCREEN_TITLE = "player+knight"  # SCREEN_TITLE

MOVEMENT_SPEED = 3
FACING_TOP = 0
FACING_RIGHT = 1
FACING_BOTTOM = 2
FACING_LEFT = 3
NOT_PRESSED = 99

ATTACK = 1
WAITING_ATTACK = 0
HEALTH_KNIGHT = 10

UPDATES_PER_FRAME = 6


def load_texture_pair(filename):
    """
    Load a texture pair, with mirror image as second one
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]


def normal_or_boosted_speed(is_powered, item_picked):
    if is_powered:
        if item_picked == DEFAULT_CONSUMABLE:
            return MOVEMENT_SPEED_REDUCTION
        return MOVEMENT_SPEED_POWERUP
    else:
        return MOVEMENT_SPEED


class MyGame(arcade.Window):
    """Custom window class"""

    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        # Set bg color
        arcade.set_background_color(arcade.csscolor.WHITE)

        # Game scene
        self.scene = None

        # Set up the player info
        self.player_list = None
        self.player_sprite = None
        self.enemies_list = None
        self.enemy_sprite = None

        # Pick up object
        self.pickup_object_list = None

        # Draw text while game playing
        self.can_draw_text = False

        # Power up timer state variables
        self.powerup_countdown = 0
        self.total_time = 0.0

        self.pickup_object_sprite = None

        self.ability_icon = None

    def setup(self):
        # Creating scene
        self.scene = arcade.Scene()

        # Set up the player
        self.player_list = arcade.SpriteList()
        self.player_sprite = Player()

        # Player initial position
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2

        self.player_list.append(self.player_sprite)

        self.pickup_object_list = arcade.SpriteList()

        self.pickup_object_sprite = PickableItem("assets/food_items/blue_potion.png", randint(0, SCREEN_WIDTH),
                                                 randint(0, SCREEN_HEIGHT - 100), sprite_scaling=1.25,
                                                 tag=DEFAULT_CONSUMABLE)
        self.pickup_object_list.append(self.pickup_object_sprite)
        self.pickup_object_sprite = PickableItem("assets/food_items/pink_potion.png", randint(0, SCREEN_WIDTH),
                                                 randint(0, SCREEN_HEIGHT - 100), sprite_scaling=1.25,
                                                 tag=PINK_CONSUMABLE)
        self.pickup_object_list.append(self.pickup_object_sprite)

        self.enemies_list = arcade.SpriteList()

        self.enemy_sprite = Enemy()
        self.enemy_sprite.center_x = 65
        self.enemy_sprite.center_y = 56
        self.enemies_list.append(self.enemy_sprite)

        for enemy in self.enemies_list:
            self.scene.add_sprite('Final Knight', enemy)

        for pickable_object in self.pickup_object_list:
            self.scene.add_sprite('Pick-able object', pickable_object)

        self.scene.add_sprite('Player', self.player_sprite)

    def on_draw(self):
        arcade.start_render()

        # Draw all the sprites.
        self.scene.draw()

        arcade.draw_text('Arrow keys to move, hold X to attack, C to pick up or cancel on power up mode', 5,
                         SCREEN_HEIGHT - 21,
                         arcade.color.BLACK, 12)

        if self.can_draw_text:
            arcade.draw_text('C to pick up', SCREEN_WIDTH - 111, 21,
                             arcade.color.BLUEBERRY,
                             12, bold=True)

        arcade.draw_text(f'Power Up Countdown: {self.powerup_countdown} / {POWERUP_AVAILABLE_TIME}', 5,
                         SCREEN_HEIGHT - 42, arcade.color.BLACK)

        if self.ability_icon is not None:
            self.ability_icon.draw()

        icon_pos = [21, SCREEN_HEIGHT - 65]
        for i in range(self.player_sprite.health_points):
            self.health_icon = arcade.Sprite('assets/abilities_icons/health_icon.png', 1.5, center_x=icon_pos[0],
                                             center_y=icon_pos[1])
            self.health_icon.draw()
            icon_pos = [21 + self.health_icon.width * (i + 1), SCREEN_HEIGHT - 65]

    def on_update(self, delta_time):
        # Move the player
        self.player_list.update()
        self.player_list.update_animation()

        power_up_items_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.pickup_object_list)
        enemies_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemies_list)

        for power_up_item in power_up_items_hit_list:
            self.pickup_object_sprite = power_up_item
            if self.player_sprite.picking == PICKING:
                power_up_item.remove_from_sprite_lists()
                if self.player_sprite.item_picked == DEFAULT_CONSUMABLE:
                    self.player_sprite.health_points += 1

        if len(power_up_items_hit_list) != 0 and self.player_sprite.power_up == POWERUP_DISABLED:
            self.player_sprite.can_pick_up = True
            self.can_draw_text = True
        else:
            self.player_sprite.can_pick_up = False
            self.can_draw_text = False

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

        # Enable power up for x amount of seconds and display counter on screen
        if self.player_sprite.power_up == POWERUP_ENABLED:
            if self.powerup_countdown == POWERUP_AVAILABLE_TIME:
                self.player_sprite.power_up = POWERUP_DISABLED
                self.powerup_countdown = 0
                self.total_time = 0.0
                self.ability_icon = None
            else:
                self.total_time += delta_time
                seconds = int(self.total_time) % 60
                self.powerup_countdown = seconds

        if self.player_sprite.power_up == POWERUP_ENABLED:
            icon_pos = [SCREEN_WIDTH - 32, SCREEN_HEIGHT - 32]
            if self.player_sprite.item_picked == DEFAULT_CONSUMABLE:
                self.ability_icon = arcade.Sprite('assets/abilities_icons/blue_hability.png', 2,
                                                  center_x=icon_pos[0], center_y=icon_pos[1])
            if self.player_sprite.item_picked == PINK_CONSUMABLE:
                self.ability_icon = arcade.Sprite('assets/abilities_icons/pink_hability.png', 2,
                                                  center_x=icon_pos[0], center_y=icon_pos[1])
        for enemy in self.enemies_list:
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
            if x_diff <= 300 and y_diff <= 300 and not enemy.hit and not enemy.destroy_enemy and not enemy.attack:
                enemy.change_x = math.cos(angle) * ENEMY_MOVEMENT_SPEED
                enemy.change_y = math.sin(angle) * ENEMY_MOVEMENT_SPEED
            else:
                enemy.change_x = 0
                enemy.change_y = 0

            if enemy.destroy_enemy:
                for i in range(0, len(DIE_SPRITES), 1):
                    self.enemy_sprite = DIE_SPRITES[i]
                enemy.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.face_direction = FACING_TOP
                self.player_sprite.change_y = normal_or_boosted_speed(self.player_sprite.power_up,
                                                                      self.player_sprite.item_picked)
        elif key == arcade.key.DOWN:
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.face_direction = FACING_BOTTOM
                self.player_sprite.change_y = -normal_or_boosted_speed(self.player_sprite.power_up,
                                                                       self.player_sprite.item_picked)
        elif key == arcade.key.LEFT:
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.face_direction = FACING_LEFT
                self.player_sprite.change_x = -normal_or_boosted_speed(self.player_sprite.power_up,
                                                                       self.player_sprite.item_picked)
        elif key == arcade.key.RIGHT:
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.face_direction = FACING_RIGHT
                self.player_sprite.change_x = normal_or_boosted_speed(self.player_sprite.power_up,
                                                                      self.player_sprite.item_picked)
        elif key == arcade.key.X:
            if self.player_sprite.picking == WAITING_PICKING and self.player_sprite.attack == WAITING_ATTACK:
                self.player_sprite.attack = ATTACK

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.X:
            self.player_sprite.attack = WAITING_ATTACK
        elif key == arcade.key.C:
            if self.player_sprite.power_up == POWERUP_ENABLED:
                self.player_sprite.power_up = POWERUP_DISABLED
                self.powerup_countdown = 0
                self.total_time = 0.0
                self.ability_icon = None
            elif self.player_sprite.can_pick_up:
                self.player_sprite.picking = PICKING
                self.player_sprite.power_up = POWERUP_ENABLED
                self.player_sprite.item_picked = self.pickup_object_sprite.tag


def main():
    """Main method"""
    wn = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    wn.setup()
    arcade.run()


if __name__ == '__main__':
    main()




