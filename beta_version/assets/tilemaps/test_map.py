import arcade

SCREEN_TITLE = "Test map"

# Size of screen to show, in pixels
SCREEN_WIDTH = 830
SCREEN_HEIGHT = 620


class GameWindow(arcade.Window):


    def __init__(self, width, height, title):
        # Init the parent class
        self.tile_map = None
        super().__init__(width, height, title)
        self.scene = None

    def setup(self):

        test = "map_4.tmx"
        self.tile_map = arcade.load_tilemap(test,1.30)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

    def on_draw(self):

        self.clear()
        self.scene.draw()


def main():

    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()