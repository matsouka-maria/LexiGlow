"""
LexiGlow - A CS-Themed Word Guessing Game
==========================================
Code in Place 2026 - Final Project
Author: Maria

Guess hidden computer science words letter by letter.
Score points, build streaks, and use hints wisely!
"""

import random


# ── Word Bank ──────────────────────────────────────────────────────────────────

WORD_BANK = [
    {"word": "PYTHON",    "category": "Programming",      "hint": "The language you learned in Code in Place"},
    {"word": "BINARY",    "category": "CS Basics",        "hint": "The number system computers use (0s and 1s)"},
    {"word": "LOOP",      "category": "Programming",      "hint": "Repeat code with this structure"},
    {"word": "STACK",     "category": "Data Structures",  "hint": "Last in, first out — like a pile of plates"},
    {"word": "QUEUE",     "category": "Data Structures",  "hint": "First in, first out — like a line at a cafe"},
    {"word": "ARRAY",     "category": "Data Structures",  "hint": "An ordered collection of elements"},
    {"word": "MERGE",     "category": "Algorithms",       "hint": "Combine two sorted lists into one"},
    {"word": "HASH",      "category": "CS Basics",        "hint": "A function that maps data to a fixed size value"},
    {"word": "CLASS",     "category": "OOP",              "hint": "A blueprint for creating objects"},
    {"word": "INDEX",     "category": "Programming",      "hint": "Position of an element in a list (starts at 0!)"},
    {"word": "DEBUG",     "category": "Programming",      "hint": "Find and fix errors in your code"},
    {"word": "CACHE",     "category": "Systems",          "hint": "Fast temporary memory for frequently used data"},
    {"word": "GRAPH",     "category": "Data Structures",  "hint": "Nodes connected by edges"},
    {"word": "PIXEL",     "category": "Graphics",         "hint": "The smallest unit of a digital image"},
    {"word": "SCOPE",     "category": "Programming",      "hint": "Where a variable can be accessed"},
    {"word": "TUPLE",     "category": "Python",           "hint": "An immutable ordered sequence in Python"},
    {"word": "LOGIC",     "category": "CS Basics",        "hint": "AND, OR, NOT — the building blocks"},
    {"word": "TOKEN",     "category": "CS Basics",        "hint": "A unit in a programming language grammar"},
    {"word": "SYNTAX",    "category": "Programming",      "hint": "The rules that define a programming language"},
    {"word": "RUNTIME",   "category": "CS Basics",        "hint": "When your program is actually executing"},
    {"word": "POINTER",   "category": "Memory",           "hint": "A variable that stores a memory address"},
    {"word": "BOOLEAN",   "category": "CS Basics",        "hint": "True or False — nothing in between"},
    {"word": "COMPILE",   "category": "Programming",      "hint": "Translate source code into machine code"},
    {"word": "ITERATE",   "category": "Programming",      "hint": "Go through a sequence one item at a time"},
    {"word": "FUNCTION",  "category": "Programming",      "hint": "A reusable block of code with a name"},
    {"word": "VARIABLE",  "category": "Programming",      "hint": "A named container that stores a value"},
    {"word": "RECURSION", "category": "Algorithms",       "hint": "A function that calls itself"},
    {"word": "ALGORITHM", "category": "Algorithms",       "hint": "A step-by-step procedure to solve a problem"},
]

MAX_GUESSES = 8
HINT_COST   = 5


# ── Display helpers ────────────────────────────────────────────────────────────

PINK  = "\033[95m"
TEAL  = "\033[96m"
GREEN = "\033[92m"
AMBER = "\033[93m"
RED   = "\033[91m"
GRAY  = "\033[90m"
BOLD  = "\033[1m"
RESET = "\033[0m"


def clear_screen():
    print("\n" * 2)


