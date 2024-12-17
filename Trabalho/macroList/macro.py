import pyautogui as pa
import time

def play_macro():
    time.sleep(1.66)
    pa.click(-196, 105)  # Mouse click at (-196, 105)
    time.sleep(4.04)
    pa.write('3')  # Type: 3
    time.sleep(2.74)
    pa.hotkey('page down')  # Hotkey: page down
    time.sleep(0.00)
    pa.hotkey('tab')  # Hotkey: tab
    time.sleep(0.53)
    pa.hotkey('enter')  # Hotkey: enter
    time.sleep(1.39)
    pa.hotkey('enter')  # Hotkey: enter
    time.sleep(3.21)
    pa.click(-354, 250)  # Mouse click at (-354, 250)
    time.sleep(1.88)
    pa.click(-367, 293)  # Mouse click at (-367, 293)
    time.sleep(2.36)
    pa.click(-744, 367)  # Mouse click at (-744, 367)
    time.sleep(2.05)
    pa.click(-774, 436)  # Mouse click at (-774, 436)
    time.sleep(4.45)
    pa.click(-857, 865)  # Mouse click at (-857, 865)
    time.sleep(3.10)
    pa.click(-933, 79)  # Mouse click at (-933, 79)
    time.sleep(2.32)
    pa.click(265, 130)  # Mouse click at (265, 130)

if __name__ == '__main__':
    play_macro()
