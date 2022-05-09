import arcade

# Open up a window
SCREEN_WIDTH = 800  # WIDTH
SCREEN_HEIGHT = 600  # HEIGHT
SCREEN_TITLE = "FINAL KNIGHT"  # SCREEN_TITLE

IDLE_SPRITES = [
    "_PNG/2_KNIGHT/_IDLE/_IDLE_000.png",
    "_PNG/2_KNIGHT/_IDLE/_IDLE_001.png",
    "_PNG/2_KNIGHT/_IDLE/_IDLE_002.png",
    "_PNG/2_KNIGHT/_IDLE/_IDLE_003.png",
    "_PNG/2_KNIGHT/_IDLE/_IDLE_004.png",
    "_PNG/2_KNIGHT/_IDLE/_IDLE_005.png",
    "_PNG/2_KNIGHT/_IDLE/_IDLE_006.png",
    ]

ATTACK_SPRITES = [
    "_PNG/2_KNIGHT/_ATTACK/_ATTACK_000.png",
    "_PNG/2_KNIGHT/_ATTACK/_ATTACK_001.png",
    "_PNG/2_KNIGHT/_ATTACK/_ATTACK_002.png",
    "_PNG/2_KNIGHT/_ATTACK/_ATTACK_003.png",
    "_PNG/2_KNIGHT/_ATTACK/_ATTACK_004.png",
    "_PNG/2_KNIGHT/_ATTACK/_ATTACK_005.png",
    "_PNG/2_KNIGHT/_ATTACK/_ATTACK_006.png",
]

DIE_SPRITES = [
    "_PNG/2_KNIGHT/_DIE/_DIE_000.png",
    "_PNG/2_KNIGHT/_DIE/_DIE_001.png",
    "_PNG/2_KNIGHT/_DIE/_DIE_002.png",
    "_PNG/2_KNIGHT/_DIE/_DIE_003.png",
    "_PNG/2_KNIGHT/_DIE/_DIE_004.png",
    "_PNG/2_KNIGHT/_DIE/_DIE_005.png",
    "_PNG/2_KNIGHT/_DIE/_DIE_006.png",
]

HURT_SPRITES = [
    "_PNG/2_KNIGHT/_HURT/HURT_000.png",
    "_PNG/2_KNIGHT/_HURT/HURT_001.png",
    "_PNG/2_KNIGHT/_HURT/HURT_002.png",
    "_PNG/2_KNIGHT/_HURT/HURT_003.png",
    "_PNG/2_KNIGHT/_HURT/HURT_004.png",
    "_PNG/2_KNIGHT/_HURT/HURT_005.png",
    "_PNG/2_KNIGHT/_HURT/HURT_006.png",
]

JUMP_SPRITES = [
    "_PNG/2_KNIGHT/_JUMP/_JUMP_000.png",
    "_PNG/2_KNIGHT/_JUMP/_JUMP_001.png",
    "_PNG/2_KNIGHT/_JUMP/_JUMP_002.png",
    "_PNG/2_KNIGHT/_JUMP/_JUMP_003.png",
    "_PNG/2_KNIGHT/_JUMP/_JUMP_004.png",
    "_PNG/2_KNIGHT/_JUMP/_JUMP_005.png",
    "_PNG/2_KNIGHT/_JUMP/_JUMP_006.png",
]

RUN_SPRITES = [
    "_PNG/2_KNIGHT/_RUN/_RUN_000.png",
    "_PNG/2_KNIGHT/_RUN/_RUN_001.png",
    "_PNG/2_KNIGHT/_RUN/_RUN_002.png",
    "_PNG/2_KNIGHT/_RUN/_RUN_003.png",
    "_PNG/2_KNIGHT/_RUN/_RUN_004.png",
    "_PNG/2_KNIGHT/_RUN/_RUN_005.png",
    "_PNG/2_KNIGHT/_RUN/_RUN_006.png",
]

WALK_SPRITES = [
    "_PNG/2_KNIGHT/_WALK/_WALK_000.png",
    "_PNG/2_KNIGHT/_WALK/_WALK_001.png",
    "_PNG/2_KNIGHT/_WALK/_WALK_002.png",
    "_PNG/2_KNIGHT/_WALK/_WALK_003.png",
    "_PNG/2_KNIGHT/_WALK/_WALK_004.png",
    "_PNG/2_KNIGHT/_WALK/_WALK_005.png",
    "_PNG/2_KNIGHT/_WALK/_WALK_006.png",
]

MOVEMENT_SPEED = 3
FACING_TOP = 0
FACING_RIGHT = 1
FACING_BOTTOM = 2
FACING_LEFT = 3
NOT_PRESSED = 99


SPRITE_SCALING = 1

ATTACK = 1
WAITING_ATTACK = 0
HEALTH_KNIGHT = 10

UPDATES_PER_FRAME = 7


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


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Set up the player info
        self.finalKnight_list = None
        self.finalKnight_sprite = None

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def setup(self):

        # Set up the player
        self.finalKnight_list = arcade.SpriteList()
        self.finalKnight_sprite = FinalKnight()

        # Player initial position  - Spawn Point
        self.finalKnight_sprite.center_x = 150
        self.finalKnight_sprite.center_y = 550

        self.finalKnight_list.append(self.knight_sprite)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

        arcade.draw_text('WASD to move', 5, SCREEN_HEIGHT - 21, arcade.color.BLACK, 12)

        self.finalKnight_list.draw()

    def on_update(self, delta_time):
        self.ball.update()

        """# Move the player
        self.finalKnight_list.update()
        self.finalKnight_list.update_animation()"""

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.A:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.ball.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.ball.change_y = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


main()
