# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.\n
The purpose of the game is to be a number guessing game. Users have a toggleable hint option and different difficulties to configure their game experience.
- [x] Detail which bugs you found.\n
Bugs found: "New game" button didn't start new games, "High/Low" indicators did not correctly display the correct hints, Comparisons between guess and secret was also incorrectly handled.
- [x] Explain what fixes you applied.\n
Resetted the game status so players wouldn't be stuck on a won/lost game. Removed string comparisons and enforced integer inputs. Updated high/low messages.

## 📸 Demo

- [x] [Insert a screenshot of your fixed, winning game here]
<img width="1909" height="1009" alt="image" src="https://github.com/user-attachments/assets/e60808da-6f31-470a-b9ca-fd3e41db9939" />


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
