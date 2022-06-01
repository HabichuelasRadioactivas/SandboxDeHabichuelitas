import arcade

from load_assets import *


class SoundPlayer:
    def __init__(self):
        self.heroic_background_music = arcade.load_sound(BACKGROUND_MUSIC)  # load sound_player
        self.sword_sound = arcade.load_sound(SWORD_SOUND)
        self.player_walk_sound = arcade.load_sound(WALK_SOUND)
        self.etas_habichuela = arcade.load_sound(HABICHUELAS_SOUND)




class SoundPlayer:
    def __init__(self):
        self.heroic_background_music = arcade.play_sound(arcade.load_sound(BACKGROUND_MUSIC))  # load sound_player
        self.heroic_background_music.pause()  # pause the sound, so it doesn't start. Start sound with .play()
        self.attack_sound = arcade.play_sound(arcade.load_sound(SWORD_SOUND))
        self.attack_sound.pause()
        self.player_walk_sound = arcade.load_sound(WALK_SOUND)
        #self.player_walk_sound.pause()

        # self.xxx = arcade.play_sound(arcade.load_sound(XXX))
        # self.xxx.pause()

    def play_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music.play()
        if sound_name == "attack_sound":
            self.attack_sound.play()

            # self.play_sound(SWORD_SOUND)

        # elif sound_name == "xxx":
        # pass  # self.xxx.play()


    def pause_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music.pause()
        if sound_name == "sword.mp3":
            self.attack_sound.pause()
        elif sound_name == "xxx":
            pass
            # self.xxx.pause()



    def reload_sound(self, sound_name):
        if sound_name == "heroic_background_music":
            self.heroic_background_music = arcade.play_sound(arcade.load_sound(BACKGROUND_MUSIC), 0.5)
            self.heroic_background_music.pause()
        if sound_name == "sword.mp3":
            self.attack_sound.pause()
        elif sound_name == "xxx":
            # self.xxx = arcade.play_sound(arcade.load_sound(XXX))
            # self.xxx.pause()
            pass











