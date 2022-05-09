import arcade
from random import randint
import math

from utils.constants import *
from utils.object_tags import *
from entities.Player import Player
from entities.PickableItem import PickableItem

# Open up a window
SCREEN_WIDTH = 800  # WIDTH
SCREEN_HEIGHT = 600  # HEIGHT
SCREEN_TITLE = "FINAL KNIGHT"  # SCREEN_TITLE

IDLE_SPRITES = [
    "PNGs_Knights/2_KNIGHT/_IDLE/_IDLE_000.png",
    "PNGs_Knights/2_KNIGHT/_IDLE/_IDLE_001.png",
    "PNGs_Knights/2_KNIGHT/_IDLE/_IDLE_002.png",
    "PNGs_Knights/2_KNIGHT/_IDLE/_IDLE_003.png",
    "PNGs_Knights/2_KNIGHT/_IDLE/_IDLE_004.png",
    "PNGs_Knights/2_KNIGHT/_IDLE/_IDLE_005.png",
    "PNGs_Knights/2_KNIGHT/_IDLE/_IDLE_006.png",
    ]

ATTACK_SPRITES = [
    "PNGs_Knights/2_KNIGHT/_ATTACK/_ATTACK_000.png",
    "PNGs_Knights/2_KNIGHT/_ATTACK/_ATTACK_001.png",
    "PNGs_Knights/2_KNIGHT/_ATTACK/_ATTACK_002.png",
    "PNGs_Knights/2_KNIGHT/_ATTACK/_ATTACK_003.png",
    "PNGs_Knights/2_KNIGHT/_ATTACK/_ATTACK_004.png",
    "PNGs_Knights/2_KNIGHT/_ATTACK/_ATTACK_005.png",
    "PNGs_Knights/2_KNIGHT/_ATTACK/_ATTACK_006.png",
]

DIE_SPRITES = [
    "PNGs_Knights/2_KNIGHT/_DIE/_DIE_000.png",
    "PNGs_Knights/2_KNIGHT/_DIE/_DIE_001.png",
    "PNGs_Knights/2_KNIGHT/_DIE/_DIE_002.png",
    "PNGs_Knights/2_KNIGHT/_DIE/_DIE_003.png",
    "PNGs_Knights/2_KNIGHT/_DIE/_DIE_004.png",
    "PNGs_Knights/2_KNIGHT/_DIE/_DIE_005.png",
    "PNGs_Knights/2_KNIGHT/_DIE/_DIE_006.png",
]

HURT_SPRITES = [
    "PNGs_Knights/2_KNIGHT/_HURT/HURT_000.png",
    "PNGs_Knights/2_KNIGHT/_HURT/HURT_001.png",
    "PNGs_Knights/2_KNIGHT/_HURT/HURT_002.png",
    "PNGs_Knights/2_KNIGHT/_HURT/HURT_003.png",
    "PNGs_Knights/2_KNIGHT/_HURT/HURT_004.png",
    "PNGs_Knights/2_KNIGHT/_HURT/HURT_005.png",
    "PNGs_Knights/2_KNIGHT/_HURT/HURT_006.png",
]

JUMP_SPRITES = [
    "PNGs_Knights/2_KNIGHT/_JUMP/_JUMP_000.png",
    "PNGs_Knights/2_KNIGHT/_JUMP/_JUMP_001.png",
    "PNGs_Knights/2_KNIGHT/_JUMP/_JUMP_002.png",
    "PNGs_Knights/2_KNIGHT/_JUMP/_JUMP_003.png",
    "PNGs_Knights/2_KNIGHT/_JUMP/_JUMP_004.png",
    "PNGs_Knights/2_KNIGHT/_JUMP/_JUMP_005.png",
    "PNGs_Knights/2_KNIGHT/_JUMP/_JUMP_006.png",
]

