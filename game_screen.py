#import other modules
import random
import config

class Game:
    def __init__(self):
        config.num_correct = 0
        config.num_games = 0

    def game_play(self):
        num_1 = random.randrange(1, 21)
        num_2 = random.randrange(1, 21)

        while num_1 == num_2:
            num_2 = random.randrange(1, 21)
        
        user_guess = input(config.game_prompt.format(num_1))

        while user_guess != '1' and user_guess != '2':
            print(config.input_error)
            user_guess = input(config.game_prompt.format(num_1))

        if num_1 > num_2 and user_guess == '1':
            print(config.game_correct.format(num_2))
            config.num_correct += 1
        elif num_1 < num_2 and user_guess == '2':
            print(config.game_correct.format(num_2))
            config.num_correct += 1
        else:
            print(config.game_wrong.format(num_2))

    def menu(self):
        user_opt = 's'

        while user_opt != 'q':
            user_opt = input(config.prompt)
            user_opt = user_opt.lower()

            if user_opt not in config.player_sels:
                print(config.input_error)
            elif user_opt == 'q':
                return
            elif user_opt == 'i':
                print(config.instr)
            else:
                self.game_play()
                config.num_games += 1
