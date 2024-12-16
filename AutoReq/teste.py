import pyautogui as pa
import time

Unidade = '13'
Dispensario = '161'
arquivo_nome = f'Requisicao de Insumos - Unidade {Unidade} - Local {Dispensario} - Data {time.gmtime().tm_mon}-{time.gmtime().tm_mday}'

def play_macro(Unidade, arquivo_nome):
    time.sleep(2.84)
    pa.click(-1828, -75)  # Mouse click at (-1828, -75)
    time.sleep(5.04)
    pa.click(-1441, 577)  # Mouse click at (-1441, 577)
    time.sleep(1.90)
    pa.hotkey('tab')  # Hotkey: tab
    time.sleep(0.35)
    pa.hotkey('tab')  # Hotkey: tab
    time.sleep(0.91)
    pa.write(Unidade)
    time.sleep(1.59)
    pa.hotkey('tab')  # Hotkey: tab
    time.sleep(2.89)
    pa.click(-1201, 449)  # Mouse click at (-1201, 449)
    time.sleep(4.15)
    pa.click(-1438, 621)  # Mouse click at (-1438, 621)
    time.sleep(2.52)
    pa.hotkey('tab')  # Hotkey: tab
    time.sleep(1.60)
    pa.hotkey('enter')  # Hotkey: enter
    time.sleep(4.68)
    pa.click(-1892, 7)  # Mouse click at (-1892, 7)
    time.sleep(1.70)
    pa.click(-1570, 310)  # Mouse click at (-1570, 310)
    time.sleep(2.72)
    pa.click(-1792, 291)  # Mouse click at (-1792, 291)
    time.sleep(3.84)
    pa.click(-1698, 54)  # Mouse click at (-1698, 54)
    time.sleep(2.74)
    pa.click(-1840, 862)  # Mouse click at (-1840, 862)
    time.sleep(4.45)
    pa.click(-1754, 110)  # Mouse click at (-1754, 110)
    time.sleep(1.76)
    pa.click(-1846, 135)  # Mouse click at (-1846, 135)
    
    time.sleep(1.37)
    pa.write(str(2552))
    time.sleep(1.37)
    pa.hotkey('tab')
    time.sleep(1.37)
    pa.write(str(2))
    pa.hotkey('tab')
    pa.hotkey('tab')
    pa.hotkey('enter')
    
    time.sleep(2.64)
    pa.click(-1765, 855)  # Mouse click at (-1765, 855)
    time.sleep(3.84)
    pa.click(-991, 16)  # Mouse click at (-991, 16)
    time.sleep(2.80)
    pa.click(-1070, 39)  # Mouse click at (-1070, 39)
    time.sleep(3.02)
    pa.write(arquivo_nome)  # Type: f
    time.sleep(1.69)
    pa.hotkey('enter')  # Hotkey: enter
    time.sleep(2.90)
    pa.click(-1006, 872)  # Mouse click at (-1006, 872)
    time.sleep(2.45)
    pa.click(-1004, 855)  # Mouse click at (-1004, 855)

if __name__ == '__main__':
    play_macro(Unidade, arquivo_nome)
