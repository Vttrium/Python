import tkinter as tk
import pyperclip  # type: ignore # Biblioteca para manipular a área de transferência

# Função para pegar o texto, converter para maiúsculas e copiar para a área de transferência
def copiar_texto(event=None):
    texto = entry.get()  # Pega o texto inserido no campo de entrada
    if (texto == "") :
        return;
    
    texto_maiusculo = texto.upper()  # Converte para maiúsculas
    pyperclip.copy(texto_maiusculo)  # Copia para a área de transferência
    label_resultado.config(text=f"Texto copiado: {texto_maiusculo}")  # Exibe o texto copiado na interface
    entry.delete(0, tk.END)  # Limpa o campo de entrada para um novo texto

# Função para dar foco ao campo de entrada quando o aplicativo ganhar foco
def dar_foco(event=None):
    entry.focus()

# Criar a janela principal
root = tk.Tk()
root.title("Texto para Maiúsculas")

# Criar o campo de entrada para o texto
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Criar o botão para executar a função
botao = tk.Button(root, text="Copiar em Maiúsculas", command=copiar_texto)
botao.pack(pady=10)

# Label para mostrar o texto copiado
label_resultado = tk.Label(root, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Associar a tecla Enter ao botão
entry.bind('<Return>', copiar_texto)  # A tecla Enter (Return) chama a função copiar_texto

# Associar o evento de foco (quando a janela voltar ao primeiro plano) ao campo de entrada
root.bind('<FocusIn>', dar_foco)  # A janela ganhando foco chama a função dar_foco

# Executar a interface gráfica
root.mainloop()