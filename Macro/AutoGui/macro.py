import pyautogui as pa
import time

def play_macro():
    time.sleep(1.19)
    pa.mouseDown(-1149, 839)  # Mouse down at (-1149, 839)
    time.sleep(0.11)
    pa.moveTo(-1153, 838)  # Mouse move during drag
    time.sleep(0.42)
    pa.mouseUp(-1159, 830)  # Mouse up at (-1159, 830)
    time.sleep(1.09)
    pa.press('ctrl')  # Key press: ctrl
    time.sleep(0.21)
    pa.hotkey("ctrl", "c")  # Hotkey: ctrl+c

if __name__ == '__main__':
    play_macro()
