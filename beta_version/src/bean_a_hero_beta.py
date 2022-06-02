import arcade

from game_parameters import *
from load_assets import *
from game_view import Game
from menu_views import *


class BeanAHeroBeta(arcade.Window):
    """Custom window class"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.game = Game()
        self.game.setup()
        self.status = 1
        self.set_update_rate(1 / 35)  # TODO the engine increases the update rate. Has to be fixed
        self.background_music = arcade.load_sound(BACKGROUND_MUSIC)
        self.open_menu()

    def on_update(self, delta_time):
        pass

    def open_menu(self):
        self.status = 0
        self.show_view(Menu())

    def open_story(self):
        self.show_view(Story())

    def open_controls(self):
        self.show_view(Controls())

    def open_the_end(self):
        self.show_view(TheEnd())

    def open_credits(self):
        self.show_view(Credits())

    def open_game_over(self):
        self.show_view(GameOver())

    def open_pause(self):
        self.show_view(Pause())

    def open_game(self):
        self.show_view(self.game)

    def open_bean_cutscene(self):
        self.show_view(MrBeanCutScene())

    def open_post_credits(self):
        self.show_view(PostCredits())
     
    def open_king_cutscene(self):
        self.show_view(KingCutScene())

    def open_post_fight_cutscene(self):
        self.show_view(PostFightCutScene())

    def reload_game(self):
        self.game = Game()
        self.game.setup()
