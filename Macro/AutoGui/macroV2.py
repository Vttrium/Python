import pyautogui as pa
import time

def play_macro():
    time.sleep(1.27)
    pa.mouseDown(-1152, 838)  # Mouse down at (-1152, 838)
    time.sleep(0.08)
    pa.mouseUp(-1152, 838)  # Mouse up at (-1152, 838)
    time.sleep(0.74)
    pa.mouseDown(-1143, 844)  # Mouse down at (-1143, 844)
    time.sleep(0.08)
    pa.moveTo(-1143, 844)  # Mouse move during drag
    time.sleep(0.05)
    pa.moveTo(-1149, 842)  # Mouse move during drag
    time.sleep(0.06)
    pa.moveTo(-1163, 835)  # Mouse move during drag
    time.sleep(0.06)
    pa.moveTo(-1170, 833)  # Mouse move during drag
    time.sleep(0.45)
    pa.mouseUp(-1176, 830)  # Mouse up at (-1176, 830)
    time.sleep(0.64)
    pa.press('ctrl')  # Key press: ctrl
    time.sleep(0.29)
    pa.hotkey("ctrl", "c")  # Hotkey: ctrl+c

if __name__ == '__main__':
    play_macro()
