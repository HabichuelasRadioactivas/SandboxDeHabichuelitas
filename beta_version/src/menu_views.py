import arcade.gui

from game_parameters import *
from game_view import Game
from friendly_npcs import MrBean
from load_assets import *

class Menu(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Empezar", width=200, font_name="Times New Roman")
        self.v_box.add(start_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Salir", width=200, font_name="Times New Roman")
        self.v_box.add(quit_button.with_space_around(bottom=20))

        start_button.on_click = self.on_click_start
        quit_button.on_click = self.on_click_quit

        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))

    def on_click_start(self, event):
        story = Story()
        # self.window.show_view(story)
        self.window.open_story()
        self.manager.disable()

    def on_click_quit(self, event):
        arcade.exit()

    def on_draw(self):
        self.clear()

        self.manager.draw()
        arcade.draw_text("Bean a Hero",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - 100,
                         arcade.color.BLACK,
                         font_size=70,
                         font_name="Times New Roman",
                         anchor_x="center", bold=True)
    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            self.window.open_story()
            self.manager.disable()



class Story(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Nos encontramos en la época medieval, una época con muchos habitantes y poco suministro de",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 160, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("alimento para la gran cantidad de población que vivían en los pueblos de estos reinos antiguos.",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 140, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("La gente desesperada, comenzaba a consumir cualquier tipo de alimento que encontraban.",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 120, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")

        arcade.draw_text("La gente, desgraciadamente, moría de hambre y no había nada que ellos pudieran hacer ",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("al respecto y todo por culpa de un rey tirano que acumulaba toda la comida",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("para el solo, comida que además terminaba pudriéndose.",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")

        arcade.draw_text("La única esperanza de acabar con esta catástrofe era un caballero debilucho",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 40, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("que nunca destaco entre los demás, pero",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("¿cómo podrá este escuálido caballero salvar al mundo...?",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120, arcade.color.WHITE, 18, anchor_x="center",
                         font_name="Times New Roman", italic=True, bold=True)

        arcade.draw_text("Presiona Enter para Continuar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.WHITE, 12, anchor_x="center", font_name="Times New Roman")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            control = Controls()
            # self.window.show_view(control)
            self.window.open_controls()


class Controls(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Controles", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200,
                         arcade.color.WHITE, 70, anchor_x="center", font_name="Times New Roman" )
        arcade.draw_text("W", SCREEN_WIDTH / 2 - 61, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("A S D", SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2 + 80,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Para Moverse", SCREEN_WIDTH / 2 + 55, SCREEN_HEIGHT / 2 + 90,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("K", SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Para Atacar", SCREEN_WIDTH / 2 + 48, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("P", SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2 - 80,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Para Recoger", SCREEN_WIDTH / 2 + 53, SCREEN_HEIGHT / 2 - 80,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("ESC", SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2 - 160,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Para Pausar", SCREEN_WIDTH / 2 + 53, SCREEN_HEIGHT / 2 - 160,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Presiona Enter para Continuar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.WHITE, 12, anchor_x="center", font_name="Times New Roman")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            # self.window.show_view(game)
            self.window.open_game()


class Pause(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.

        # player_sprite = self.game_view.player_sprite
        # player_sprite.draw()

        # draw an orange filter over him
        """
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.ORANGE + (200,))
        arcade.draw_text("PAUSA", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center", font_name="Times New Roman")
        """

        # Show tip to return or reset
        arcade.draw_text("Presiona ESC para Volver",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Presiona Enter para Salir",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center", font_name="Times New Roman")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:  # resume game
            # self.window.show_view(self.game_view)
            self.window.open_game()
        elif key == arcade.key.ENTER:  # reset game
            menu = Menu()
            # self.window.show_view(menu)
            self.window.reload_game()
            self.window.open_menu()


class TheEnd(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Días después de haber derrotado al ejercito del rey tirano,",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 120, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("la paz comenzaba a reinar en todos los rincones de aquel antiguo reino y la comida ya no escaseaba,",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("pues entre los tesoros del rey había un montón de semillas y de todo tipo de alimentos.",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 80, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")

        arcade.draw_text("Sin embargo, ciertas palabras seguían resonando en la cabeza del héroe que había traído la paz",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("“Perdóneme Gran Señor, le he fallado…”",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("¿Realmente la paz duraría para siempre…?",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 140, arcade.color.WHITE, 20, anchor_x="center",
                         font_name="Times New Roman", italic=True, bold=True)

        arcade.draw_text("Presiona Enter para Continuar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.WHITE, 12, anchor_x="center", font_name="Times New Roman")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            credits = Credits()
            # self.window.show_view(credits)
            self.window.open_credits()


class Credits(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()

        arcade.draw_text("Creditos", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200,
                         arcade.color.WHITE, 70, anchor_x="center", font_name="Times New Roman")

        arcade.draw_text("Director del Videojuego...........................Gjergj Kukaj",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 120, arcade.color.WHITE, 16, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("Programador Principal.......................Javier Hérnandez",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 80, arcade.color.WHITE, 16, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("Diseñador de Mapas e Historia.......Gabriel Hernández",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40, arcade.color.WHITE, 16, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("Ingeniero de Sonido.................................Helena Pérez",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 , arcade.color.WHITE, 16, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("Programador........................................Chenyu Castillo",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 40, arcade.color.WHITE, 16, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("Programador de Mecánicas....................Carlos Eguren",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 80, arcade.color.WHITE, 16, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text("Programador de Interfaces...........................Pablo Ruiz",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120, arcade.color.WHITE, 16, anchor_x="center",
                         font_name="Times New Roman")

        arcade.draw_text("Presiona Enter para Continuar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.WHITE, 12, anchor_x="center", font_name="Times New Roman")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            menu = Menu()
            # self.window.show_view(menu)
            self.window.open_post_credits()


class GameOver(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Has Muerto", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.RED_DEVIL, 80, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Presiona Enter para Continuar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.WHITE, 20, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Presiona Esc para Salir", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.WHITE, 15, anchor_x="center", font_name="Times New Roman")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            menu = Menu()
            # self.window.show_view(menu)
            self.window.open_menu()
        elif key == arcade.key.ENTER:
            game = Game()
            # self.window.show_view(game)
            self.window.reload_game()
            self.window.open_game()


class MrBeanCutScene(arcade.View):
    def on_show_view(self):
        self.mr_bean = MrBean()
        self.mr_bean.scale = 1.1
        self.mr_bean.center_x = SCREEN_WIDTH - 120
        self.mr_bean.center_y = SCREEN_HEIGHT/2

        self.dialogue_counter = 0

        self.text_1 = arcade.Sprite(MR_BEAN_DIALOGUE[0], 0.8)
        self.text_1.center_x = 892/2 * 0.6
        self.text_1.center_y = SCREEN_HEIGHT - 568/2 * 0.6 - 20

        self.text_2 = arcade.Sprite(MR_BEAN_DIALOGUE[1], 0.8)
        self.text_2.center_x = 896/2 * 0.6
        self.text_2.center_y = SCREEN_HEIGHT - 578/2 * 0.6 - 20

        self.text_3 = arcade.Sprite(MR_BEAN_DIALOGUE[2], 0.8)
        self.text_3.center_x = 882/2 * 0.6
        self.text_3.center_y = SCREEN_HEIGHT - 116/2 * 0.6 - 20

        self.bean = arcade.Sprite(MR_BEAN_DIALOGUE[3], 0.5)
        self.bean.center_x = SCREEN_WIDTH/2 - 50
        self.bean.center_y = SCREEN_HEIGHT/2

    def on_draw(self):
        self.clear()
        if self.dialogue_counter == 0:
            self.text_1.draw()
            arcade.draw_text("Presiona ENTER para continuar", SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 200,
                             arcade.color.BLACK, 15, anchor_x="left", font_name="Times New Roman")
        elif self.dialogue_counter == 1:
            self.text_2.draw()
            arcade.draw_text("Presiona ENTER para continuar", SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 200,
                             arcade.color.BLACK, 15, anchor_x="left", font_name="Times New Roman")
        elif self.dialogue_counter == 2:
            self.mr_bean.celebrate()
            self.text_3.draw()
            self.bean.draw()
            arcade.draw_text("Presiona ENTER para coger la habichuela", SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 200,
                             arcade.color.BLACK, 15, anchor_x="left", font_name="Times New Roman")
        else:
            self.window.open_game()
        arcade.set_background_color(arcade.color.WHITE)
        self.mr_bean.draw()

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            self.dialogue_counter += 1


class PostCredits(arcade.View):
    def on_show_view(self):

        self.mr_bean = MrBean()
        self.mr_bean.scale = 1.1
        self.mr_bean.center_x = SCREEN_WIDTH - 120
        self.mr_bean.center_y = SCREEN_HEIGHT/2

        self.dialogue_counter = 0

        self.text_4 = arcade.Sprite(POST_CREDITS[0], 1)
        self.text_4.center_x = 892 / 2 * 0.6 + 20
        self.text_4.center_y = SCREEN_HEIGHT - 568 / 2 * 0.6 - 20

        self.text_5 = arcade.Sprite(POST_CREDITS[1], 1)  # 896x578
        self.text_5.center_x = 896 / 2 * 0.6 + 20
        self.text_5.center_y = SCREEN_HEIGHT - 578 / 2 * 0.6 - 20

        self.text_6 = arcade.Sprite(POST_CREDITS[2], 1)  # 882x116
        self.text_6.center_x = 882 / 2 * 0.6 + 20
        self.text_6.center_y = SCREEN_HEIGHT / 2 * 0.6 + 220

    def on_draw(self):
        self.clear()
        if self.dialogue_counter == 0:
            self.text_4.draw()
            arcade.draw_text("Presiona ENTER para continuar", SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 200,
                             arcade.color.BLACK, 15, anchor_x="left", font_name="Times New Roman")

        elif self.dialogue_counter == 1:
            self.text_5.draw()
            arcade.draw_text("Presiona ENTER para continuar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200,
                             arcade.color.BLACK, 15, anchor_x="left", font_name="Times New Roman")
        elif self.dialogue_counter == 2:
            self.text_6.draw()
            self.mr_bean.celebrate()
            arcade.draw_text("Presiona ENTER para continuar", SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 200,
                             arcade.color.BLACK, 15, anchor_x="left", font_name="Times New Roman")
        else:
            self.window.open_game()
        arcade.set_background_color(arcade.color.WHITE)
        self.mr_bean.draw()

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            self.dialogue_counter += 1
        if key == arcade.key.ENTER and self.dialogue_counter == 3:
            self.window.reload_game()
            self.window.open_menu()
