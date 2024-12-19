import re
import time
import pyautogui as pa

def extrair_codigos(arquivo):
    """
    Lê um arquivo e extrai códigos alfanuméricos em uma lista.

    :param arquivo: Caminho para o arquivo.
    :return: Lista de códigos encontrados.
    """
    codigos = []
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                # Expressão regular para capturar palavras alfanuméricas
                codigos.extend(re.findall(r'\b\w+\b', linha))
        return codigos
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []

# Caminho para o arquivo
arquivo = r"C:\Users\SINNCAPPLE\Documents\VSCodeProjects\PythonProjects\CursoPython\Trabalho\DocumentosTrabalho\InsumosObrigatorios.txt"

# Extrair os códigos
lista_de_codigos = extrair_codigos(arquivo)

# Exibir os códigos
def play_codigo_obrigatorio(lista_de_codigos):
    for codigo in range(len(lista_de_codigos)):
        time.sleep(1)
        pa.click(-1840, 79)  # Mouse click at (-1840, 79)
        time.sleep(1)
        pa.click(-1330, 109)  # Mouse click at (-1330, 109)
        time.sleep(1.5)
        pa.write(str(lista_de_codigos[codigo]))
        time.sleep(0.99)
        pa.hotkey('tab')  # Hotkey: tab
        time.sleep(0.82)
        pa.hotkey('enter')  # Hotkey: enter
        time.sleep(1)
        pa.hotkey('enter')  # Hotkey: enter
        time.sleep(2)
        pa.click(-1138, 340)  # Mouse click at (-1138, 340)
        time.sleep(1)
        pa.click(-1166, 386)  # Mouse click at (-1166, 386)
        time.sleep(1)
        pa.click(-1572, 103)  # Mouse click at (-1572, 103)
        time.sleep(1)
        pa.click(-1667, 137)  # Mouse click at (-1667, 137)
        time.sleep(1)
        pa.click(-1682, 163)  # Mouse click at (-1682, 163)
        time.sleep(1.02)
        pa.click(-1647, 194)  # Mouse click at (-1647, 194)
        time.sleep(1)
        pa.hotkey('ctrl', 'a')
        pa.write('1')  # Type: 1
        time.sleep(1.08)
        pa.hotkey('tab')  # Hotkey: tab
        time.sleep(1.37)
        pa.click(-1768, 867)  # Mouse click at (-1768, 867)
        time.sleep(1.01)
        pa.click(-1839, 89)  # Mouse click at (-1839, 89)

play_codigo_obrigatorio(lista_de_codigos)