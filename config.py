#global variable to be used by any module
def init():
    global intro
    intro = """Welcome to Higher or Lower!"""

    global prompt
    prompt = """--Press [s] to start the game
--Press [i] to read the game's instructions
--Press [q] to exit the game
"""

    global end_game
    end_game = """
Thank you for playing!
--Total score: {}
--Games played: {}"""

    global instr
    instr = """
INSTRUCTIONS:
You are given one number
Guess whether the second number will be higher or lower than this number
You will get random numbers ranging from 1 to 20
----Press [1] to guess the number is lower
----Press [2] to guess the number is higher
"""

    global input_error
    input_error = """
==INVALID INPUT==
"""

    global game_prompt
    game_prompt = """
You're number is {}
Is the second number higher [2] or lower [1]?
"""

    global game_correct
    game_correct = """
Congratulations, you guessed correctly!
The second number is {}
"""

    global game_wrong
    game_wrong = """
Sorry, you guessed wrong
The second number is {}
"""

    global num_correct
    num_correct = 0

    global num_games
    num_games = 0

    global player_sels
    player_sels = ["s", "i", "q"]
