import pyautogui as pa
import time
import threading

def play_ticket_sinnc(client, tempo, assunto, descricao):
    time.sleep(2.16)
    pa.click(81, 137)  # Mouse click at (81, 137)
    time.sleep(2.16)
    pa.click(100, 200)
    time.sleep(6.58)
    pa.click(147, 298)  # Mouse click at (147, 298)
    time.sleep(2.44)
    pa.write(client)  # Type: s
    time.sleep(2.55)
    pa.click(154, 344)  # Mouse click at (154, 344)
    time.sleep(2.67)
    pa.click(122, 420)  # Mouse click at (122, 420)
    time.sleep(2.48)
    pa.write(client)  # Type: s
    time.sleep(2.57)
    pa.click(124, 486)  # Mouse click at (124, 486)
    time.sleep(2.00)
    pa.click(126, 505)  # Mouse click at (126, 505)
    time.sleep(2.99)
    pa.click(114, 557)  # Mouse click at (114, 557)
    time.sleep(2.35)
    pa.click(127, 693)  # Mouse click at (127, 693)
    time.sleep(2.39)
    pa.click(302, 601)  # Mouse click at (302, 601)
    time.sleep(2.14)
    pa.click(184, 499)  # Mouse click at (184, 499)
    time.sleep(2.96)
    pa.click(168, 594)  # Mouse click at (168, 594)
    time.sleep(5.28)
    pa.click(143, 434)  # Mouse click at (143, 434)
    time.sleep(5.27)
    pa.click(190, 684)  # Mouse click at (190, 684)
    time.sleep(2.20)
    pa.write('g')  # Type: g
    time.sleep(2.20)
    pa.write('e')  # Type: e
    time.sleep(2.09)
    pa.write('r')  # Type: r
    time.sleep(2.63)
    pa.click(189, 645)  # Mouse click at (189, 645)
    time.sleep(6.04)
    pa.click(914, 251)  # Mouse click at (914, 251)
    time.sleep(6.81)
    pa.write(assunto)  # Type: s
    time.sleep(2.02)
    pa.click(435, 357)  # Mouse click at (435, 357)
    time.sleep(2.75)
    pa.write(descricao) # Type: s
    time.sleep(2.60)
    pa.click(1151, 201)  # Mouse click at (1151, 201)
    time.sleep(2.82)
    pa.click(1159, 390)  # Mouse click at (1159, 390)
    time.sleep(2.35)
    pa.click(1161, 396)  # Mouse click at (1161, 396)
    time.sleep(2.09)
    pa.click(1161, 396)  # Mouse click at (1161, 396)
    time.sleep(2.28)
    pa.click(1035, 407)  # Mouse click at (1035, 407)
    time.sleep(2.13)
    pa.click(1193, 608)  # Mouse click at (1193, 608)
    time.sleep(2.94)
    pa.write(tempo)  # Type: 0
    time.sleep(5.79)
    pa.click(1177, 721)  # Mouse click at (1177, 721)
    time.sleep(2.65)
    pa.click(903, 440)  # Mouse click at (903, 440)
    
