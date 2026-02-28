import sys
from vibe_mini.rps import outcome, Error

def main():
    if len(sys.argv) != 3:
        print("Usage: python -m vibe_mini.cli <player_move> <cpu_move>")
        sys.exit(1)

    player = sys.argv[1]
    cpu = sys.argv[2]

    try:
        result = outcome(player, cpu)
        print(result)
    except Error as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
