from vibe_mini.rps import outcome

def test_rock_scissors():
    assert outcome("rock", "scissors") == "win"

def test_rock_paper():
    assert outcome("rock", "paper") == "lose"

def test_scissors_paper():
    assert outcome("scissors", "paper") == "win"

def test_paper_rock():
    assert outcome("paper", "rock") == "win"

def test_scissors_scissors():
    assert outcome("scissors", "scissors") == "tie"
