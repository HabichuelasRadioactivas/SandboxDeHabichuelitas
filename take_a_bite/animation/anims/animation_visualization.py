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
SCREEN_WIDTH = 800 # WIDTH
SCREEN_HEIGHT = 600 # HEIGHT
SCREEN_TITLE = "Animation Visualization" # SCREEN_TITLE

CHARACTER_SPRITES = [
        "images/_Crouch.png",
        "images/_SlideTransitionEnd.png",
]

IDLE_SPRITES = [
    "images/idle_anim/tile000.png",
    "images/idle_anim/tile001.png",
    "images/idle_anim/tile002.png",
    "images/idle_anim/tile003.png",
    "images/idle_anim/tile004.png",
    "images/idle_anim/tile005.png",
    "images/idle_anim/tile006.png",
    "images/idle_anim/tile007.png",
    "images/idle_anim/tile008.png",
    "images/idle_anim/tile009.png",
]

RUN_SPRITES = [
    "images/run_anim/tile000.png",
    "images/run_anim/tile001.png",
    "images/run_anim/tile002.png",
    "images/run_anim/tile003.png",
    "images/run_anim/tile004.png",
    "images/run_anim/tile005.png",
    "images/run_anim/tile006.png",
    "images/run_anim/tile007.png",
    "images/run_anim/tile008.png",
    "images/run_anim/tile009.png",
]

ATTACK_SPRITES = [
    "images/attack_anim/tile000.png",
    "images/attack_anim/tile001.png",
    "images/attack_anim/tile002.png",
    "images/attack_anim/tile003.png",
]

MOVEMENT_SPEED = 5

SPRITE_SCALING = 1

FACING_TOP = 0
FACING_RIGHT = 1
FACING_BOTTOM = 2
FACING_LEFT = 3

ATTACK = 1
WAITING_ATTACK = 0


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

        # Texture scaling
        self.scale = SPRITE_SCALING

        # State variables
        self.attack = WAITING_ATTACK

        # Initial animations status
        self.idle_status = 0
        self.run_status = 0
        self.attack_status = 0

        # Load textures
        self.top_facing_texture = arcade.load_texture(CHARACTER_SPRITES[0])
        self.bottom_facing_texture = arcade.load_texture(CHARACTER_SPRITES[1])

        # Idle textures
        self.idle_textures = []
        for i in range(len(IDLE_SPRITES)):
            self.idle_textures.append(arcade.load_texture(IDLE_SPRITES[i]))

        # Run textures
        self.run_right_textures = []
        for i in range(len(RUN_SPRITES)):
            self.run_right_textures.append(arcade.load_texture(RUN_SPRITES[i]))
        self.run_left_textures = []
        for i in range(len(RUN_SPRITES)):
            self.run_left_textures.append(arcade.load_texture(RUN_SPRITES[i], flipped_horizontally=True))

        # Attack textures
        self.attack_right_textures = []
        for i in range(len(ATTACK_SPRITES)):
            self.attack_right_textures.append(arcade.load_texture(ATTACK_SPRITES[i]))
        self.attack_left_textures = []
        for i in range(len(ATTACK_SPRITES)):
            self.attack_left_textures.append(arcade.load_texture(ATTACK_SPRITES[i], flipped_horizontally=True))

        # Set initial texture
        self.texture = self.idle_textures[0]


    # Helper functions
    def update_idle_anim(self):
        if self.idle_status == len(IDLE_SPRITES) - 1:
            self.idle_status = 0
        else:
            self.idle_status += 1

    def update_run_anim(self):
        if self.run_status == len(RUN_SPRITES) - 1:
            self.run_status = 0
        else:
            self.run_status += 1

    def update_attack_anim(self):
        if self.attack_status == len(ATTACK_SPRITES) - 1:
            self.attack_status = 0
        else:
            self.attack_status += 1

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
        if self.face_direction == FACING_TOP:
            self.texture = self.top_facing_texture
        elif self.face_direction == FACING_RIGHT:
            self.texture = self.run_right_textures[self.run_status]
            self.update_run_anim()
        elif self.face_direction == FACING_BOTTOM:
            self.texture = self.bottom_facing_texture
        elif self.face_direction == FACING_LEFT:
            self.texture = self.run_left_textures[self.run_status]
            self.update_run_anim()

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_textures[self.idle_status]
            self.update_idle_anim()

        # Attack animation
        if self.attack == ATTACK and self.face_direction == FACING_LEFT:
            self.texture = self.attack_left_textures[self.attack_status]
            self.update_attack_anim()
        elif self.attack == ATTACK and self.face_direction == FACING_RIGHT:
            self.texture = self.attack_right_textures[self.attack_status]
            self.update_attack_anim()


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
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.player_sprite)


    def on_draw(self):
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()


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




def main():
    """Main method"""
    wn = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    wn.setup()
    arcade.run()


if __name__ == '__main__':
    main()
