import pyautogui as pa
import time

def play_macro():
    time.sleep(3.70)
    pa.click(-1614, 857)  # Mouse click at (-1614, 857)
    time.sleep(2.91)
    pa.click(-1469, 485)  # Mouse click at (-1469, 485)
    time.sleep(3.37)
    pa.click(-1001, 857)  # Mouse click at (-1001, 857)

if __name__ == '__main__':
    play_macro()