def play_ticket_client(client, tempo, assunto, descricao):
    time.sleep(2.16)
    pa.click(81, 137)  # Mouse click at (81, 137)
    time.sleep(2.16)
    pa.click(100, 200)
    time.sleep(6.58)
    pa.click(147, 298)  # Mouse click at (147, 298)
    time.sleep(2.44)
    pa.write(client)  # Type: s
    time.sleep(2.55)
    pa.click(154, 344)  # Mouse click at (154, 344)
    time.sleep(2.67)
    pa.click(122, 420)  # Mouse click at (122, 420)
    time.sleep(2.48)
    pa.write(client)  # Type: s
    time.sleep(2.57)
    pa.click(124, 486)  # Mouse click at (124, 486)
    time.sleep(2.00)
    pa.click(126, 505)  # Mouse click at (126, 505)
    time.sleep(2.99)
    pa.click(114, 557)  # Mouse click at (114, 557)
    time.sleep(2.35)
    pa.click(127, 693)  # Mouse click at (127, 693)
    time.sleep(2.39)
    pa.click(302, 601)  # Mouse click at (302, 601)
    time.sleep(2.14)
    pa.click(184, 499)  # Mouse click at (184, 499)
    time.sleep(2.96)
    pa.click(168, 594)  # Mouse click at (168, 594)
    time.sleep(5.28)
    pa.click(143, 434)  # Mouse click at (143, 434)
    time.sleep(5.27)
    pa.click(190, 684)  # Mouse click at (190, 684)
    time.sleep(2.20)
    pa.write('g')  # Type: g
    time.sleep(2.20)
    pa.write('e')  # Type: e
    time.sleep(2.09)
    pa.write('r')  # Type: r
    time.sleep(2.63)
    pa.click(189, 645)  # Mouse click at (189, 645)
    time.sleep(6.04)
    pa.click(914, 251)  # Mouse click at (914, 251)
    time.sleep(6.81)
    pa.write(assunto)  # Type: s
    time.sleep(2.02)
    pa.click(435, 357)  # Mouse click at (435, 357)
    time.sleep(2.75)
    pa.write(descricao) # Type: s
    time.sleep(2.60)
    pa.click(1151, 201)  # Mouse click at (1151, 201)
    time.sleep(2.82)
    pa.click(1159, 390)  # Mouse click at (1159, 390)
    time.sleep(2.35)
    pa.click(1161, 396)  # Mouse click at (1161, 396)
    time.sleep(2.09)
    pa.click(1161, 396)  # Mouse click at (1161, 396)
    time.sleep(2.28)
    pa.click(1035, 407)  # Mouse click at (1035, 407)
    time.sleep(2.13)
    pa.click(1193, 608)  # Mouse click at (1193, 608)
    time.sleep(2.94)
    pa.write(tempo)  # Type: 0
    time.sleep(5.79)
    pa.click(1177, 721)  # Mouse click at (1177, 721)
    time.sleep(2.65)
    pa.click(908, 498)  # Mouse click at (903, 440)

# Função para capturar input com limite de tempo
def timed_input(prompt, timeout):
    result = [None]

    def get_input():
        result[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        pa.click(-450, -106)
        pa.hotkey('esc')
        return None  # Tempo esgotado, retorna None
    return result[0]

def ticket(entries, indices):

    max_len = len(entries)
    
    if indices != []:
        print("\nSelected entries:")
        for i, idx in enumerate(indices):
            print(f"{i}: {entries[idx]['client']} - {entries[idx]['assunto']}")
    else:
        pa.click(-492, 828)
        print(f"\nAvailable entries (0 to {max_len - 1}):")
        for i, entry in enumerate(entries):
            print(f"{i}: {entry['client']} - {entry['assunto']}")
        while True:
            user_input = input(f"Enter the indices of entries to use (max {max_len}, separated by spaces): ")
            
            try:
                # Converter entrada para uma lista de índices
                indices = list(map(int, user_input.split()))
                
                # Validações
                if len(indices) > max_len:
                    raise ValueError("Input exceeds the maximum allowed length.")
                if not all(0 <= idx < max_len for idx in indices):
                    raise ValueError("One or more indices are out of range.")
                break  # Input válido, sair do loop
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    # Iterar sobre os índices selecionados
    print("\nProcessing selected entries:")
    for number, entry in enumerate(entries):
        if number in indices:
            pa.click(-492, 828)
            # Solicitar tempo personalizado ou usar padrão com timeout de 15 segundos
            user_tempo = timed_input(
                f"For entry '{entry['client']}', specify a time (4 digits, e.g., 0030) or press Enter to use the default ({entry['tempo']}): ",
                timeout=10
            )

            # Validar e definir o tempo
            if user_tempo and user_tempo.isdigit() and len(user_tempo) == 4:
                tempo = user_tempo
            elif user_tempo == "" or user_tempo is None:
                print("Timeout or no input. Using default time.")
                tempo = entry["tempo"]
            else:
                print("Invalid time format. Using default time.")
                tempo = entry["tempo"]

            # Chamar a função apropriada
            if number < 3:
                play_ticket_sinnc(entry["client"], tempo, entry["assunto"], entry["descricao"])
            else:
                play_ticket_client(entry["client"], tempo, entry["assunto"], entry["descricao"])