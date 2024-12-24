import os

def menu():
    print("1. Gravar ações")
    print("2. Reproduzir ações")
    print("3. Ver log de execução")
    print("4. Sair")
    return input("Escolha uma opção: ")

while True:
    choice = menu()
    if choice == "1":
        os.system("Macro\Selenium\gravacaoSelenium.ipynb")
    elif choice == "2":
        os.system("Macro\Selenium\execucaoSelenium.ipynb")
    elif choice == "3":
        with open("execution_log.json", "r") as file:
            print(json.load(file))
    elif choice == "4":
        break
    else:
        print("Opção inválida.")
