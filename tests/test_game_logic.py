from logic_utils import check_guess


def simulate_new_game(session: dict, new_secret: int) -> dict:
    """Mirrors the new-game reset block in app.py."""
    session["attempts"] = 0
    session["secret"] = new_secret
    session["status"] = "playing"
    session["history"] = []
    return session


def test_new_game_resets_status_after_win():
    session = {"status": "won", "history": [40, 60, 50], "attempts": 3, "score": 70}
    simulate_new_game(session, new_secret=42)
    assert session["status"] == "playing"


def test_new_game_resets_status_after_loss():
    session = {"status": "lost", "history": [10, 20], "attempts": 8, "score": 0}
    simulate_new_game(session, new_secret=99)
    assert session["status"] == "playing"


def test_new_game_clears_history():
    session = {"status": "won", "history": [1, 2, 3], "attempts": 3, "score": 50}
    simulate_new_game(session, new_secret=7)
    assert session["history"] == []


def test_new_game_resets_attempts():
    session = {"status": "lost", "history": [], "attempts": 8, "score": 0}
    simulate_new_game(session, new_secret=55)
    assert session["attempts"] == 0


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
