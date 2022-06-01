import arcade

from load_assets import *


class SoundPlayer:
    def __init__(self):
        self.heroic_background_music = arcade.play_sound(arcade.load_sound(BACKGROUND_MUSIC), 0.5)  # load sound_player
        self.heroic_background_music.pause()  # pause the sound, so it doesn't start. Start sound with .play()

        # self.xxx = arcade.play_sound(arcade.load_sound(XXX))
        # self.xxx.pause()

    def play_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music.play()
        elif sound_name == "xxx":
            pass  # self.xxx.play()

    def pause_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music.pause()
        elif sound_name == "xxx":
            pass  # self.xxx.pause()

    def reload_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music = arcade.play_sound(arcade.load_sound(BACKGROUND_MUSIC), 0.5)
            self.heroic_background_music.pause()
        elif sound_name == "xxx":
            # self.xxx = arcade.play_sound(arcade.load_sound(XXX))
            # self.xxx.pause()
            pass
