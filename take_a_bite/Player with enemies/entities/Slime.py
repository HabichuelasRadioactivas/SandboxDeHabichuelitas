import arcade

import utils.constants
from utils.texture_loader import load_textures
from utils.anims_state_updater import *

IDLE_UP_SPRITES = [
    "SlimeAnimations/SlimeIdle/SlimeIdleTop00.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleTop01.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleTop02.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleTop03.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleTop04.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleTop05.png",
]

IDLE_LEFT_SPRITES = [
    "SlimeAnimations/SlimeIdle/SlimeIdleLeft00.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleLeft01.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleLeft02.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleLeft03.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleLeft04.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleLeft05.png",
]

IDLE_RIGHT_SPRITES = [
    "SlimeAnimations/SlimeIdle/SlimeIdleRight00.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleRight01.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleRight02.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleRight03.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleRight04.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleRight05.png",
]

IDLE_DOWN_SPRITES = [
    "SlimeAnimations/SlimeIdle/SlimeIdleDown00.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleDown01.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleDown02.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleDown03.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleDown04.png",
    "SlimeAnimations/SlimeIdle/SlimeIdleDown05.png",
]

ATTACK_UP_SPRITES = [
    "SlimeAnimations/SlimeDamage/SlimeDamageTop00.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageTop01.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageTop02.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageTop03.png",
]

ATTACK_LEFT_SPRITES = [
    "SlimeAnimations/SlimeDamage/SlimeDamageLeft00.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageLeft01.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageLeft02.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageLeft03.png",
]

ATTACK_RIGHT_SPRITES = [
    "SlimeAnimations/SlimeDamage/SlimeDamageRight00.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageRight01.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageRight02.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageRight03.png",
]

ATTACK_DOWN_SPRITES = [
    "SlimeAnimations/SlimeDamage/SlimeDamageDown00.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageDown01.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageDown02.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageDown03.png",
]

DIE_SPRITES = [
    "SlimeAnimations/SlimeDeath/SlimeDeath00.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath00.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath01.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath01.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath02.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath02.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath03.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath03.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath04.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath04.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath05.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath05.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath06.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath06.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath07.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath07.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath08.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath08.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath09.png",
    "SlimeAnimations/SlimeDeath/SlimeDeath09.png",
]

WALK_UP_SPRITES = [
    "SlimeAnimations/SlimeWalk/SlimeWalkTop00.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkTop01.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkTop02.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkTop03.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkTop04.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkTop05.png",
]

WALK_LEFT_SPRITES = [
    "SlimeAnimations/SlimeWalk/SlimeWalkLeft00.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkLeft01.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkLeft02.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkLeft03.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkLeft04.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkLeft05.png",
]

WALK_RIGHT_SPRITES = [
    "SlimeAnimations/SlimeWalk/SlimeWalkRight00.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkRight01.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkRight02.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkRight03.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkRight04.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkRight05.png",
]

WALK_DOWN_SPRITES = [
    "SlimeAnimations/SlimeWalk/SlimeWalkDown00.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkDown01.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkDown02.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkDown03.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkDown04.png",
    "SlimeAnimations/SlimeWalk/SlimeWalkDown05.png",
]

HURT_SPRITES = [
    "SlimeAnimations/SlimeDamage/SlimeDamageTop03.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageTop02.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageTop03.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageTop01.png",
    "SlimeAnimations/SlimeDamage/SlimeDamageTop03.png",
]

SPRITE_SCALING_SLIME = 0.4
SPRITE_HEALTH_SLIME = 0.6


