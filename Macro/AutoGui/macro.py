import pyautogui as pa
import time

def play_macro():
    time.sleep(2.53)
    pa.click(-1204, 449)  # Mouse click at (-1204, 449)
    time.sleep(2.38)
    pa.click(-1428, 580)  # Mouse click at (-1428, 580)
    time.sleep(1.30)
    pa.hotkey('tab')  # Hotkey: tab
    time.sleep(1.54)
    pa.hotkey('enter')  # Hotkey: enter

if __name__ == '__main__':
    play_macro()
