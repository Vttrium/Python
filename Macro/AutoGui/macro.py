import pyautogui as pa
import time

def play_macro():
    time.sleep(2.41)
    pa.click(-1392, 865)  # Mouse click at (-1392, 865)
    time.sleep(2.83)
    pa.click(-1376, 750)  # Mouse click at (-1376, 750)
    time.sleep(4.85)
    pa.click(-979, 0)  # Mouse click at (-979, 0)

if __name__ == '__main__':
    play_macro()