class Slime(arcade.AnimatedTimeBasedSprite):
    """Slime Class"""

    def __init__(self, enemy_type='slime'):
        super().__init__()

        # Set type of enemy (skeleton, goblin, slime, knight)
        self.enemy_type = enemy_type

        # Set facing direction
        self.face_direction = FACING_BOTTOM

        # Set initial attack state
        self.attack = False

        # Texture scaling
        self.scale = SPRITE_SCALING_SLIME

        # Initial animations status
        self.idle_status = 0
        self.idle_down_status = 0
        self.idle_up_status = 0
        self.idle_side_status = 0
        self.idle_right_status = 0
        self.idle_left_status = 0
        self.walk_status = 0
        self.walk_down_status = 0
        self.walk_up_status = 0
        self.walk_side_status = 0
        self.walk_right_status = 0
        self.walk_left_status = 0
        self.attack_status = 0
        self.attack_down_status = 0
        self.attack_up_status = 0
        self.attack_side_status = 0
        self.attack_right_status = 0
        self.attack_left_status = 0
        self.dead_status = 0
        self.hit_status = 0

        # Enemy frame rate
        self.updates_per_frame = UPDATES_PER_FRAME
        # Enemy health points
        self.health_points = SPRITE_HEALTH_SLIME

        # Toggle between left & right run anims
        self.left_or_right = None

        # Enemy hit by player state variable
        self.hit = False

        # Enemy dead state variable
        self.enemy_dead = False
        self.destroy_enemy = False

        # Idle textures
        self.idle_down_textures = []
        load_textures(self.idle_down_textures, IDLE_DOWN_SPRITES)

        self.idle_up_textures = []
        load_textures(self.idle_up_textures, IDLE_UP_SPRITES)

        self.idle_left_side_textures = []
        load_textures(self.idle_left_side_textures, IDLE_LEFT_SPRITES)

        self.idle_right_side_textures = []
        load_textures(self.idle_right_side_textures, IDLE_RIGHT_SPRITES)

        self.idle_sprites_len = len(IDLE_UP_SPRITES)

        # Walk textures
        self.walk_down_textures = []
        load_textures(self.walk_down_textures, WALK_DOWN_SPRITES)

        self.walk_left_textures = []
        load_textures(self.walk_left_textures, WALK_LEFT_SPRITES)

        self.walk_right_textures = []
        load_textures(self.walk_right_textures, WALK_RIGHT_SPRITES)

        self.walk_up_textures = []
        load_textures(self.walk_up_textures, WALK_UP_SPRITES)

        self.walk_sprites_len = len(WALK_UP_SPRITES)

        # Attack textures
        self.attack_down_textures = []
        load_textures(self.attack_down_textures, ATTACK_DOWN_SPRITES)

        self.attack_up_textures = []
        load_textures(self.attack_up_textures, ATTACK_UP_SPRITES)

        self.attack_left_textures = []
        load_textures(self.attack_left_textures, ATTACK_LEFT_SPRITES)

        self.attack_right_textures = []
        load_textures(self.attack_right_textures, ATTACK_RIGHT_SPRITES)

        self.attack_sprites_len = 4

        # Dead textures
        self.dead_textures = []
        self.dead_sprites_len = 0
        load_textures(self.dead_textures, DIE_SPRITES)
        self.dead_sprites_len = len(DIE_SPRITES)

        # Hit textures
        self.hit_textures = []
        self.hit_sprites_len = 0
        load_textures(self.hit_textures, HURT_SPRITES)
        self.hit_sprites_len = len(HURT_SPRITES)

        # Set initial texture
        self.texture = self.idle_up_textures[0]

    def update(self):
        # Move enemy
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
        if self.change_x == 0 and self.change_y == 0 and not self.hit:
            idle_frame = self.idle_status // self.updates_per_frame
            if self.left_or_right == 'right':
                self.texture = self.idle_right_side_textures[idle_frame]
            else:
                self.texture = self.idle_left_side_textures[idle_frame]

            self.idle_status = update_idle_down_anim(self.idle_status, self.idle_sprites_len)

        elif self.change_x != 0 and self.change_y != 0 and not self.hit:
            frame = self.walk_status // self.updates_per_frame
            if self.left_or_right == 'right':
                self.texture = self.walk_right_textures[frame]
            else:
                self.texture = self.walk_left_textures[frame]

            self.walk_status = update_idle_down_anim(self.walk_status, self.walk_sprites_len)

        if self.hit:
            if self.hit_status == len(self.hit_textures) - 1:
                self.hit = False
            else:
                hit_frame = self.hit_status
                self.texture = self.hit_textures[hit_frame]
                self.hit_status = update_idle_down_anim(self.hit_status, self.hit_sprites_len)

        if self.enemy_dead:
            if self.dead_status == len(self.dead_textures) - 1:
                self.destroy_enemy = True
            else:
                dead_frame = self.dead_status
                self.texture = self.dead_textures[dead_frame]
                self.dead_status = update_idle_down_anim(self.dead_status, self.dead_sprites_len)

        if self.attack:
            if self.attack_status == len(self.attack_right_textures) - 1:
                self.attack = False
            else:
                attack_frame = self.attack_status
                if self.left_or_right == 'right':
                    self.texture = self.attack_right_textures[attack_frame]
                else:
                    self.texture = self.attack_left_textures[attack_frame]

                self.attack_status = update_idle_down_anim(self.attack_status, self.attack_sprites_len)
