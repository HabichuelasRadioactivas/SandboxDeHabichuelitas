import arcade

from load_assets import *


class SoundPlayer:
    def __init__(self):
        self.heroic_background_music = arcade.play_sound(arcade.load_sound(BACKGROUND_MUSIC))  # load sound_player
        self.heroic_background_music.pause()  # pause the sound, so it doesn't start. Start sound with .play()

        self.attack_sound = arcade.play_sound(arcade.load_sound(SWORD_SOUND))
        self.attack_sound.pause()

        self.player_walk_sound = arcade.play_sound(arcade.load_sound(WALK_SOUND))
        self.player_walk_sound.pause()

        self.power_up_sound = arcade.play_sound(arcade.load_sound(POWER_UP_SOUND))
        self.power_up_sound.pause()


        self.picking_things_sound = arcade.play_sound(arcade.load_sound(PICKING_SOUND))
        self.picking_things_sound.pause()

        # self.xxx = arcade.play_sound(arcade.load_sound(XXX))
        # self.xxx.pause()

    def play_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music.play()
        if sound_name == "attack_sound":
            self.attack_sound.play()
        if sound_name == "player_walk_sound":
            self.player_walk_sound.play()
        if sound_name == "picking_things_sound":
            self.picking_things_sound.play()


        # elif sound_name == "xxx":
        # pass  # self.xxx.play()


    def pause_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music.pause()

        if sound_name == "player_walk_sound":
            self.player_walk_sound.pause()
        if sound_name == "attack_sound":
            self.play_sound.pause()
        if sound_name == "picking_things_sound":
            self.picking_things_sound.pause()




        elif sound_name == "xxx":
            pass
            # self.xxx.pause()



    def reload_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music = arcade.play_sound(arcade.load_sound(BACKGROUND_MUSIC), 0.5)
            self.heroic_background_music.pause()
        if sound_name == "attack_sound":
            self.attack_sound = arcade.play_sound(arcade.load_sound(SWORD_SOUND))
            self.attack_sound.pause()
        if sound_name == "player_walk_sound":
            self.player_walk_sound = arcade.play_sound(arcade.load_sound(WALK_SOUND))
            self.player_walk_sound.pause()
        if sound_name == "picking_things_sound":
            self.picking_things_sound = arcade.play_sound(arcade.load_sound(PICKING_SOUND))
            self.picking_things_sound.pause()





        elif sound_name == "xxx":
            # self.xxx = arcade.play_sound(arcade.load_sound(XXX))
            # self.xxx.pause()
            pass











