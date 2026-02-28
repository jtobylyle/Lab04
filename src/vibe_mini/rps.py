class Error(Exception):
    """Custom error for Rock-Paper-Scissors."""
    pass

def outcome(player, cpu):
    moves = {"rock", "paper", "scissors"}
    if player not in moves or cpu not in moves:
        raise Error("Invalid move")

    if player == cpu:
        return "tie"

    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if wins[player] == cpu:
        return "win"
    else:
        return "lose"
