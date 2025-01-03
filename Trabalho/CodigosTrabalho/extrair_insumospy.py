import re

# Carregar o arquivo
with open("c:/Users/SINNCAPPLE/Desktop/e-SUS/Insumos_Conims/saldos inativar.txt", encoding="utf-8") as file:
    content = file.read()

# Usar expressão regular para encontrar números de 4 a 9 dígitos antes do hífen e do espaço
codes = re.findall(r'\b\d{4,9}(?=\s+-)', content)

# Armazenar os códigos em uma lista
codes_list = list(codes)

# Exibir a lista de códigos
print("Códigos encontrados:", codes_list)

# Exibir a quantidade de números encontrados
print("Total de números encontrados:", len(codes_list))


