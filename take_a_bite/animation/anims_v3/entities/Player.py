import arcade
from typing import List
from utils.constants import *
from utils.sprites import *


def load_textures(append_to: List, sprites: List[str], flip_hor=False):
    for i in range(len(sprites)):
        append_to.append(arcade.load_texture(sprites[i], flipped_horizontally=flip_hor))


class Player(arcade.AnimatedTimeBasedSprite):
    """Player Class"""

    def __init__(self):
        super().__init__()

        # Set facing direction
        self.face_direction = FACING_BOTTOM

        # Set initial attack state
        self.attack = WAITING_ATTACK

        # Set initial picking state
        self.picking = WAITING_PICKING
        self.can_pick_up = False

        # Set initial power up state
        self.power_up = POWERUP_DISABLED

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
        self.pick_up_status = 0

        # Idle textures
        self.idle_down_textures = []
        load_textures(self.idle_down_textures, IDLE_DOWN_SPRITES)

        self.idle_up_textures = []
        load_textures(self.idle_up_textures, IDLE_UP_SPRITES)

        self.idle_down_textures_powerup = []
        load_textures(self.idle_down_textures_powerup, IDLE_DOWN_POWERUP_SPRITES)

        self.idle_up_textures_powerup = []
        load_textures(self.idle_up_textures_powerup, IDLE_UP_POWERUP_SPRITES)

        # Left side idle
        self.idle_left_side_textures = []
        load_textures(self.idle_left_side_textures, IDLE_SIDE_SPRITES)

        self.idle_left_side_textures_powerup = []
        load_textures(self.idle_left_side_textures_powerup, IDLE_SIDE_POWERUP_SPRITES)

        # Right side idle
        self.idle_right_side_textures = []
        load_textures(self.idle_right_side_textures, IDLE_SIDE_SPRITES, flip_hor=True)

        self.idle_right_side_textures_powerup = []
        load_textures(self.idle_right_side_textures_powerup, IDLE_SIDE_POWERUP_SPRITES, flip_hor=True)

        # Walk down textures
        self.walk_down_textures = []
        load_textures(self.walk_down_textures, WALK_DOWN_SPRITES)

        self.walk_down_textures_powerup = []
        load_textures(self.walk_down_textures_powerup, WALK_DOWN_POWERUP_SPRITES)

        # Walk up textures
        self.walk_up_textures = []
        load_textures(self.walk_up_textures, WALK_UP_SPRITES)

        self.walk_up_textures_powerup = []
        load_textures(self.walk_up_textures_powerup, WALK_UP_POWERUP_SPRITES)

        # Walk left textures
        self.walk_left_textures = []
        load_textures(self.walk_left_textures, SIDE_WALK_SPRITES)

        self.walk_left_textures_powerup = []
        load_textures(self.walk_left_textures_powerup, SIDE_WALK_POWERUP_SPRITES)

        # Walk right textures
        self.walk_right_textures = []
        load_textures(self.walk_right_textures, SIDE_WALK_SPRITES, flip_hor=True)

        self.walk_right_textures_powerup = []
        load_textures(self.walk_right_textures_powerup, SIDE_WALK_POWERUP_SPRITES, flip_hor=True)

        # Attack down textures
        self.attack_down_textures = []
        load_textures(self.attack_down_textures, ATTACK_DOWN_SPRITES)

        self.attack_down_textures_powerup = []
        load_textures(self.attack_down_textures_powerup, ATTACK_DOWN_POWERUP_SPRITES)

        # Attack up textures
        self.attack_up_textures = []
        load_textures(self.attack_up_textures, ATTACK_UP_SPRITES)

        self.attack_up_textures_powerup = []
        load_textures(self.attack_up_textures_powerup, ATTACK_UP_POWERUP_SPRITES)

        # Attack left textures
        self.attack_left_textures = []
        load_textures(self.attack_left_textures, ATTACK_SIDE_SPRITES)

        self.attack_left_textures_powerup = []
        load_textures(self.attack_left_textures_powerup, ATTACK_SIDE_POWERUP_SPRITES)

        # Attack right textures
        self.attack_right_textures = []
        load_textures(self.attack_right_textures, ATTACK_SIDE_SPRITES, flip_hor=True)

        self.attack_right_textures_powerup = []
        load_textures(self.attack_right_textures_powerup, ATTACK_SIDE_POWERUP_SPRITES, flip_hor=True)

        # Pick up textures
        self.pick_up_textures = []
        for i in range(len(PICK_UP_SPRITES)):
            self.pick_up_textures.append(arcade.load_texture(PICK_UP_SPRITES[i]))

        # Set initial texture
        self.texture = self.idle_down_textures[0]

    # Helper functions
    def update_idle_down_anim(self):
        # if self.idle_status == len(IDLE_SPRITES) - 1:
        if self.idle_down_status > (len(IDLE_DOWN_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.idle_down_status = 0
        else:
            self.idle_down_status += 1

    def update_idle_up_anim(self):
        if self.idle_up_status > (len(IDLE_UP_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.idle_up_status = 0
        else:
            self.idle_up_status += 1

    def update_idle_side_anim(self):
        if self.idle_side_status > (len(IDLE_SIDE_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.idle_side_status = 0
        else:
            self.idle_side_status += 1

    def update_walk_down_anim(self):
        if self.walk_down_status > (len(WALK_DOWN_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.walk_down_status = 0
        else:
            self.walk_down_status += 1

    def update_walk_up_anim(self):
        if self.walk_up_status > (len(WALK_UP_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.walk_up_status = 0
        else:
            self.walk_up_status += 1

    def update_side_walk_anim(self):
        if self.walk_side_status > (len(SIDE_WALK_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.walk_side_status = 0
        else:
            self.walk_side_status += 1

    def update_attack_down_anim(self):
        if self.attack_down_status > (len(ATTACK_DOWN_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.attack_down_status = 0
        else:
            self.attack_down_status += 1

    def update_attack_up_anim(self):
        if self.attack_up_status > (len(ATTACK_UP_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.attack_up_status = 0
        else:
            self.attack_up_status += 1

    def update_attack_side_anim(self):
        if self.attack_side_status > (len(ATTACK_SIDE_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.attack_side_status = 0
        else:
            self.attack_side_status += 1

    def update_pick_up_anim(self):
        if self.pick_up_status > (len(PICK_UP_SPRITES) - 1) * UPDATES_PER_FRAME:
            self.pick_up_status = 0
            self.picking = WAITING_PICKING
        else:
            self.pick_up_status += 1

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
        # Idle animations
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

        # Powerup Idle animations
        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_BOTTOM and self.power_up == POWERUP_ENABLED:
            self.texture = self.idle_down_textures_powerup[idle_down_frame]
            self.update_idle_down_anim()

        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_TOP and self.power_up == POWERUP_ENABLED:
            self.texture = self.idle_up_textures_powerup[idle_up_frame]
            self.update_idle_up_anim()

        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_LEFT and self.power_up == POWERUP_ENABLED:
            self.texture = self.idle_left_side_textures_powerup[idle_side_frame]
            self.update_idle_side_anim()

        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_RIGHT and self.power_up == POWERUP_ENABLED:
            self.texture = self.idle_right_side_textures_powerup[idle_side_frame]
            self.update_idle_side_anim()

        # Walk down animation
        walk_down_frame = self.walk_down_status // UPDATES_PER_FRAME
        if self.change_y != 0 and self.face_direction == FACING_BOTTOM:
            self.texture = self.walk_down_textures[walk_down_frame]
            self.update_walk_down_anim()

        # Walk down powerup animation
        if self.change_y != 0 and self.face_direction == FACING_BOTTOM and self.power_up == POWERUP_ENABLED:
            self.texture = self.walk_down_textures_powerup[walk_down_frame]
            self.update_walk_down_anim()

        # Walk up animation
        walk_up_frame = self.walk_up_status // UPDATES_PER_FRAME
        if self.change_y != 0 and self.face_direction == FACING_TOP:
            self.texture = self.walk_up_textures[walk_up_frame]
            self.update_walk_up_anim()

        # Walk up powerup animation
        if self.change_y != 0 and self.face_direction == FACING_TOP and self.power_up == POWERUP_ENABLED:
            self.texture = self.walk_up_textures_powerup[walk_up_frame]
            self.update_walk_up_anim()

        # Sidewalk animations
        side_walk_frame = self.walk_side_status // UPDATES_PER_FRAME
        if self.change_x != 0 and self.face_direction == FACING_LEFT:
            self.texture = self.walk_left_textures[side_walk_frame]
            self.update_side_walk_anim()
        elif self.change_x != 0 and self.face_direction == FACING_RIGHT:
            self.texture = self.walk_right_textures[side_walk_frame]
            self.update_side_walk_anim()

        # Sidewalk powerup animations
        if self.change_x != 0 and self.face_direction == FACING_LEFT and self.power_up:
            self.texture = self.walk_left_textures_powerup[side_walk_frame]
            self.update_side_walk_anim()
        elif self.change_x != 0 and self.face_direction == FACING_RIGHT and self.power_up:
            self.texture = self.walk_right_textures_powerup[side_walk_frame]
            self.update_side_walk_anim()

        # Attack animations
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

        # Attack powerup animations
        if self.attack == ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_BOTTOM and self.power_up == POWERUP_ENABLED:
            self.texture = self.attack_down_textures_powerup[attack_down_frame]
            self.update_attack_down_anim()
        elif self.attack == ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_TOP and self.power_up == POWERUP_ENABLED:
            self.texture = self.attack_up_textures_powerup[attack_up_frame]
            self.update_attack_up_anim()
        elif self.attack == ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_LEFT and self.power_up == POWERUP_ENABLED:
            self.texture = self.attack_left_textures_powerup[attack_side_frame]
            self.update_attack_side_anim()
        elif self.attack == ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_RIGHT and self.power_up == POWERUP_ENABLED:
            self.texture = self.attack_right_textures_powerup[attack_side_frame]
            self.update_attack_side_anim()

        # Pick up animation
        pick_up_frame = self.pick_up_status // UPDATES_PER_FRAME
        if self.change_x == 0 and self.change_y == 0 and self.picking == PICKING:
            self.texture = self.pick_up_textures[pick_up_frame]
            self.update_pick_up_anim()
