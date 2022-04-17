import arcade

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

class MapRightDoor(arcade.View):
    """ Class to manage the game over view """
    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        arcade.draw_text('WASD to move, X to attack, C to pick up', 5, SCREEN_HEIGHT - 21, arcade.color.BLACK, 12)
        print("RIGHT DOOR")
        arcade.draw_lrtb_rectangle_filled(SCREEN_WIDTH - 10, SCREEN_WIDTH, 300, 250, arcade.color.BLACK)


class MapLeftDoor(arcade.View):
    """ Class to manage the game over view """
    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_text('WASD to move, X to attack, C to pick up', 5, SCREEN_HEIGHT - 21, arcade.color.BLACK, 12)
        print("LEFT DOOR")
        arcade.draw_lrtb_rectangle_filled(SCREEN_WIDTH - 10, SCREEN_WIDTH, 300, 250, arcade.color.BLACK)
