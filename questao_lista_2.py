lista_de_idade = []
idade =0

while(idade>=0):
    idade = int(input("digite sua idade: "))
    if(idade > 0):
      lista_de_idade.append(idade)


media = sum(lista_de_idade) / len(lista_de_idade)

print(f"a media e {media}")
