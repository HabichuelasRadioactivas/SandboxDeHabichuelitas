import arcade
from game_parameters import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from menu_views import Menu

def main():
    """Main method"""
    wn = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    wn.show_view(Menu())
    arcade.run()

if __name__ == '__main__':
    main()
