"""
Sample program to view characters animation tiles on row
"""

"""
TODO:
- Change animations speed,
- Add walk up, down animations
"""

# arcade library
import arcade

# Open up a window
SCREEN_WIDTH = 800  # WIDTH
SCREEN_HEIGHT = 600  # HEIGHT
SCREEN_TITLE = "Animation Visualization"  # SCREEN_TITLE

IDLE_DOWN_SPRITES = [
    "assets/idle_anim/tile000.png",
    "assets/idle_anim/tile001.png",
    "assets/idle_anim/tile002.png",
    "assets/idle_anim/tile003.png",
    "assets/idle_anim/tile004.png",
]

IDLE_UP_SPRITES = [
    "assets/idle_up_anim/tile000.png",
    "assets/idle_up_anim/tile001.png",
    "assets/idle_up_anim/tile002.png",
    "assets/idle_up_anim/tile003.png",
    "assets/idle_up_anim/tile004.png",
]

IDLE_SIDE_SPRITES = [
    "assets/idle_side_anim/tile000.png",
    "assets/idle_side_anim/tile001.png",
    "assets/idle_side_anim/tile002.png",
    "assets/idle_side_anim/tile003.png",
    "assets/idle_side_anim/tile004.png",
]

WALK_DOWN_SPRITES = [
    "assets/walk_down_anim/tile000.png",
    "assets/walk_down_anim/tile001.png",
    "assets/walk_down_anim/tile002.png",
    "assets/walk_down_anim/tile003.png",
    "assets/walk_down_anim/tile004.png",
    "assets/walk_down_anim/tile005.png",
]

WALK_UP_SPRITES = [
    "assets/walk_up_anim/tile000.png",
    "assets/walk_up_anim/tile001.png",
    "assets/walk_up_anim/tile002.png",
    "assets/walk_up_anim/tile003.png",
    "assets/walk_up_anim/tile004.png",
    "assets/walk_up_anim/tile005.png",
]

SIDE_WALK_SPRITES = [
    "assets/side_walk_anim/tile000.png",
    "assets/side_walk_anim/tile001.png",
    "assets/side_walk_anim/tile002.png",
    "assets/side_walk_anim/tile003.png",
    "assets/side_walk_anim/tile004.png",
    "assets/side_walk_anim/tile005.png",
]

ATTACK_DOWN_SPRITES = [
    "assets/attack_down_anim/tile000.png",
    "assets/attack_down_anim/tile001.png",
    "assets/attack_down_anim/tile002.png",
]

ATTACK_UP_SPRITES = [
    "assets/attack_up_anim/tile000.png",
    "assets/attack_up_anim/tile001.png",
    "assets/attack_up_anim/tile002.png",
]

ATTACK_SIDE_SPRITES = [
    "assets/attack_side_anim/tile000.png",
    "assets/attack_side_anim/tile001.png",
    "assets/attack_side_anim/tile002.png",
]

PICK_UP_SPRITES = [
    "assets/pick_up_anim/tile000.png",
    "assets/pick_up_anim/tile001.png",
    "assets/pick_up_anim/tile002.png",
    "assets/pick_up_anim/tile003.png",
    "assets/pick_up_anim/tile004.png",
]

MOVEMENT_SPEED = 5

SPRITE_SCALING = 2

FACING_TOP = 0
FACING_RIGHT = 1
FACING_BOTTOM = 2
FACING_LEFT = 3
NOT_PRESSED = 99

ATTACK = 1
WAITING_ATTACK = 0

PICKING = 1
WAITING_PICKING = 0

UPDATES_PER_FRAME = 7


