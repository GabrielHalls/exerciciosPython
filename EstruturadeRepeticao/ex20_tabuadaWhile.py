# tabuada

valor = int(input("Digite um valor que deseja saber a tabuada:\n"))
print("Você escolheu a tabuada do valor", valor, "\n")
contadora = 1
while contadora <=10:
    print(valor, "x", contadora, "=", valor*contadora)
    contadora+=1