RUN_SPRITES = [
    "PNGs_Knights/2_KNIGHT/_RUN/_RUN_000.png",
    "PNGs_Knights/2_KNIGHT/_RUN/_RUN_001.png",
    "PNGs_Knights/2_KNIGHT/_RUN/_RUN_002.png",
    "PNGs_Knights/2_KNIGHT/_RUN/_RUN_003.png",
    "PNGs_Knights/2_KNIGHT/_RUN/_RUN_004.png",
    "PNGs_Knights/2_KNIGHT/_RUN/_RUN_005.png",
    "PNGs_Knights/2_KNIGHT/_RUN/_RUN_006.png",
]

WALK_SPRITES = [
    "PNGs_Knights/2_KNIGHT/_WALK/_WALK_000.png",
    "PNGs_Knights/2_KNIGHT/_WALK/_WALK_001.png",
    "PNGs_Knights/2_KNIGHT/_WALK/_WALK_002.png",
    "PNGs_Knights/2_KNIGHT/_WALK/_WALK_003.png",
    "PNGs_Knights/2_KNIGHT/_WALK/_WALK_004.png",
    "PNGs_Knights/2_KNIGHT/_WALK/_WALK_005.png",
    "PNGs_Knights/2_KNIGHT/_WALK/_WALK_006.png",
]

MOVEMENT_SPEED = 3
FACING_TOP = 0
FACING_RIGHT = 1
FACING_BOTTOM = 2
FACING_LEFT = 3
NOT_PRESSED = 99


SPRITE_SCALING = 0.1

ATTACK = 1
WAITING_ATTACK = 0
HEALTH_KNIGHT = 10

UPDATES_PER_FRAME = 7


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