def print_banner():
    print(PINK + BOLD)
    print("  ██╗     ███████╗██╗  ██╗██╗ ██████╗ ██╗      ██████╗ ██╗    ██╗")
    print("  ██║     ██╔════╝╚██╗██╔╝██║██╔════╝ ██║     ██╔═══██╗██║    ██║")
    print("  ██║     █████╗   ╚███╔╝ ██║██║  ███╗██║     ██║   ██║██║ █╗ ██║")
    print("  ██║     ██╔══╝   ██╔██╗ ██║██║   ██║██║     ██║   ██║██║███╗██║")
    print("  ███████╗███████╗██╔╝ ██╗██║╚██████╔╝███████╗╚██████╔╝╚███╔███╔╝")
    print("  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚══╝╚══╝ ")
    print(RESET)
    print(GRAY + "  A CS-themed word guessing game  •  Code in Place 2026" + RESET)
    print()


def print_separator():
    print(GRAY + "  " + "─" * 54 + RESET)


def display_word(word, revealed):
    """Show correctly guessed letters, underscores for the rest."""
    display = ""
    for i, letter in enumerate(word):
        if revealed[i]:
            display += GREEN + BOLD + letter + RESET + "  "
        else:
            display += GRAY + "_" + RESET + "  "
    print("  " + display)


def display_stats(score, streak, guesses_left, solved):
    print()
    print(
        f"  {PINK}Score{RESET} {BOLD}{score:>4}{RESET}   "
        f"{TEAL}Streak{RESET} {BOLD}{streak:>2}{RESET}   "
        f"{AMBER}Guesses{RESET} {BOLD}{guesses_left:>2}/{MAX_GUESSES}{RESET}   "
        f"{GREEN}Solved{RESET} {BOLD}{solved:>2}{RESET}"
    )
    print()


def display_wrong_guesses(wrong_letters):
    if wrong_letters:
        letters = "  ".join(sorted(wrong_letters))
        print(f"  {GRAY}Wrong: {RED}{letters}{RESET}")
    else:
        print(f"  {GRAY}Wrong: —{RESET}")
    print()


def display_progress_bar(guesses_left):
    filled = guesses_left
    empty  = MAX_GUESSES - guesses_left
    bar    = GREEN + "█" * filled + RESET + GRAY + "░" * empty + RESET
    print(f"  {bar}  {guesses_left} left")
    print()


# ── Game logic ─────────────────────────────────────────────────────────────────

def pick_word(used_words):
    """Pick a random word that hasn't been used yet this session."""
    available = [w for w in WORD_BANK if w["word"] not in used_words]
    if not available:
        used_words.clear()
        available = WORD_BANK
    return random.choice(available)


def get_letter_input(prompt):
    """Ask the player for a single letter, keep asking until valid."""
    while True:
        raw = input(prompt).strip().upper()
        if len(raw) == 1 and raw.isalpha():
            return raw
        print(f"  {RED}Please enter a single letter (A-Z).{RESET}")


