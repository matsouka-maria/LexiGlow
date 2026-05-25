# LexiGlow 🌸

> A CS-themed terminal word guessing game — built as the Code in Place 2026 Final Project.

Guess hidden computer science vocabulary words letter by letter. Score points, build streaks, and use hints strategically — before you run out of guesses!

---

## Demo

```
  ██╗     ███████╗██╗  ██╗██╗ ██████╗ ██╗      ██████╗ ██╗    ██╗
  ██║     ██╔════╝╚██╗██╔╝██║██╔════╝ ██║     ██╔═══██╗██║    ██║
  ██║     █████╗   ╚███╔╝ ██║██║  ███╗██║     ██║   ██║██║ █╗ ██║
  ...

  Score   40   Streak  2   Guesses  6/8   Solved  2

  Category: Data Structures
  Last in, first out — like a pile of plates

  ████░░░░  6 left

  S  T  A  _  _

  Wrong: B  F  X
```

---

## How to run

**Requirements:** Python 3.6+, no external libraries needed.

```bash
git clone https://github.com/matsouka-maria/lexiglow.git
cd lexiglow
python lexiglow.py
```

---

## How to play

| Key | Action |
|-----|--------|
| `G` | Guess a letter |
| `H` | Buy a hint (costs 5 points) |
| `S` | Skip the current word |
| `Q` | Quit the game |

- You have **8 guesses** per word
- Correct guesses reveal the letter in every position it appears
- Wrong guesses reduce your remaining guesses
- **Scoring:** `guesses_left × 10 + 20` bonus points per word solved
- **Streaks** multiply your motivation 💅

---

## Word categories

The game includes 28 words across 9 CS categories:

| Category | Examples |
|----------|---------|
| Programming | PYTHON, LOOP, DEBUG, SCOPE |
| Data Structures | STACK, QUEUE, ARRAY, GRAPH |
| Algorithms | MERGE, RECURSION, ALGORITHM |
| CS Basics | BINARY, HASH, LOGIC, TOKEN |
| Python | TUPLE |
| OOP | CLASS |
| Memory | POINTER |
| Systems | CACHE |
| Graphics | PIXEL |

---

## Python concepts used

This project was built using concepts from **Stanford's Code in Place**:

- **Variables & data types** — strings, integers, booleans, sets, lists, dicts
- **Functions** — modular design with single-responsibility functions
- **Loops** — `while` loops for game flow and `for` loops for word iteration
- **Conditionals** — branching game logic based on player input
- **Lists** — tracking revealed letters and word state
- **Dictionaries** — storing word bank entries (word, category, hint)
- **Sets** — efficiently tracking guessed and wrong letters
- **String methods** — `.upper()`, `.strip()`, `.isalpha()`, f-strings
- **Randomness** — `random.choice()` for word selection
- **`__name__ == "__main__"`** — proper Python entry point pattern

---

## Project structure

```
lexiglow/
├── lexiglow.py   # main game (single file, fully self-contained)
└── README.md
```

---

## About

Built by **Maria** for the [Code in Place 2026](https://codeinplace.stanford.edu) Final Project — Stanford's free introductory Python course.

Part of my CS learning journey alongside CS50, CS50P, CS50W, CS50 SQL, and my studies at Democritus University of Thrace.
