from random import randint 
lista = []

for i in range(0,100):
    lista.append(randint(0,1000))

maior = max(lista)
posicao= lista.index(maior)

print(f"o maior valor é {maior}  e sua posicao na lista e {posicao}")    