def play_round(word_data, score, streak, solved, used_words):
    """
    Play one round of LexiGlow.
    Returns (new_score, new_streak, new_solved, won).
    """
    word     = word_data["word"]
    category = word_data["category"]
    hint     = word_data["hint"]

    revealed      = [False] * len(word)
    wrong_letters = set()
    guessed       = set()
    guesses_left  = MAX_GUESSES
    hints_used    = 0

    while True:
        clear_screen()
        print_banner()
        display_stats(score, streak, guesses_left, solved)
        print_separator()
        print(f"\n  {PINK}Category:{RESET} {BOLD}{category}{RESET}")
        print(f"  {GRAY}{hint}{RESET}\n")
        display_progress_bar(guesses_left)
        display_word(word, revealed)
        print()
        display_wrong_guesses(wrong_letters)
        print_separator()

        # Check win
        if all(revealed):
            pts = guesses_left * 10 + 20
            score  += pts
            streak += 1
            solved += 1
            print(f"\n  {GREEN}{BOLD}You got it!{RESET}  {PINK}+{pts} points{RESET}\n")
            input(f"  {GRAY}Press Enter for the next word...{RESET}")
            return score, streak, solved, True

        # Check lose
        if guesses_left <= 0:
            streak = 0
            print(f"\n  {RED}Out of guesses!{RESET}  The word was {BOLD}{GREEN}{word}{RESET}\n")
            input(f"  {GRAY}Press Enter to continue...{RESET}")
            return score, streak, solved, False

        # Menu
        print(f"\n  [G] Guess a letter    [H] Buy hint ({HINT_COST} pts)    [S] Skip    [Q] Quit\n")
        choice = input("  Your choice: ").strip().upper()

        if choice == "Q":
            return score, streak, solved, False

        elif choice == "S":
            streak = 0
            print(f"\n  {GRAY}Skipped. The word was {BOLD}{word}{RESET}{GRAY}.{RESET}\n")
            input(f"  {GRAY}Press Enter...{RESET}")
            return score, streak, solved, False

        elif choice == "H":
            if score < HINT_COST:
                print(f"  {RED}Not enough points for a hint! (Need {HINT_COST}){RESET}")
                input(f"  {GRAY}Press Enter...{RESET}")
                continue
            hidden = [i for i, r in enumerate(revealed) if not r]
            if not hidden:
                print(f"  {GRAY}No letters left to reveal!{RESET}")
                input(f"  {GRAY}Press Enter...{RESET}")
                continue
            idx = random.choice(hidden)
            revealed[idx] = True
            guessed.add(word[idx])
            score -= HINT_COST
            hints_used += 1
            print(f"  {TEAL}Hint: position {idx + 1} is \"{word[idx]}\"{RESET}")
            input(f"  {GRAY}Press Enter...{RESET}")

        elif choice == "G":
            letter = get_letter_input("  Enter a letter: ")

            if letter in guessed:
                print(f"  {AMBER}You already guessed \"{letter}\"!{RESET}")
                input(f"  {GRAY}Press Enter...{RESET}")
                continue

            guessed.add(letter)

            if letter in word:
                for i, ch in enumerate(word):
                    if ch == letter:
                        revealed[i] = True
                print(f"  {GREEN}Nice! \"{letter}\" is in the word!{RESET}")
            else:
                wrong_letters.add(letter)
                guesses_left -= 1
                print(f"  {RED}\"{letter}\" is not in the word.{RESET}")

            input(f"  {GRAY}Press Enter...{RESET}")

        else:
            print(f"  {RED}Invalid choice. Press G, H, S, or Q.{RESET}")
            input(f"  {GRAY}Press Enter...{RESET}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    clear_screen()
    print_banner()
    print(f"  Welcome to {PINK}{BOLD}LexiGlow{RESET}! Guess CS words letter by letter.")
    print(f"  {GRAY}Score points, build streaks, and use hints wisely.{RESET}\n")
    input(f"  {GRAY}Press Enter to start...{RESET}")

    score      = 0
    streak     = 0
    solved     = 0
    used_words = set()

    while True:
        word_data = pick_word(used_words)
        used_words.add(word_data["word"])

        score, streak, solved, won = play_round(
            word_data, score, streak, solved, used_words
        )

        clear_screen()
        print_banner()
        print_separator()
        print(f"\n  {PINK}{BOLD}Session Stats{RESET}")
        print(f"\n  Score   {BOLD}{score}{RESET}")
        print(f"  Streak  {BOLD}{streak}{RESET}")
        print(f"  Solved  {BOLD}{solved}{RESET}")
        print()
        print_separator()
        print()

        again = input("  Play another round? (Y / N): ").strip().upper()
        if again != "Y":
            break

    clear_screen()
    print_banner()
    print(f"  {PINK}{BOLD}Thanks for playing LexiGlow!{RESET}\n")
    print(f"  Final Score  {BOLD}{score}{RESET}")
    print(f"  Words Solved {BOLD}{solved}{RESET}")
    print(f"  Best info    check your GitHub! :){RESET}")
    print()


if __name__ == "__main__":
    main()
