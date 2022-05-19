import arcade



class BeanAHero(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Sound")

        #pantalla inicial
        self.start_playing = arcade.load_sound("heroic-story-drums-ampamp-bass-9827.mp3")


        #clik en alguna opcion
        self.sonido_control = arcade.load_sound("click-21156.mp3")

        #cambiar sala
        self.door_open = arcade.load_sound("qubodup-DoorOpen07.flac")

        #volver a sala anterior
        self.door_closed = arcade.load_sound("qubodup-DoorClose07.flac")

        #el personaje anda
        self.andar = arcade.load_sound("mixkit-crunchy-road-fast-walking-loop-1274.wav")

        #el personaje se come la habichuela
        self.eats_habichuela = arcade.load_sound("habichuelas.mp3")

        #momento de la batalla
        self.pelea = arcade.load_sound("mixkit-tactical-drone-ambience-2744.wav")

        #golpe al personaje
        self.golpe = arcade.load_sound("mixkit-boxer-getting-hit-2055.wav")

        #enemigos se rien
        self.enemigos = arcade.load_sound("mixkit-evil-dwarf-laugh-421.wav")

        #el enemigo jefe se rie
        self.risa_enemigo_jefe = arcade.load_sound("mixkit-human-male-casual-laugh-411.wav")

        #el caballero da al enemigo en la pelea
        self.golpe_enemigo = arcade.load_sound("ouch-sound-effect-30-11844.mp3")



    def on_key_press(self, key, modifiers):

        if key == arcade.key.D:
            arcade.play_sound(self.door_open)
        if key == arcade.key.A:
            arcade.play_sound(self.door_closed)
        if key == arcade.key.R:
            arcade.play_sound(self.eats_habichuela)
        if key == arcade.key.ENTER:
            arcade.play_sound(self.start_playing)
        if key == arcade.key.K:
            arcade.play_sound(self.sonido_control)
        if key == arcade.key.Y:
            arcade.play_sound(self.golpe)
        if key == arcade.key.KEY_1:
            arcade.play_sound(self.andar)
        if key == arcade.key.KEY_2:
            arcade.play_sound(self.enemigos)
        if key == arcade.key.KEY_3:
            arcade.play_sound(self.risa_enemigo_jefe)
        if key == arcade.key.KEY_4:
            arcade.play_sound(self.golpe_enemigo)
        if key == arcade.key.KEY_5:
            arcade.play_sound(self.pelea)



def main():
    window = BeanAHero(500, 500)
    arcade.run()


main()
