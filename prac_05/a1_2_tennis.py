print("Welcome Player 1. How was your match?")
player_score = input("    Your score: ")
opponent_score = input("Opponent score: ")

if player_score > opponent_score:
    print("You win! :)")
elif player_score == opponent_score:
    print("It's a draw.")
    print("Congratulations on playing first match!")
else:
    print("You lost :( Keep trying.")
    print("Congratulations on playing first match!")
# The decision model used here is to compare the results of competitors.
# The condition of winning is to have a higher score than the opponent.