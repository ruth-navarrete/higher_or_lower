# Higher or Lower
 A guessing game where you have to guess whether or not the hidden number is higher or lower than the revealed number.

Premise of the game is that the player will be given a number and based on that number, the user will guess whether the still hidden number is higher or lower than the first number.

* The player will only be able to guess once for each set of numbers.
* The player will enter certain keys for various purposes
    [1] to guess the hidden number is higher
    [2] to guess the hidden number is lower
  - or -
    [q] or [Q] to quit the game
  - or -
    [s] or [S] to play the game
  - or -
    [i] or [I] to get game instructions
  Any other character will incur an error message followed by a new game.
  Input will be converted to lowercase.
* If the player guesses correcctly, add 5 to the score, local_score, which is initialized at the start of the game to 0. We will attempt later to create stored memory where the local_score will be updated to the stored_score.
