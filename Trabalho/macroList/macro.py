import pyautogui as pa
import time

def play_macro():
    time.sleep(2.23)
    pa.click(-1840, 79)  # Mouse click at (-1840, 79)
    time.sleep(1.93)
    pa.click(-1330, 109)  # Mouse click at (-1330, 109)
    time.sleep(3.35)
    pa.write('1')  # Type: 1
    time.sleep(0.38)
    pa.write('6')  # Type: 6
    time.sleep(0.22)
    pa.write('3')  # Type: 3
    time.sleep(0.99)
    pa.hotkey('tab')  # Hotkey: tab
    time.sleep(0.82)
    pa.hotkey('enter')  # Hotkey: enter
    time.sleep(1.64)
    pa.hotkey('enter')  # Hotkey: enter
    time.sleep(3.65)
    pa.click(-1138, 340)  # Mouse click at (-1138, 340)
    time.sleep(2.56)
    pa.click(-1166, 386)  # Mouse click at (-1166, 386)
    time.sleep(2.03)
    pa.click(-1572, 103)  # Mouse click at (-1572, 103)
    time.sleep(2.11)
    pa.click(-1667, 137)  # Mouse click at (-1667, 137)
    time.sleep(1.34)
    pa.click(-1682, 163)  # Mouse click at (-1682, 163)
    time.sleep(1.02)
    pa.click(-1647, 194)  # Mouse click at (-1647, 194)
    time.sleep(1.47)
    pa.write('1')  # Type: 1
    time.sleep(1.25)
    pa.hotkey('enter')  # Hotkey: enter
    time.sleep(1.08)
    pa.hotkey('tab')  # Hotkey: tab
    time.sleep(3.37)
    pa.click(-1768, 867)  # Mouse click at (-1768, 867)
    time.sleep(3.01)
    pa.click(-1839, 89)  # Mouse click at (-1839, 89)

if __name__ == '__main__':
    play_macro()
