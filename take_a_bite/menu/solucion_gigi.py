import arcade.gui

WIDTH = 800
HEIGHT = 600

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class ClickView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # Define button. Button-handler is declared at the end of Class
        space_view_button = arcade.gui.UIFlatButton(text="SpaceView", width=200)
        self.v_box.add(space_view_button)
        space_view_button.on_click = self.on_space_view

        # Define button. Button-handler is declared at the end of Class
        esc_view_button = arcade.gui.UIFlatButton(text="EscView", width=200)
        self.v_box.add(esc_view_button)
        esc_view_button.on_click = self.on_esc_view

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self):
        self.clear()
        self.manager.draw()

    # define button_methods
    def on_space_view(self, event):
        self.window.show_view(SpaceView())

    def on_esc_view(self, event):
        self.window.show_view(EscapeView())


class SpaceView(arcade.View):
    """ Manage the 'game' view for our program. """

    def __init__(self):
        super().__init__()
        # Create variables here

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()
        arcade.draw_text("Game - press SPACE to advance", WIDTH / 2, HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ Handle key presses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if key == arcade.key.SPACE:
            self.window.show_view(ClickView())


class EscapeView(arcade.View):
    """ Class to manage the game over view """
    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """
        self.clear()
        arcade.draw_text("Game Over - press ESCAPE to advance", WIDTH / 2, HEIGHT / 2,
                         arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if key == arcade.key.ESCAPE:
            self.window.show_view(ClickView())

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "UIFlatButton Example", resizable=True)
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

window = MyWindow()
window.show_view(ClickView())
arcade.run()