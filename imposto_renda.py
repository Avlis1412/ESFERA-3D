salario = float(input("digite salário: "))

if salario <= 1903.8:
    print("Você está isento do IRPF.")
    
elif 1903.8 <= salario <= 2826.65:
    imposto = salario * 7.5 / 100
    print  ("O desconto do IRPF é: " , imposto)
    
elif 2826.66 <= salario <= 3751.05:
    imposto = salario * 15 / 100
    print  ("O desconto do IRPF é: ", imposto)
    
elif 3751.06 <= salario <= 4664.68:
    imposto = salario * 22.5 / 100
    print  ("O desconto do IRPF é: ", imposto)
    
else:
    imposto = salario * 27.5 / 100
    print ("O desconto do IRPF é:", imposto)

input("Pressione Enter para sair...")
