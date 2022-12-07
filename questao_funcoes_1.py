def salario(bruto):
    inss = bruto *0.89
    salario_liquido = inss *0.85
    return salario_liquido



bruto = input("infrome seu salrio :")
liquido = salario(bruto)
print(f"seu salario liquido foi de  {liquido}")