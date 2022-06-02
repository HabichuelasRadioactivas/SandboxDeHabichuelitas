from load_assets import *
from anims_state_updater import *

BOSS_STATE = 0
BOSS_SCALE = 0.1
BOSS_MOVEMENT_SPEED = 2
BOSS_HEALTH_POINTS = 10


class FinalKnight(arcade.AnimatedTimeBasedSprite):
    """Enemy Class"""
    def __init__(self, enemy_type='finalKnight'):
        super().__init__()

        # Set type of enemy (skeleton, goblin, slime)
        self.enemy_type = enemy_type

        # Set facing direction
        self.face_direction = FACING_BOTTOM

        # Set initial attack state
        self.attack = False

        # Set state
        self.state = BOSS_STATE
        self.scale = BOSS_SCALE
        self.movement_speed = BOSS_MOVEMENT_SPEED
        self.health_points = BOSS_HEALTH_POINTS

        # Initial animations status
        self.idle_status = 0
        self.walk_status = 0
        self.attack_status = 0
        self.hit_status = 0
        self.dead_status = 0

        # Enemy frame rate
        self.updates_per_frame = UPDATES_PER_FRAME

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
        load_textures(self.idle_right_textures, ENEMY_KNIGHT_IDLE_SPRITES)
        load_textures(self.idle_left_textures, ENEMY_KNIGHT_IDLE_SPRITES, flip_hor=True)
        self.idle_sprites_len = len(ENEMY_KNIGHT_IDLE_SPRITES)

        # Run textures
        self.run_right_textures = []
        self.run_left_textures = []
        load_textures(self.run_right_textures, ENEMY_KNIGHT_RUN_SPRITES)
        load_textures(self.run_left_textures, ENEMY_KNIGHT_RUN_SPRITES, flip_hor=True)
        self.run_sprites_len = len(ENEMY_KNIGHT_RUN_SPRITES)

        # Hit textures
        self.hit_right_textures = []
        self.hit_left_textures = []
        load_textures(self.hit_right_textures, ENEMY_KNIGHT_HIT_SPRITES)
        load_textures(self.hit_left_textures, ENEMY_KNIGHT_HIT_SPRITES, flip_hor=True)
        self.hit_sprites_len = len(ENEMY_KNIGHT_HIT_SPRITES)

        # Dead textures
        self.dead_right_textures = []
        self.dead_left_textures = []
        load_textures(self.dead_right_textures, ENEMY_KNIGHT_DEAD_SPRITES)
        load_textures(self.dead_left_textures, ENEMY_KNIGHT_DEAD_SPRITES, flip_hor=True)
        self.dead_sprites_len = len(ENEMY_KNIGHT_DEAD_SPRITES)

        # Attack textures
        self.attack_right_textures = []
        self.attack_left_textures = []
        load_textures(self.attack_right_textures, ENEMY_KNIGHT_ATTACK_SPRITES)
        load_textures(self.attack_left_textures, ENEMY_KNIGHT_ATTACK_SPRITES, flip_hor=True)
        self.attack_sprites_len = len(ENEMY_KNIGHT_ATTACK_SPRITES)

        # Set initial texture
        self.texture = self.idle_right_textures[0]

    def update(self):
        # Move enemy
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.health_points <= 5:
            self.state = 1
        if self.state == 1:
            self.scale = BOSS_SCALE * 1.4
            self.movement_speed = BOSS_MOVEMENT_SPEED * 2

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