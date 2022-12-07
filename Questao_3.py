from datetime import time

#diferença de horarios 

inicioH = int(input("digite a hora do inicio do jogo: "))
inicioM = int(input("digite o minuto  do jogo: "))
fimH = int(input("digite o começo do jogo: "))
fimM = int(input("digite o começo do jogo: "))

tempo_gasto = time(fimH-inicioH ,fimM-inicioM)

print(f"O jogo durou {tempo_gasto.hour} horas e {tempo_gasto.minute} minutos")