def load_texture_pair(filename):
    """
    Load a texture pair, with mirror image as second one
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]


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
        for i in range(len(IDLE_DOWN_SPRITES)):
            self.idle_down_textures.append(arcade.load_texture(IDLE_DOWN_SPRITES[i]))

        self.idle_up_textures = []
        for i in range(len(IDLE_UP_SPRITES)):
            self.idle_up_textures.append(arcade.load_texture(IDLE_UP_SPRITES[i]))

        # Left side idle
        self.idle_left_side_textures = []
        for i in range(len(IDLE_SIDE_SPRITES)):
            self.idle_left_side_textures.append(arcade.load_texture(IDLE_SIDE_SPRITES[i]))

        # Right side idle
        self.idle_right_side_textures = []
        for i in range(len(IDLE_SIDE_SPRITES)):
            self.idle_right_side_textures.append(arcade.load_texture(IDLE_SIDE_SPRITES[i], flipped_horizontally=True))

        # Walk down textures
        self.walk_down_textures = []
        for i in range(len(WALK_DOWN_SPRITES)):
            self.walk_down_textures.append(arcade.load_texture(WALK_DOWN_SPRITES[i]))

        # Walk up textures
        self.walk_up_textures = []
        for i in range(len(WALK_UP_SPRITES)):
            self.walk_up_textures.append(arcade.load_texture(WALK_UP_SPRITES[i]))

        # Walk left textures
        self.walk_left_textures = []
        for i in range(len(SIDE_WALK_SPRITES)):
            self.walk_left_textures.append(arcade.load_texture(SIDE_WALK_SPRITES[i]))

        # Walk right textures
        self.walk_right_textures = []
        for i in range(len(SIDE_WALK_SPRITES)):
            self.walk_right_textures.append(arcade.load_texture(SIDE_WALK_SPRITES[i], flipped_horizontally=True))

        # Attack down textures
        self.attack_down_textures = []
        for i in range(len(ATTACK_DOWN_SPRITES)):
            self.attack_down_textures.append(arcade.load_texture(ATTACK_DOWN_SPRITES[i]))

        # Attack up textures
        self.attack_up_textures = []
        for i in range(len(ATTACK_UP_SPRITES)):
            self.attack_up_textures.append(arcade.load_texture(ATTACK_UP_SPRITES[i]))

        # Attack left textures
        self.attack_left_textures = []
        for i in range(len(ATTACK_SIDE_SPRITES)):
            self.attack_left_textures.append(arcade.load_texture(ATTACK_SIDE_SPRITES[i]))

        # Attack right textures
        self.attack_right_textures = []
        for i in range(len(ATTACK_SIDE_SPRITES)):
            self.attack_right_textures.append(arcade.load_texture(ATTACK_SIDE_SPRITES[i], flipped_horizontally=True))

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

        # Pick up animation
        pick_up_frame = self.pick_up_status // UPDATES_PER_FRAME
        if self.change_x == 0 and self.change_y == 0 and self.picking == PICKING:
            self.texture = self.pick_up_textures[pick_up_frame]
            self.update_pick_up_anim()


class MyGame(arcade.Window):
    """Custom window class"""

    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        # Set bg color
        arcade.set_background_color(arcade.csscolor.WHITE)

        # Set up the player info
        self.player_list = None
        self.player_sprite = None

    def setup(self):
        # Set up the player
        self.player_list = arcade.SpriteList()
        self.player_sprite = Player()

        # Player initial position
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2

        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

        arcade.draw_text('Arrow keys to move, hold X to attack, C to pick up', 5, SCREEN_HEIGHT - 21, arcade.color.BLACK, 12)

    def on_update(self, delta_time):
        # Move the player
        self.player_list.update()
        self.player_list.update_animation()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.face_direction = FACING_TOP
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.face_direction = FACING_BOTTOM
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.face_direction = FACING_LEFT
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.face_direction = FACING_RIGHT
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.X:
            self.player_sprite.attack = ATTACK

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.X:
            self.player_sprite.attack = WAITING_ATTACK
        elif key == arcade.key.C:
            self.player_sprite.picking = PICKING


def main():
    """Main method"""
    wn = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    wn.setup()
    arcade.run()


if __name__ == '__main__':
    main()
