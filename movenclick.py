import subprocess
import sys
import time
import threading
import random  # Importa a biblioteca random para gerar números aleatórios

# Função para verificar e instalar a biblioteca pyautogui
def instalar_pyautogui():
    try:
        import pyautogui
        print("pyautogui já está instalado.")
    except ImportError:
        print("pyautogui não está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
        print("pyautogui instalado com sucesso!")

# Verifica e instala o pyautogui, se necessário
instalar_pyautogui()

# Importa o pyautogui após garantir que está instalado
import pyautogui

# Função para apertar uma tecla por um determinado tempo
def apertar_tecla(tecla, tempo_pressionado, repeticoes):
    for _ in range(repeticoes):
        pyautogui.keyDown(tecla)  # Pressiona a tecla
        time.sleep(tempo_pressionado)  # Mantém pressionada pelo tempo especificado
        pyautogui.keyUp(tecla)  # Libera a tecla
        time.sleep(0.2)  # Pequeno intervalo entre as pressões

    print(f"Tecla {tecla} pressionada por {tempo_pressionado} segundos, {repeticoes} vezes.")

# Função para clicar o mouse com intervalo randômico entre 0,4 e 0,6 segundos
def clicar_mouse():
    print("Iniciando cliques por 3 minutos...")
    tempo_final = time.time() + 180  # 3 minutos = 180 segundos
    while time.time() < tempo_final:
        pyautogui.click()  # Clica uma vez com o botão esquerdo do mouse
        intervalo = random.uniform(0.4, 0.6)  # Gera um intervalo aleatório entre 0,4 e 0,6 segundos
        time.sleep(intervalo)  # Aguarda o intervalo gerado
    print("Clicou por 3 minutos.")

# Função principal que executa a rotina
def executar_rotina():
    while True:
        # Aperta a tecla 'a' por 1 segundo
        apertar_tecla('a', 1, 1)
        print("Tecla 'a' pressionada por 1 segundo.")

        # Aperta a tecla 'd' por 0.5 segundos, 2 vezes
        apertar_tecla('d', 0.5, 2)

        # Clica o mouse com intervalo randômico durante 3 minutos
        clicar_mouse()

        print("Rotina concluída. Reiniciando...")

# Aguarda 5 segundos antes de começar para dar tempo de mudar para a janela desejada
print("O script começará em 5 segundos. Mude para a janela desejada.")
time.sleep(5)

# Inicia a execução da rotina
try:
    executar_rotina()
except KeyboardInterrupt:
    print("Script interrompido pelo usuário.")