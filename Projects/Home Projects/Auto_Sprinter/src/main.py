from pynput.keyboard import Controller, Key
import threading
import time

keyboard = Controller()

# Spam left and right keys at warp speed
def spam_arrows():
    while True:
        keyboard.press(Key.left)
        keyboard.release(Key.left)

# Run spammer in a separate thread so it doesn’t block
thread = threading.Thread(target=spam_arrows)
thread.start()

print("🚀 Arrow spammer started")