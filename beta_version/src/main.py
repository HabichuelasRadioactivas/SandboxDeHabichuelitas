import arcade
from beta_game import BetaGame

def main():
    """Main method"""
    wn = BetaGame()
    wn.setup()
    arcade.run()

if __name__ == '__main__':
    main()
