"""
This file contains the Views for the start menu, pause menu, game over screen
"""
class Menu(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
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
        arcade.draw_text("Once upon a time...", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200,
                         arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Press Enter to Continue", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200,
                         arcade.color.WHITE, 12, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            control = Controls()
            self.window.show_view(control)


class Controls(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Controls", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200,
                         arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("W", SCREEN_WIDTH / 2 - 61, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.WHITE, 15, anchor_x="center")
        arcade.draw_text("A S D", SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2 + 80,
                         arcade.color.WHITE, 15, anchor_x="center")
        arcade.draw_text("To Move", SCREEN_WIDTH / 2 + 40, SCREEN_HEIGHT / 2 + 90,
                         arcade.color.WHITE, 15, anchor_x="center")
        arcade.draw_text("X", SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 15, anchor_x="center")
        arcade.draw_text("To Attack", SCREEN_WIDTH / 2 + 40, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 15, anchor_x="center")
        #arcade.draw_text("C", SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2 - 100,
         #                arcade.color.WHITE, 15, anchor_x="center")
        #arcade.draw_text("To Pick Up", SCREEN_WIDTH / 2 + 40, SCREEN_HEIGHT / 2 - 100,
        #                 arcade.color.WHITE, 15, anchor_x="center")
        arcade.draw_text("Press Enter to Continue", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200,
                         arcade.color.WHITE, 12, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            game = Game()
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

        arcade.draw_text("PAUSED", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to Return",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to Quit",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

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
        arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.RED_DEVIL, 80, anchor_x="center")
        arcade.draw_text("Press Enter to Continue", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Press Esc to Quit", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.WHITE, 15, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            menu = Menu()
            self.window.show_view(menu)
        elif key == arcade.key.ENTER:
            game = Game()
            self.window.show_view(game)
            
def main():
   window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Bean a Hero")
   menu = Menu()
   window.show_view(menu)
   arcade.run()


if __name__ == "__main__":
    main()
