def rps(p1, p2):
    outcomes = ["Player 1 won!", "Player 2 won!", "Draw!"]

    rps_map = {"scissors": "paper", "paper": "rock", "rock": "scissors"}

    if rps_map[p1] == p2:
        return outcomes[0]

    if rps_map[p2] == p1:
        return outcomes[1]

    return outcomes[2]


if __name__ == "__main__":
    print(rps("rock", "scissors"))  # Player 1 won!
    print(rps("paper", "rock"))  # Player 1 won!
    print(rps("scissors", "paper"))  # Player 1 won!
    print(rps("rock", "paper"))  # Player 2 won!
    print(rps("paper", "scissors"))  # Player 2 won!
    print(rps("scissors", "rock"))  # Player 2 won!
    print(rps("rock", "rock"))  # Draw!
    print(rps("paper", "paper"))  # Draw!
    print(rps("scissors", "scissors"))  # Draw!
