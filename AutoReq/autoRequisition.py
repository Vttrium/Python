import time
import pandas as pd  # type: ignore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Caminho do arquivo Excel e do driver do Chrome
excel_path = r'C:\Users\SINNCAPPLE\Downloads\Requisição de Insumos 22-11-2024.xlsx'
chrome_driver_path = r'C:\Users\SINNCAPPLE\Documents\VSCodeProjects\PythonProjects\chromedriver-win64\chromedriver.exe'

# Lendo o arquivo Excel e mostrando as abas disponíveis
excel_data = pd.ExcelFile(excel_path)
sheet_names = excel_data.sheet_names  # Lista de todas as abas disponíveis

print("Abas disponíveis no Excel:")
for i, sheet_name in enumerate(sheet_names, start=1):
    print(f"{i}. {sheet_name}")

# Solicitar ao usuário a aba que deseja processar
while True:
    try:
        escolha = int(input("\nDigite o número da aba que deseja processar (ou 0 para sair): "))
        if escolha == 0:
            print("Finalizando o script.")
            break
        elif 1 <= escolha <= len(sheet_names):
            aba_escolhida = sheet_names[escolha - 1]
            print(f"Você escolheu a aba: {aba_escolhida}")
        else:
            print("Número inválido. Escolha novamente.")
            continue
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    # Lendo os dados da aba escolhida
    df = excel_data.parse(aba_escolhida)
    df_cleaned = df.iloc[2:, [0, 1]]  # Ajuste para manter apenas as colunas relevantes
    df_cleaned.columns = ['Código', 'Quantidade']
    df_cleaned = df_cleaned[df_cleaned['Quantidade'].apply(lambda x: str(x).isdigit())]

    # Inicializando o navegador
    print("\nAbrindo o navegador e acessando o site...")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://sa.sinnc.app/demo/IDSSaude.dll")

    # Login no site
    print("Realizando login no site...")
    time.sleep(2)  # Aguardar o carregamento inicial da página

    # Inserir username
    username_input = driver.switch_to.active_element  # O campo já está focado inicialmente
    username_input.clear()
    username_input.send_keys("sinnc")

    # Inserir senha
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.clear()
    password_input.send_keys("!gdoc@0601")

    # Clicar no botão "Acessar"
    botao_acessar = driver.find_element(By.XPATH, "//span[contains(text(),'Acessar')]")
    botao_acessar.click()
    
    time.sleep(1)
    driver.switch_to.active_element.send_keys(Keys.RETURN)
    time.sleep(4)

    try:
        botao_fechar_popup = driver.find_element(By.XPATH, "//span[@class='x-btn-icon-el x-btn-icon-el-default-toolbar-small icon-x']")
        botao_fechar_popup.click()
    except:
        print("Nenhum pop-up detectado.")

    # Navegar para "Requisições de Insumos"
    print("Navegando para Requisições de Insumos...")
    time.sleep(2)
    linha_requisicoes = driver.find_element(By.XPATH, "//div[contains(text(),'Requisições de Insumos')]")
    linha_requisicoes.click()
    time.sleep(3)

    # Clicar no botão "Incluir"
    botao_incluir = driver.find_element(By.XPATH, "//span[contains(text(),'Incluir')]")
    botao_incluir.click()
    time.sleep(2)

    # Na janela de itens, clicar no botão "Incluir"
    botao_incluir_itens = driver.find_element(By.XPATH, "//span[contains(text(),'Incluir')]")
    botao_incluir_itens.click()
    time.sleep(2)

    # Automatizando o processo para cada linha da aba atual
    print("Processando itens da planilha...")
    for _, row in df_cleaned.iterrows():
        codigo = row['Código']
        quantidade = row['Quantidade']
        
        # Localizar o campo de código
        input_codigo = driver.find_element(By.ID, 'O7B5_id-inputEl')  # Substitua pelo ID correto
        input_codigo.clear()
        input_codigo.send_keys(codigo)
        
        # Aguardar o carregamento (ajuste o tempo conforme necessário)
        time.sleep(2)
        
        # Mover para o próximo campo usando Tab
        input_codigo.send_keys(Keys.TAB)
        
        # Inserir a quantidade no segundo campo (assumindo que Tab leva ao campo correto)
        input_quantidade = driver.switch_to.active_element  # Elemento atualmente focado
        input_quantidade.clear()
        input_quantidade.send_keys(quantidade)
        
        # Localizar e clicar no botão de inclusão
        botao_incluir_item = driver.find_element(By.ID, 'O725_id')  # Substitua pelo ID correto
        botao_incluir_item.click()
        
        # Aguardar antes de passar para o próximo item
        time.sleep(2)

    # Perguntar se deseja continuar com outra aba
    continuar = input("\nDeseja processar outra aba? (s/n): ").strip().lower()
    if continuar != 's':
        print("Finalizando o script.")
        break

# Fechar o navegador ao final do processo
driver.quit()