class FinalKnight(arcade.AnimatedTimeBasedSprite):
    """Knight class"""

    def __init__(self):
        super().__init__()

        self.health = HEALTH_KNIGHT

        # Set facing direction
        self.face_direction = FACING_BOTTOM

        # Set initial attack state
        self.attack = WAITING_ATTACK

        # Used for flipping between image sequences
        self.cur_texture = 0

        # Texture scaling
        self.scale = SPRITE_SCALING

        # Initial animations status
        self.idle_down_status = 0
        self.idle_up_status = 0
        self.idle_side_status = 0
        self.walk_down_status = 0
        self.walk_up_status = 0
        self.walk_side_status = 0
        self.attack_down_status = 0
        self.attack_up_status = 0
        self.attack_side_status = 0

        # Idle textures
        # Left side idle
        self.idle_left_side_textures = []
        for i in range(len(IDLE_SPRITES)):
            self.idle_left_side_textures.append(arcade.load_texture(IDLE_SPRITES[i], flipped_horizontally=True))

        # Right side idle
        self.idle_right_side_textures = []
        for i in range(len(IDLE_SPRITES)):
            self.idle_right_side_textures.append(arcade.load_texture(IDLE_SPRITES[i]))

        # Down idle
        self.idle_down_textures = []
        for i in range(len(IDLE_SPRITES)):
            self.idle_down_textures.append(arcade.load_texture(IDLE_SPRITES[i]))

        # Up idle
        self.idle_up_textures = []
        for i in range(len(IDLE_SPRITES)):
            self.idle_up_textures.append(arcade.load_texture(IDLE_SPRITES[i]))

        # Walk textures
        # Walk left textures
        self.walk_left_textures = []
        for i in range(len(WALK_SPRITES)):
            self.walk_left_textures.append(arcade.load_texture(WALK_SPRITES[i], flipped_horizontally=True))

        # Walk right textures
        self.walk_right_textures = []
        for i in range(len(WALK_SPRITES)):
            self.walk_right_textures.append(arcade.load_texture(WALK_SPRITES[i]))

        # Walk down textures
        self.walk_down_textures = []
        for i in range(len(WALK_SPRITES)):
            self.walk_down_textures.append(arcade.load_texture(WALK_SPRITES[i]))

        # Walk up textures
        self.walk_up_textures = []
        for i in range(len(WALK_SPRITES)):
            self.walk_up_textures.append(arcade.load_texture(WALK_SPRITES[i]))

        # Attack textures
        # Attack left textures
        self.attack_left_textures = []
        for i in range(len(ATTACK_SPRITES)):
            self.attack_left_textures.append(arcade.load_texture(ATTACK_SPRITES[i], flipped_horizontally=True))

        # Attack right textures
        self.attack_right_textures = []
        for i in range(len(ATTACK_SPRITES)):
            self.attack_right_textures.append(arcade.load_texture(ATTACK_SPRITES[i]))

        # Attack down textures
        self.attack_down_textures = []
        for i in range(len(ATTACK_SPRITES)):
            self.attack_down_textures.append(arcade.load_texture(ATTACK_SPRITES[i]))

        # Attack up textures
        self.attack_up_textures = []
        for i in range(len(ATTACK_SPRITES)):
            self.attack_up_textures.append(arcade.load_texture(ATTACK_SPRITES[i]))

        # Set initial texture
        self.texture = self.idle_right_side_textures[0]

    # Helper functions
    def update_idle_down_anim(self):
        # if self.idle_status == len(IDLE_SPRITES) - 1:
        if self.idle_down_status > (len(IDLE_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.idle_down_status = 0
        else:
            self.idle_down_status += 1

    def update_idle_up_anim(self):
        if self.idle_up_status > (len(IDLE_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.idle_up_status = 0
        else:
            self.idle_up_status += 1

    def update_idle_side_anim(self):
        if self.idle_side_status > (len(IDLE_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.idle_side_status = 0
        else:
            self.idle_side_status += 1

    def update_walk_down_anim(self):
        if self.walk_down_status > (len(WALK_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.walk_down_status = 0
        else:
            self.walk_down_status += 1

    def update_walk_up_anim(self):
        if self.walk_up_status > (len(WALK_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.walk_up_status = 0
        else:
            self.walk_up_status += 1

    def update_side_walk_anim(self):
        if self.walk_side_status > (len(WALK_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.walk_side_status = 0
        else:
            self.walk_side_status += 1

    def update_attack_down_anim(self):
        if self.attack_down_status > (len(ATTACK_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.attack_down_status = 0
        else:
            self.attack_down_status += 1

    def update_attack_up_anim(self):
        if self.attack_up_status > (len(ATTACK_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.attack_up_status = 0
        else:
            self.attack_up_status += 1

    def update_attack_side_anim(self):
        if self.attack_side_status > (len(ATTACK_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.attack_side_status = 0
        else:
            self.attack_side_status += 1

    def update(self):
        # Move player
        self.center_x += self.change_x
        self.center_y += self.change_y

        # out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

    def update_animation(self, delta_time: float = 1 / 60):

        # Idle animation
        idle_down_frame = self.idle_down_status // UPDATES_PER_FRAME
        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_BOTTOM:
            self.texture = self.idle_down_textures[idle_down_frame]
            self.update_idle_down_anim()

        idle_up_frame = self.idle_up_status // UPDATES_PER_FRAME
        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_TOP:
            self.texture = self.idle_up_textures[idle_up_frame]
            self.update_idle_up_anim()

        idle_side_frame = self.idle_side_status // UPDATES_PER_FRAME
        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_LEFT:
            self.texture = self.idle_left_side_textures[idle_side_frame]
            self.update_idle_side_anim()

        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_RIGHT:
            self.texture = self.idle_right_side_textures[idle_side_frame]
            self.update_idle_side_anim()

        # Walk down animation
        walk_down_frame = self.walk_down_status // UPDATES_PER_FRAME
        if self.change_y != 0 and self.face_direction == FACING_BOTTOM:
            self.texture = self.walk_down_textures[walk_down_frame]
            self.update_walk_down_anim()

        # Walk up animation
        walk_up_frame = self.walk_up_status // UPDATES_PER_FRAME
        if self.change_y != 0 and self.face_direction == FACING_TOP:
            self.texture = self.walk_up_textures[walk_up_frame]
            self.update_walk_up_anim()

        # Sidewalk animation
        side_walk_frame = self.walk_side_status // UPDATES_PER_FRAME
        if self.change_x != 0 and self.face_direction == FACING_LEFT:
            self.texture = self.walk_left_textures[side_walk_frame]
            self.update_side_walk_anim()
        elif self.change_x != 0 and self.face_direction == FACING_RIGHT:
            self.texture = self.walk_right_textures[side_walk_frame]
            self.update_side_walk_anim()

        # Attack animation
        attack_down_frame = self.attack_down_status // UPDATES_PER_FRAME
        attack_up_frame = self.attack_up_status // UPDATES_PER_FRAME
        attack_side_frame = self.attack_side_status // UPDATES_PER_FRAME
        if self.attack == ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_BOTTOM:
            self.texture = self.attack_down_textures[attack_down_frame]
            self.update_attack_down_anim()
        elif self.attack == ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_TOP:
            self.texture = self.attack_up_textures[attack_up_frame]
            self.update_attack_up_anim()
        elif self.attack == ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_LEFT:
            self.texture = self.attack_left_textures[attack_side_frame]
            self.update_attack_side_anim()
        elif self.attack == ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_RIGHT:
            self.texture = self.attack_right_textures[attack_side_frame]
            self.update_attack_side_anim()


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Set bg color
        arcade.set_background_color(arcade.color.WHITE)

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

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Set up the player info
        self.finalKnight_list = None
        self.finalKnight_sprite = None

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

        # Set up the knight
        self.finalKnight_list = arcade.SpriteList()
        self.finalKnight_sprite = FinalKnight()

        # Knight initial position  - Spawn Point
        self.finalKnight_sprite.center_x = 600
        self.finalKnight_sprite.center_y = 500

        self.finalKnight_list.append(self.finalKnight_sprite)

        self.pickup_object_list = arcade.SpriteList()
        self.pickup_object_sprite = PickableItem("assets/food_items/blue_potion.png", randint(0, SCREEN_WIDTH),
                                                 randint(0, SCREEN_HEIGHT - 100), sprite_scaling=1.25,
                                                 tag=DEFAULT_CONSUMABLE)
        self.pickup_object_list.append(self.pickup_object_sprite)
        self.pickup_object_sprite = PickableItem("assets/food_items/pink_potion.png", randint(0, SCREEN_WIDTH),
                                                 randint(0, SCREEN_HEIGHT - 100), sprite_scaling=1.25,
                                                 tag=PINK_CONSUMABLE)
        self.pickup_object_list.append(self.pickup_object_sprite)

        for pickable_object in self.pickup_object_list:
            self.scene.add_sprite('Pick-able object', pickable_object)

        for enemy in self.finalKnight_list:
            self.scene.add_sprite('knight', enemy)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        self.finalKnight_list.draw()

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
            self.health_icon = arcade.Sprite('./assets/abilities_icons/health_icon.png', 1.5, center_x=icon_pos[0],
                                             center_y=icon_pos[1])
            self.health_icon.draw()
            icon_pos = [21 + self.health_icon.width * (i + 1), SCREEN_HEIGHT - 65]

    def on_update(self, delta_time):
        """# Move the player
        self.finalKnight_list.update()
        self.finalKnight_list.update_animation()"""

        # Move the player
        self.player_list.update()
        self.player_list.update_animation()

        power_up_items_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.pickup_object_list)
        enemies_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.finalKnight_list)

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
                self.ability_icon = arcade.Sprite('./assets/abilities_icons/blue_hability.png', 2,
                                                  center_x=icon_pos[0], center_y=icon_pos[1])
            if self.player_sprite.item_picked == PINK_CONSUMABLE:
                self.ability_icon = arcade.Sprite('./assets/abilities_icons/pink_hability.png', 2,
                                                  center_x=icon_pos[0], center_y=icon_pos[1])

        for enemy in self.finalKnight_list:
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
        """ Called whenever the user presses a key. """
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
        """ Called whenever a user releases a key. """
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
