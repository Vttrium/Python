import pyautogui as pa
import time

def play_macro():
    time.sleep(2.78)
    pa.mouseDown(-1303, 622)  # Mouse down at (-1303, 622)
    time.sleep(0.08)
    pa.mouseUp(-1303, 622)  # Mouse up at (-1303, 622)
    time.sleep(1.36)
    pa.mouseDown(-1300, 168)  # Mouse down at (-1300, 168)
    time.sleep(0.08)
    pa.mouseUp(-1300, 168)  # Mouse up at (-1300, 168)
    time.sleep(0.55)
    pa.mouseDown(-1300, 168)  # Mouse down at (-1300, 168)
    time.sleep(0.08)
    pa.mouseUp(-1300, 168)  # Mouse up at (-1300, 168)
    time.sleep(0.16)
    pa.click(-1300, 168)  # Simple click at (-1300, 168)
    time.sleep(0.17)
    pa.click(-1300, 168)  # Simple click at (-1300, 168)
    time.sleep(0.47)
    pa.press('ctrl')  # Key press: ctrl
    time.sleep(0.30)
    pa.hotkey("ctrl", "c")  # Hotkey: ctrl+c
    time.sleep(1.57)
    pa.mouseDown(-1050, 542)  # Mouse down at (-1050, 542)
    time.sleep(0.07)
    pa.mouseUp(-1050, 542)  # Mouse up at (-1050, 542)
    time.sleep(1.25)
    pa.mouseDown(-1212, 532)  # Mouse down at (-1212, 532)
    time.sleep(0.06)
    pa.moveTo(-1212, 532)  # Mouse move during drag
    time.sleep(0.10)
    pa.moveTo(-1234, 536)  # Mouse move during drag
    time.sleep(0.05)
    pa.moveTo(-1781, 541)  # Mouse move during drag
    time.sleep(0.09)
    pa.moveTo(-1829, 541)  # Mouse move during drag
    time.sleep(0.35)
    pa.mouseUp(-1846, 543)  # Mouse up at (-1846, 543)
    time.sleep(1.01)
    pa.press('ctrl')  # Key press: ctrl
    time.sleep(0.43)
    pa.hotkey("ctrl", "c")  # Hotkey: ctrl+c

if __name__ == '__main__':
    play_macro()
