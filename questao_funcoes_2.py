def valorPagamento(valor,atraso):
    if(atraso == 0):
        return valor
    else:
        valor *= 1.03
        valor = valor* (1+0.1)**atraso 
        return valor


valor= 1
atraso =0
varTotal =0
while (valor!= 0):
    valor = int(input("digite o valor a ser pago: "))
    if(valor == 0):
        break
    atraso = int(input("digite o numero de dias de atraso: "))
    varTotal +=valorPagamento(valor,atraso)
    print("o novo valor a ser pago é: ",valorPagamento(valor,atraso))


print("o valo total a ser pago e:",varTotal)    

