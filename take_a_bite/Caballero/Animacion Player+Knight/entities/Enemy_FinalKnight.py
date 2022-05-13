import arcade
from utils.texture_loader import load_textures
from utils.anims_state_updater import *


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

SPRITE_SCALING_KNIGHT = 0.1


class Enemy(arcade.AnimatedTimeBasedSprite):
    """Enemy Class"""
    def __init__(self, enemy_type='finalKnight'):
        super().__init__()

        # Set type of enemy (skeleton, goblin, slime, knight)
        self.enemy_type = enemy_type

        # Set facing direction
        self.face_direction = FACING_BOTTOM

        # Set initial attack state
        self.attack = False

        # Texture scaling
        self.scale = SPRITE_SCALING_KNIGHT

        # Initial animations status
        self.idle_status = 0
        self.walk_status = 0
        self.run_status = 0
        self.attack_status = 0
        self.hit_status = 0
        self.dead_status = 0

        # Enemy frame rate
        self.updates_per_frame = UPDATES_PER_FRAME

        # Enemy health points
        self.health_points = 10

        # Toggle between left & right run anims
        self.left_or_right = None

        # Enemy hit by player state variable
        self.hit = False

        # Enemy dead state variable
        self.enemy_dead = False
        self.destroy_enemy = False

        # Idle textures
        self.idle_right_textures = []
        self.idle_left_textures = []
        self.idle_sprites_len = 0
        load_textures(self.idle_right_textures, IDLE_SPRITES)
        load_textures(self.idle_left_textures, IDLE_SPRITES, flip_hor=True)
        self.idle_sprites_len = len(IDLE_SPRITES)

        # Run textures
        self.run_right_textures = []
        self.run_left_textures = []
        self.run_sprites_len = 0
        load_textures(self.run_right_textures, RUN_SPRITES)
        load_textures(self.run_left_textures, RUN_SPRITES, flip_hor=True)
        self.run_sprites_len = len(RUN_SPRITES)

        # Hit textures
        self.hit_right_textures = []
        self.hit_left_textures = []
        self.hit_sprites_len = 0
        load_textures(self.hit_right_textures, HURT_SPRITES)
        load_textures(self.hit_left_textures, HURT_SPRITES, flip_hor=True)
        self.hit_sprites_len = len(HURT_SPRITES)

        # Dead textures
        self.dead_right_textures = []
        self.dead_left_textures = []
        self.dead_sprites_len = 0
        load_textures(self.dead_right_textures, DIE_SPRITES)
        load_textures(self.dead_left_textures, DIE_SPRITES, flip_hor=True)
        self.dead_sprites_len = len(DIE_SPRITES)

        # Attack textures
        self.attack_right_textures = []
        self.attack_left_textures = []
        self.attack_sprites_len = 0
        load_textures(self.attack_right_textures, ATTACK_SPRITES)
        load_textures(self.attack_left_textures, ATTACK_SPRITES, flip_hor=True)
        self.attack_sprites_len = len(ATTACK_SPRITES)

        # Set initial texture
        self.texture = self.run_right_textures[0]

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
                self.texture = self.idle_right_textures[idle_frame]
            else:
                self.texture = self.idle_left_textures[idle_frame]

            self.idle_status = update_idle_down_anim(self.idle_status, self.idle_sprites_len)

        elif self.change_x != 0 and self.change_y != 0 and not self.hit:
            frame = self.walk_status // self.updates_per_frame
            if self.left_or_right == 'right':
                self.texture = self.run_right_textures[frame]
            else:
                self.texture = self.run_left_textures[frame]

            self.walk_status = update_idle_down_anim(self.walk_status, self.run_sprites_len)

        if self.hit:
            if self.hit_status == len(self.hit_right_textures) - 1:
                self.hit = False
            else:
                hit_frame = self.hit_status
                if self.left_or_right == 'right':
                    self.texture = self.hit_right_textures[hit_frame]
                else:
                    self.texture = self.hit_left_textures[hit_frame]

                self.hit_status = update_idle_down_anim(self.hit_status, self.hit_sprites_len)

        if self.enemy_dead:
            if self.dead_status == len(self.dead_right_textures) - 1:
                self.destroy_enemy = True
            else:
                dead_frame = self.dead_status
                if self.left_or_right == 'right':
                    self.texture = self.dead_right_textures[dead_frame]
                else:
                    self.texture = self.dead_left_textures[dead_frame]

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