import arcade.gui

WIDTH = 600
HEIGHT = 600
SPRITE_SCALING = 0.5


class Menu(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.background = arcade.load_texture("Escenario1.png")

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        start_button.on_click = self.on_click_start
        settings_button.on_click = self.on_click_settings
        quit_button.on_click = self.on_click_quit

        self.manager.add(
            arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))

    def on_click_start(self, event):
        game_view = Game()
        game_view.setup()
        self.window.show_view(game_view)

    def on_click_settings(self, event):
        settings_view = Settings()
        settings_view.setup()
        self.window.show_view(settings_view)

    def on_click_quit(self, event):
        arcade.exit()

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(300, 300, 600,
                                      600, self.background)
        self.manager.draw()
        arcade.draw_text("Bean a Hero",
                         WIDTH / 2,
                         HEIGHT - 100,
                         arcade.color.BLACK,
                         font_size=70,
                         font_name="Times New Roman",
                         anchor_x="center", bold=True)

    def setup(self):
        # Replace 'pass' with the code to set up your game
        pass


class Game(arcade.View):

    def __init__(self):
        super().__init__()
        # Create variables here
        # cambiar sprite por el personaje
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite.velocity = [3, 3]

    def setup(self):
        # Replace 'pass' with the code to set up your game
        pass

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw everything for the game. """
        self.clear()

        self.player_sprite.draw()

    def on_update(self, delta_time):
        # Call update on all sprites
        self.player_sprite.update()

        # Bounce off the edges
        if self.player_sprite.left < 0 or self.player_sprite.right > WIDTH:
            self.player_sprite.change_x *= -1
        if self.player_sprite.bottom < 0 or self.player_sprite.top > HEIGHT:
            self.player_sprite.change_y *= -1

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = Pause(self)
            self.window.show_view(pause)


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

        arcade.draw_text("PAUSED", WIDTH / 2, HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to Return",
                         WIDTH / 2,
                         HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to Quit",
                         WIDTH / 2,
                         HEIGHT / 2 - 30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            menu = Menu()
            self.window.show_view(menu)


class Settings(arcade.View):
    def __init__(self):
        super().__init__()

        self.media_player = None
        self.paused = True
        self.songs = [":resources:music/funkyrobot.mp3"]
        self.cur_song_index = 0

        self.my_music = arcade.load_sound(self.songs[self.cur_song_index])

        # This creates a "manager" for all our UI elements
        self.ui_manager = arcade.gui.UIManager(self.window)

        box = arcade.gui.UIBoxLayout(vertical=False)

        # --- Start button
        normal_texture = arcade.load_texture(":resources:onscreen_controls/flat_dark/"
                                             "sound_off.png")
        hover_texture = arcade.load_texture(":resources:onscreen_controls/shaded_dark/"
                                            "sound_off.png")
        press_texture = arcade.load_texture(":resources:onscreen_controls/shaded_dark/"
                                            "sound_off.png")

        # Create our button
        self.start_button = arcade.gui.UITextureButton(
            texture=normal_texture,
            texture_hovered=hover_texture,
            texture_pressed=press_texture,
        )

        # Map that button's on_click method to this view's on_button_click method.
        self.start_button.on_click = self.start_button_clicked  # type: ignore

        # Add in our element.
        box.add(self.start_button)

        # --- Down button
        press_texture = arcade.load_texture(":resources:onscreen_controls/shaded_dark/down.png")
        normal_texture = arcade.load_texture(":resources:onscreen_controls/flat_dark/down.png")
        hover_texture = arcade.load_texture(":resources:onscreen_controls/shaded_dark/down.png")

        # Create our button
        self.down_button = arcade.gui.UITextureButton(
            texture=normal_texture,
            texture_hovered=hover_texture,
            texture_pressed=press_texture,
        )

        # Map that button's on_click method to this view's on_button_click method.
        self.down_button.on_click = self.volume_down  # type: ignore
        self.down_button.scale(0.5)

        # Add in our element.
        box.add(self.down_button)

        # --- Up button
        press_texture = arcade.load_texture(":resources:onscreen_controls/shaded_dark/up.png")
        normal_texture = arcade.load_texture(":resources:onscreen_controls/flat_dark/up.png")
        hover_texture = arcade.load_texture(":resources:onscreen_controls/shaded_dark/up.png")

        # Create our button
        self.up_button = arcade.gui.UITextureButton(
            texture=normal_texture,
            texture_hovered=hover_texture,
            texture_pressed=press_texture,
        )

        # Map that button's on_click method to this view's on_button_click method.
        self.up_button.on_click = self.volume_up  # type: ignore
        self.up_button.scale(0.5)

        # Add in our element.
        box.add(self.up_button)

        # Place buttons in the center of the screen using an UIAnchorWidget with default values
        self.ui_manager.add(arcade.gui.UIAnchorWidget(child=box))

    def setup(self):
        # Replace 'pass' with the code to set up your game
        pass

    def music_over(self):
        self.media_player.pop_handlers()
        self.media_player = None
        self.sound_button_off()
        self.cur_song_index += 1
        if self.cur_song_index >= len(self.songs):
            self.cur_song_index = 0
        self.my_music = arcade.load_sound(self.songs[self.cur_song_index])
        self.media_player = self.my_music.play()
        self.media_player.push_handlers(on_eos=self.music_over)

    def volume_down(self, *_):
        if self.media_player and self.media_player.volume > 0.2:
            self.media_player.volume -= 0.2

    def volume_up(self, *_):
        if self.media_player and self.media_player.volume < 1.0:
            self.media_player.volume += 0.2

    def sound_button_on(self):
        self.start_button.texture_pressed = \
            arcade.load_texture(":resources:onscreen_controls/shaded_dark/sound_on.png")
        self.start_button.texture = \
            arcade.load_texture(":resources:onscreen_controls/flat_dark/sound_on.png")
        self.start_button.texture_hovered = \
            arcade.load_texture(":resources:onscreen_controls/shaded_dark/sound_on.png")

    def sound_button_off(self):
        self.start_button.texture_pressed = \
            arcade.load_texture(":resources:onscreen_controls/shaded_dark/sound_off.png")
        self.start_button.texture = \
            arcade.load_texture(":resources:onscreen_controls/flat_dark/sound_off.png")
        self.start_button.texture_hovered = \
            arcade.load_texture(":resources:onscreen_controls/shaded_dark/sound_off.png")

    def start_button_clicked(self, *_):
        self.paused = False
        if not self.media_player:
            # Play button has been hit, and we need to start playing from the beginning.
            self.media_player = self.my_music.play()
            self.media_player.push_handlers(on_eos=self.music_over)
            self.sound_button_on()
        elif not self.media_player.playing:
            # Play button hit, and we need to un-pause our playing.
            self.media_player.play()
            self.sound_button_on()
        elif self.media_player.playing:
            # We are playing music, so pause.
            self.media_player.pause()
            self.sound_button_off()

    def on_draw(self):
        self.clear()

        # This draws our UI elements
        self.ui_manager.draw()
        arcade.draw_text("Settings",
                         start_x=0, start_y=self.window.height - 55,
                         width=self.window.width,
                         font_size=40,
                         align="center",
                         color=arcade.color.BLACK)

        if self.media_player:
            volume = self.media_player.volume
            arcade.draw_text(f"Volume: {volume:3.1f}",
                             start_x=10, start_y=50, color=arcade.color.BLACK, font_size=24)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ALMOND)

        # Registers handlers for GUI button clicks, etc.
        # We don't really use them in this example.
        self.ui_manager.enable()

    def on_hide_view(self):
        # This unregisters the manager's UI handlers,
        # Handlers respond to GUI button clicks, etc.
        self.ui_manager.disable()

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            menu_view = Menu()
            menu_view.setup()
            self.window.show_view(menu_view)


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Bean a Hero")
    menu_view = Menu()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
