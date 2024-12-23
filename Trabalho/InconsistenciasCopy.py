import pyperclip
import pyautogui as pa
import time
import keyboard  # Para associar a tecla
import tkinter as tk  # Para criar o aplicativo de segundo plano
import threading  # Para rodar a função em segundo plano

# Função para realizar o "Ctrl+C" e copiar o texto da área de captura
def play_copy_incosistencia():
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

# Função para remover a primeira linha (título), linha da data, linha com número isolado, linha "Área / Equipe" e linha "Inconsist. CNES:"
def remove_first_and_date_line():
    # Obtém o texto copiado
    raw_text = pyperclip.paste()

    # Divide o texto em linhas
    lines = raw_text.splitlines()

    # Remove a primeira linha (título), a linha da data (quinta linha), qualquer linha com número isolado,
    # linha "Área / Equipe", e a linha subsequente com a informação "1 - PSF / VILA MARIANA"
    if len(lines) > 1:
        lines = [line for index, line in enumerate(lines) if index != 0 and index != 4 and
                 "Área / Equipe" not in line and not line.strip().isdigit() and 
                 "Inconsist. CNES:" not in line and (index == 0 or "Área / Equipe" not in lines[index - 1])]

    # Recria o texto sem as linhas removidas
    new_text = "\n".join(lines)

    # Copia o novo texto para a área de transferência
    pyperclip.copy(new_text)

    return new_text  # Retorna o novo texto sem as linhas removidas

# Função para formatar o texto
def format_text(raw_text):
    # Divide o texto em linhas
    lines = raw_text.splitlines()

    # Processa as linhas separando corretamente os dados
    try:
        unidade_saude = lines[0].strip() if len(lines) > 0 else ""
        profissional = lines[1].strip() if len(lines) > 1 else ""
        especialidade = lines[2].strip() if len(lines) > 2 else ""
        inconsistencias_cnes = "\n".join(lines[3:]).strip() if len(lines) > 3 else ""

        # Se "C.N.E.S." for encontrado em inconsistencias_cnes, adiciona a mensagem de erro
        if "C.N.E.S." in inconsistencias_cnes:
            inconsistencias_cnes += "\n➥ Não encontrado no XML, nem no CNES;"

        # Formatação da saída de acordo com o novo formato solicitado, com apenas um enter no começo e no final
        formatted_output = f"\nUnidade de Saúde: {unidade_saude}\nProfissional: {profissional}\nEspecialidade: {especialidade}\nInconsistências CNES: {inconsistencias_cnes}\n"

    except Exception as e:
        formatted_output = f"Erro ao formatar o texto: {e}"

    return formatted_output

# Função para formatar o texto e copiar para a área de transferência
def copy_formatted_text():
    raw_text = pyperclip.paste()  # Obtém o texto copiado
    formatted_text = format_text(raw_text)  # Formata o texto

    # Coloca o texto formatado na área de transferência
    pyperclip.copy(formatted_text)

    print("Texto formatado copiado para a área de transferência.")

# Função principal para controlar a execução com a tecla F9
def main():
    print("Pressione 'F9' para formatar o texto copiado e transferi-lo para a área de transferência.")
    while True:
        if keyboard.is_pressed('F9'):  # Quando a tecla F9 for pressionada
            play_copy_incosistencia()  # Executa a cópia com Ctrl+C
            time.sleep(0.5)  # Espera o texto ser copiado
            remove_first_and_date_line()  # Remove as linhas desnecessárias
            copy_formatted_text()  # Formata e copia para a área de transferência
            time.sleep(1)  # Evita múltiplas execuções rápidas

# Função para rodar o código em segundo plano
def run_in_background():
    background_thread = threading.Thread(target=main)
    background_thread.daemon = True  # Permite que o thread termine quando o programa principal terminar
    background_thread.start()

# Cria a interface invisível com Tkinter
def create_tray_app():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal (não será exibida)
    
    # Inicia a execução do programa em segundo plano
    run_in_background()

    # Mantém o aplicativo em execução (aguarda a execução do código em segundo plano)
    root.mainloop()

if __name__ == "__main__":
    create_tray_app()  # Chama a função que cria o app e inicia a execução