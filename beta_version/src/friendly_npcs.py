from load_assets import *
from sound_player import SoundPlayer


class MrBean(arcade.AnimatedTimeBasedSprite):
    def __init__(self):
        super().__init__()

        # Texture scaling

        self.scale = 0.3

        # Idle textures
        self.celebrating = arcade.load_texture(MR_BEAN_SPRITES[0])
        self.on_one_foot = arcade.load_texture(MR_BEAN_SPRITES[1])
        self.waiting = arcade.load_texture(MR_BEAN_SPRITES[2])

        # Set initial texture
        self.texture = self.waiting

        self.talked_to_bean = False



    def update(self):
        # Move player
        pass

    def update_animation(self, delta_time: float = 1/60):
        pass

    def celebrate(self):
        self.texture = self.celebrating

    def wait(self):
        self.texture = self.waiting

    def is_near(self, x, y):
        return 670 < x and 70 < y < 110

    def talk_to_bean(self):
        self.talked_to_bean = True



        #self.sound_player.pause_sound(sound_name="player_walk_sound")
