import arcade

import utils.constants
from utils.object_tags import *
from utils.animations_list import *
from utils.anims_state_updater import *
from utils.texture_loader import load_textures


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

        # Texture scaling
        self.scale = SPRITE_SCALING

        # Current item being pick by player
        self.item_picked = EMPTY

        # Current animation being played
        self.current_animation = IDLE

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
        
        # Player frame rate
        self.updates_per_frame = UPDATES_PER_FRAME

        # Player health points
        self.health_points = 3

        # Idle textures
        self.idle_down_textures = []
        load_textures(self.idle_down_textures, PLAYER_IDLE_DOWN_SPRITES)

        self.idle_up_textures = []
        load_textures(self.idle_up_textures, PLAYER_IDLE_UP_SPRITES)

        self.idle_down_textures_powerup = []
        load_textures(self.idle_down_textures_powerup, PLAYER_IDLE_DOWN_POWERUP_SPRITES)

        self.idle_up_textures_powerup = []
        load_textures(self.idle_up_textures_powerup, PLAYER_IDLE_UP_POWERUP_SPRITES)

        self.idle_down_textures_powerup_pink = []
        load_textures(self.idle_down_textures_powerup_pink, PLAYER_IDLE_DOWN_POWERUP_PINK_SPRITES)

        self.idle_up_textures_powerup_pink = []
        load_textures(self.idle_up_textures_powerup_pink, PLAYER_IDLE_UP_POWERUP_PINK_SPRITES)

        # Left side idle
        self.idle_left_side_textures = []
        load_textures(self.idle_left_side_textures, PLAYER_IDLE_SIDE_SPRITES)

        self.idle_left_side_textures_powerup = []
        load_textures(self.idle_left_side_textures_powerup, PLAYER_IDLE_SIDE_POWERUP_SPRITES)

        self.idle_left_side_textures_powerup_pink = []
        load_textures(self.idle_left_side_textures_powerup_pink, PLAYER_IDLE_SIDE_POWERUP_PINK_SPRITES)

        # Right side idle
        self.idle_right_side_textures = []
        load_textures(self.idle_right_side_textures, PLAYER_IDLE_SIDE_SPRITES, flip_hor=True)

        self.idle_right_side_textures_powerup = []
        load_textures(self.idle_right_side_textures_powerup, PLAYER_IDLE_SIDE_POWERUP_SPRITES, flip_hor=True)

        self.idle_right_side_textures_powerup_pink = []
        load_textures(self.idle_right_side_textures_powerup_pink, PLAYER_IDLE_SIDE_POWERUP_PINK_SPRITES, flip_hor=True)

        # Walk down textures
        self.walk_down_textures = []
        load_textures(self.walk_down_textures, PLAYER_WALK_DOWN_SPRITES)

        self.walk_down_textures_powerup = []
        load_textures(self.walk_down_textures_powerup, PLAYER_WALK_DOWN_POWERUP_SPRITES)

        self.walk_down_textures_powerup_pink = []
        load_textures(self.walk_down_textures_powerup_pink, PLAYER_WALK_DOWN_POWERUP_PINK_SPRITES)

        # Walk up textures
        self.walk_up_textures = []
        load_textures(self.walk_up_textures, PLAYER_WALK_UP_SPRITES)

        self.walk_up_textures_powerup = []
        load_textures(self.walk_up_textures_powerup, PLAYER_WALK_UP_POWERUP_SPRITES)

        self.walk_up_textures_powerup_pink = []
        load_textures(self.walk_up_textures_powerup_pink, PLAYER_WALK_UP_POWERUP_PINK_SPRITES)

        # Walk left textures
        self.walk_left_textures = []
        load_textures(self.walk_left_textures, PLAYER_SIDE_WALK_SPRITES)

        self.walk_left_textures_powerup = []
        load_textures(self.walk_left_textures_powerup, PLAYER_SIDE_WALK_POWERUP_SPRITES)

        self.walk_left_textures_powerup_pink = []
        load_textures(self.walk_left_textures_powerup_pink, PLAYER_SIDE_WALK_POWERUP_PINK_SPRITES)

        # Walk right textures
        self.walk_right_textures = []
        load_textures(self.walk_right_textures, PLAYER_SIDE_WALK_SPRITES, flip_hor=True)

        self.walk_right_textures_powerup = []
        load_textures(self.walk_right_textures_powerup, PLAYER_SIDE_WALK_POWERUP_SPRITES, flip_hor=True)

        self.walk_right_textures_powerup_pink = []
        load_textures(self.walk_right_textures_powerup_pink, PLAYER_SIDE_WALK_POWERUP_PINK_SPRITES, flip_hor=True)

        # Attack down textures
        self.attack_down_textures = []
        load_textures(self.attack_down_textures, PLAYER_ATTACK_DOWN_SPRITES)

        self.attack_down_textures_powerup = []
        load_textures(self.attack_down_textures_powerup, PLAYER_ATTACK_DOWN_POWERUP_SPRITES)

        self.attack_down_textures_powerup_pink = []
        load_textures(self.attack_down_textures_powerup_pink, PLAYER_ATTACK_DOWN_POWERUP_PINK_SPRITES)

        # Attack up textures
        self.attack_up_textures = []
        load_textures(self.attack_up_textures, PLAYER_ATTACK_UP_SPRITES)

        self.attack_up_textures_powerup = []
        load_textures(self.attack_up_textures_powerup, PLAYER_ATTACK_UP_POWERUP_SPRITES)

        self.attack_up_textures_powerup_pink = []
        load_textures(self.attack_up_textures_powerup_pink, PLAYER_ATTACK_UP_POWERUP_PINK_SPRITES)

        # Attack left textures
        self.attack_left_textures = []
        load_textures(self.attack_left_textures, PLAYER_ATTACK_SIDE_SPRITES)

        self.attack_left_textures_powerup = []
        load_textures(self.attack_left_textures_powerup, PLAYER_ATTACK_SIDE_POWERUP_SPRITES)

        self.attack_left_textures_powerup_pink = []
        load_textures(self.attack_left_textures_powerup_pink, PLAYER_ATTACK_SIDE_POWERUP_PINK_SPRITES)

        # Attack right textures
        self.attack_right_textures = []
        load_textures(self.attack_right_textures, PLAYER_ATTACK_SIDE_SPRITES, flip_hor=True)

        self.attack_right_textures_powerup = []
        load_textures(self.attack_right_textures_powerup, PLAYER_ATTACK_SIDE_POWERUP_SPRITES, flip_hor=True)

        self.attack_right_textures_powerup_pink = []
        load_textures(self.attack_right_textures_powerup_pink, PLAYER_ATTACK_SIDE_POWERUP_PINK_SPRITES, flip_hor=True)

        # Pick up textures
        self.pick_up_textures = []
        for i in range(len(PLAYER_PICK_UP_SPRITES)):
            self.pick_up_textures.append(arcade.load_texture(PLAYER_PICK_UP_SPRITES[i]))

        # Set initial texture
        self.texture = self.idle_down_textures[0]

    def set_texture_based_on_facing_position(self, frame_rate, current_anim, consumable):
        if consumable == DEFAULT_CONSUMABLE:
            self.scale = 0.055
            # Player speed is reduced & health is increased
            if current_anim == IDLE:
                if self.face_direction == FACING_TOP:
                    return self.idle_up_textures_powerup[frame_rate]
                elif self.face_direction == FACING_BOTTOM:
                    return self.idle_down_textures_powerup[frame_rate]
                elif self.face_direction == FACING_LEFT:
                    return self.idle_left_side_textures_powerup[frame_rate]
                elif self.face_direction == FACING_RIGHT:
                    return self.idle_right_side_textures_powerup[frame_rate]

            if current_anim == WALK:
                if self.face_direction == FACING_TOP:
                    return self.walk_up_textures_powerup[frame_rate]
                elif self.face_direction == FACING_BOTTOM:
                    return self.walk_down_textures_powerup[frame_rate]
                elif self.face_direction == FACING_LEFT:
                    return self.walk_left_textures_powerup[frame_rate]
                elif self.face_direction == FACING_RIGHT:
                    return self.walk_right_textures_powerup[frame_rate]

            if current_anim == ATTACK_ANIM:
                if self.face_direction == FACING_TOP:
                    return self.attack_up_textures_powerup[frame_rate]
                elif self.face_direction == FACING_BOTTOM:
                    return self.attack_down_textures_powerup[frame_rate]
                elif self.face_direction == FACING_LEFT:
                    return self.attack_left_textures_powerup[frame_rate]
                elif self.face_direction == FACING_RIGHT:
                    return self.attack_right_textures_powerup[frame_rate]

        if consumable == PINK_CONSUMABLE:
            self.scale = 0.055
            if current_anim == IDLE:
                if self.face_direction == FACING_TOP:
                    return self.idle_up_textures_powerup_pink[frame_rate]
                elif self.face_direction == FACING_BOTTOM:
                    return self.idle_down_textures_powerup_pink[frame_rate]
                elif self.face_direction == FACING_LEFT:
                    return self.idle_left_side_textures_powerup_pink[frame_rate]
                elif self.face_direction == FACING_RIGHT:
                    return self.idle_right_side_textures_powerup_pink[frame_rate]

            if current_anim == WALK:
                if self.face_direction == FACING_TOP:
                    return self.walk_up_textures_powerup_pink[frame_rate]
                elif self.face_direction == FACING_BOTTOM:
                    return self.walk_down_textures_powerup_pink[frame_rate]
                elif self.face_direction == FACING_LEFT:
                    return self.walk_left_textures_powerup_pink[frame_rate]
                elif self.face_direction == FACING_RIGHT:
                    return self.walk_right_textures_powerup_pink[frame_rate]

            if current_anim == ATTACK_ANIM:
                if self.face_direction == FACING_TOP:
                    return self.attack_up_textures_powerup_pink[frame_rate]
                elif self.face_direction == FACING_BOTTOM:
                    return self.attack_down_textures_powerup_pink[frame_rate]
                elif self.face_direction == FACING_LEFT:
                    return self.attack_left_textures_powerup_pink[frame_rate]
                elif self.face_direction == FACING_RIGHT:
                    return self.attack_right_textures_powerup_pink[frame_rate]

    def set_texture_base_on_consumable(self, consumable, frame_rate, current_anim):
        available_textures_based_on_consumable = {
            DEFAULT_CONSUMABLE: self.set_texture_based_on_facing_position(frame_rate, current_anim, consumable=DEFAULT_CONSUMABLE),
            PINK_CONSUMABLE: self.set_texture_based_on_facing_position(frame_rate, current_anim, consumable=PINK_CONSUMABLE)
        }
        for consumable_key in available_textures_based_on_consumable:
            if consumable_key == consumable:
                return available_textures_based_on_consumable[consumable_key]

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
        idle_down_frame = self.idle_down_status // self.updates_per_frame
        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_BOTTOM:
            self.texture = self.idle_down_textures[idle_down_frame]
            self.idle_down_status = update_idle_down_anim(self.idle_down_status, len(PLAYER_IDLE_DOWN_SPRITES))

        idle_up_frame = self.idle_up_status // self.updates_per_frame
        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_TOP:
            self.texture = self.idle_up_textures[idle_up_frame]
            self.idle_up_status = update_idle_up_anim(self.idle_up_status, len(PLAYER_IDLE_UP_SPRITES))

        idle_side_frame = self.idle_side_status // self.updates_per_frame
        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_LEFT:
            self.texture = self.idle_left_side_textures[idle_side_frame]
            self.idle_side_status = update_idle_side_anim(self.idle_side_status, len(PLAYER_IDLE_SIDE_SPRITES))

        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_RIGHT:
            self.texture = self.idle_right_side_textures[idle_side_frame]
            self.idle_side_status = update_idle_side_anim(self.idle_side_status, len(PLAYER_IDLE_SIDE_SPRITES))

        # Powerup Idle animations
        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_BOTTOM and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, idle_down_frame, current_anim=IDLE)
            self.idle_down_status = update_idle_down_anim(self.idle_down_status, len(PLAYER_IDLE_DOWN_POWERUP_SPRITES))

        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_TOP and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, idle_up_frame, current_anim=IDLE)
            self.idle_up_status = update_idle_up_anim(self.idle_up_status, len(PLAYER_IDLE_UP_POWERUP_SPRITES))

        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_LEFT and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, idle_side_frame, current_anim=IDLE)
            self.idle_side_status = update_idle_side_anim(self.idle_side_status, len(PLAYER_IDLE_SIDE_POWERUP_SPRITES))

        if self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_RIGHT and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, idle_side_frame, current_anim=IDLE)
            self.idle_side_status = update_idle_side_anim(self.idle_side_status, len(PLAYER_IDLE_SIDE_POWERUP_SPRITES))

        # Walk down animation
        walk_down_frame = self.walk_down_status // self.updates_per_frame
        if self.change_y != 0 and self.face_direction == FACING_BOTTOM:
            self.texture = self.walk_down_textures[walk_down_frame]
            self.walk_down_status = update_walk_down_anim(self.walk_down_status, len(PLAYER_WALK_DOWN_SPRITES))

        # Walk down powerup animation
        if self.change_y != 0 and self.face_direction == FACING_BOTTOM and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, walk_down_frame, current_anim=WALK)
            self.walk_down_status = update_walk_down_anim(self.walk_down_status, len(PLAYER_WALK_DOWN_POWERUP_SPRITES))

        # Walk up animation
        walk_up_frame = self.walk_up_status // self.updates_per_frame
        if self.change_y != 0 and self.face_direction == FACING_TOP:
            self.texture = self.walk_up_textures[walk_up_frame]
            self.walk_up_status = update_walk_up_anim(self.walk_up_status, len(PLAYER_WALK_UP_SPRITES))

        # Walk up powerup animation
        if self.change_y != 0 and self.face_direction == FACING_TOP and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, walk_up_frame, current_anim=WALK)
            self.walk_up_status = update_walk_up_anim(self.walk_up_status, len(PLAYER_WALK_UP_POWERUP_SPRITES))

        # Sidewalk animations
        side_walk_frame = self.walk_side_status // self.updates_per_frame
        if self.change_x != 0 and self.face_direction == FACING_LEFT:
            self.texture = self.walk_left_textures[side_walk_frame]
            self.walk_side_status = update_side_walk_anim(self.walk_side_status, len(PLAYER_SIDE_WALK_SPRITES))
        elif self.change_x != 0 and self.face_direction == FACING_RIGHT:
            self.texture = self.walk_right_textures[side_walk_frame]
            self.walk_side_status = update_side_walk_anim(self.walk_side_status, len(PLAYER_SIDE_WALK_SPRITES))

        # Sidewalk powerup animations
        if self.change_x != 0 and self.face_direction == FACING_LEFT and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, side_walk_frame, current_anim=WALK)
            self.walk_side_status = update_side_walk_anim(self.walk_side_status, len(PLAYER_SIDE_WALK_POWERUP_SPRITES))
        elif self.change_x != 0 and self.face_direction == FACING_RIGHT and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, side_walk_frame, current_anim=WALK)
            self.walk_side_status = update_side_walk_anim(self.walk_side_status, len(PLAYER_SIDE_WALK_POWERUP_SPRITES))

        # Attack animations
        attack_down_frame = self.attack_down_status // self.updates_per_frame
        attack_up_frame = self.attack_up_status // self.updates_per_frame
        attack_side_frame = self.attack_side_status // self.updates_per_frame
        if self.attack == utils.constants.ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_BOTTOM:
            self.texture = self.attack_down_textures[attack_down_frame]
            self.attack_down_status = update_attack_down_anim(self.attack_down_status, len(PLAYER_ATTACK_DOWN_SPRITES))
        elif self.attack == utils.constants.ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_TOP:
            self.texture = self.attack_up_textures[attack_up_frame]
            self.attack_up_status = update_attack_up_anim(self.attack_up_status, len(PLAYER_ATTACK_UP_SPRITES))
        elif self.attack == utils.constants.ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_LEFT:
            self.texture = self.attack_left_textures[attack_side_frame]
            self.attack_side_status = update_attack_side_anim(self.attack_side_status, len(PLAYER_ATTACK_SIDE_SPRITES))
        elif self.attack == utils.constants.ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_RIGHT:
            self.texture = self.attack_right_textures[attack_side_frame]
            self.attack_side_status = update_attack_side_anim(self.attack_side_status, len(PLAYER_ATTACK_SIDE_SPRITES))

        # Attack powerup animations
        if self.attack == utils.constants.ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_BOTTOM and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, attack_down_frame, current_anim=ATTACK_ANIM)
            self.attack_down_status = update_attack_down_anim(self.attack_down_status, len(PLAYER_ATTACK_DOWN_POWERUP_SPRITES))
        elif self.attack == utils.constants.ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_TOP and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, attack_up_frame, current_anim=ATTACK_ANIM)
            self.attack_up_status = update_attack_up_anim(self.attack_up_status, len(PLAYER_ATTACK_UP_POWERUP_SPRITES))
        elif self.attack == utils.constants.ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_LEFT and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, attack_side_frame, current_anim=ATTACK_ANIM)
            self.attack_side_status = update_attack_side_anim(self.attack_side_status, len(PLAYER_ATTACK_SIDE_POWERUP_SPRITES))
        elif self.attack == utils.constants.ATTACK and self.change_x == 0 and self.change_y == 0 and self.face_direction == FACING_RIGHT and self.power_up == POWERUP_ENABLED:
            self.texture = self.set_texture_base_on_consumable(self.item_picked, attack_side_frame, current_anim=ATTACK_ANIM)
            self.attack_side_status = update_attack_side_anim(self.attack_side_status, len(PLAYER_ATTACK_SIDE_POWERUP_SPRITES))

        # Pick up animation
        pick_up_frame = self.pick_up_status // self.updates_per_frame
        if self.change_x == 0 and self.change_y == 0 and self.picking == PICKING:
            self.texture = self.pick_up_textures[pick_up_frame]
            self.pick_up_status, self.picking = update_pick_up_anim(self.pick_up_status)
