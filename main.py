#import other modules
import config
import game_screen

def main():
    config.init()
    print(config.intro)

    game = game_screen.Game()
    game.menu()

    print(config.end_game.format(config.num_correct * 5, config.num_games))

main()
