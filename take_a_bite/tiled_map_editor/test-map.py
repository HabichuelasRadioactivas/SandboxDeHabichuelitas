import arcade

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400,200)


        arcade.set_background_color(arcade.color.BLACK)


        self.ground_list = None

        self.setup()

    def setup(self):
        map_name = "./test_map.tmx" #nombre del archivo del mapa
        map = arcade.load_tilemap(map_name)


    def on_draw(self):
        arcade.start_render()
        self.ground_list.draw()

    def on_update(self, delta_time):
        pass


MyGameWindow(1080,568,'mapa prueba')
arcade.run()
