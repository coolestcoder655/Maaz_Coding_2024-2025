import keyboard
from time import sleep as wait

def main() -> None:
    wait(3)
    print("Pressing keystrokes")
    keyboard.press_and_release("shift+a")
    keyboard.press_and_release("shift+enter")

if __name__ == "__main__":
    main()