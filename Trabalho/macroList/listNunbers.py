# Inicializa a lista para armazenar os números
numbers = []

print("Digite os números para adicionar à lista. Digite 'N' para finalizar.")

while True:
    # Solicita entrada do usuário
    user_input = input("Número: ")
    
    # Verifica se o usuário deseja sair
    if user_input.upper() == 'N':
        break
    
    # Tenta converter a entrada em número
    try:
        number = int(user_input)  # Pode usar int(user_input) se quiser apenas inteiros
        numbers.append(number)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'N' para sair.")

# Exibe a lista pronta para uso
print("\nLista gerada:")
print(numbers)
