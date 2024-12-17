from cx_Freeze import setup, Executable

# Configuração para o cx_Freeze
setup(
    name="Texto para Maiúsculas",
    version="1.0",
    description="Aplicativo para copiar texto em maiúsculas",
    executables=[Executable("upperText.py", base="Win32GUI")]  # Para GUI (sem terminal)
)

