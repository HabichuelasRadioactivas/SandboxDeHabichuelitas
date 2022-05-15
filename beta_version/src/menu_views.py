import arcade.gui

from game_parameters import *
from game_view import Game


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
        self.window.show_view(story)
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


class Story(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Nos encontramos en la época medieval, una época con muchos habitantes y poco suministro de",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 160, arcade.color.WHITE, 15, anchor_x="center",
                         font_name="Times New Roman")
        arcade.draw_text(
            "alimento para la gran cantidad de población que vivían en los pueblos de estos reinos antiguos.",
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
        arcade.draw_text("¿cómo podrá este escuálido caballero salvar al mundo?...",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120, arcade.color.WHITE, 18, anchor_x="center",
                         font_name="Times New Roman", italic=True, bold=True)


        arcade.draw_text("Presiona Enter para Continuar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.WHITE, 12, anchor_x="center", font_name="Times New Roman")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            control = Controls()
            self.window.show_view(control)


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
        arcade.draw_text("X", SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Para Atacar", SCREEN_WIDTH / 2 + 48, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("C", SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Para Recoger", SCREEN_WIDTH / 2 + 53, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.WHITE, 17, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Presiona Enter para Continuar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.WHITE, 12, anchor_x="center", font_name="Times New Roman")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            game = Game()
            game.setup()
            self.window.show_view(game)


class Pause(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        self.clear()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.ORANGE + (200,))

        arcade.draw_text("PAUSA", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center", font_name="Times New Roman")

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
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            menu = Menu()
            self.window.show_view(menu)


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
            self.window.show_view(menu)
        elif key == arcade.key.ENTER:
            game = Game()
            self.window.show_view(game)

