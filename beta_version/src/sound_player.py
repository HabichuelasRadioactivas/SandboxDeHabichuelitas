import arcade

from load_assets import *


class SoundPlayer:
    def __init__(self):
        self.heroic_background_music = arcade.play_sound(arcade.load_sound(BACKGROUND_MUSIC),
                                                         0.4, looping=True)  # load sound_player
        self.heroic_background_music.pause()  # pause the sound, so it doesn't start. Start sound with .play()

        self.attack_sound = arcade.play_sound(arcade.load_sound(SWORD_SOUND))
        self.attack_sound.pause()

        self.player_walk_sound = arcade.play_sound(arcade.load_sound(WALK_SOUND), 0.3, looping=True)
        self.player_walk_sound.pause()

        self.power_up_sound = arcade.play_sound(arcade.load_sound(POWER_UP_SOUND), 2)
        self.power_up_sound.pause()

        self.picking_things_sound = arcade.play_sound(arcade.load_sound(PICKING_SOUND))
        self.picking_things_sound.pause()

    def play_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music.play()
        elif sound_name == "attack_sound":
            self.attack_sound.play()
        elif sound_name == "player_walk_sound":
            self.player_walk_sound.play()
        elif sound_name == "picking_things_sound":
            self.picking_things_sound.play()
        elif sound_name == "power_up_sound":
            self.power_up_sound.play()

    def pause_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music.pause()
        elif sound_name == "player_walk_sound":
            self.player_walk_sound.pause()
        elif sound_name == "attack_sound":
            self.attack_sound.pause()
        elif sound_name == "picking_things_sound":
            self.picking_things_sound.pause()
        elif sound_name == "power_up_sound":
            self.power_up_sound.pause()

    def reload_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music = arcade.play_sound(arcade.load_sound(BACKGROUND_MUSIC), 0.4, looping=True)
            self.heroic_background_music.pause()
        elif sound_name == "attack_sound":
            self.attack_sound = arcade.play_sound(arcade.load_sound(SWORD_SOUND))
            self.attack_sound.pause()
        elif sound_name == "player_walk_sound":
            self.player_walk_sound = arcade.play_sound(arcade.load_sound(WALK_SOUND), 0.3, looping=True)
            self.player_walk_sound.pause()
        elif sound_name == "picking_things_sound":
            self.picking_things_sound = arcade.play_sound(arcade.load_sound(PICKING_SOUND))
            self.picking_things_sound.pause()
        elif sound_name == "power_up_sound":
            self.power_up_sound = arcade.play_sound(arcade.load_sound(POWER_UP_SOUND), 2)
            self.power_up_sound.pause()
