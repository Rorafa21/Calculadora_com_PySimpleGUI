import PySimpleGUI as sg
print("Calculadora Com PySimpleGUI")

n1 =  float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
op = input("Qual operador: ")
soma = n1 + n2
subtrai = n1 - n2
multiplica = n1 * n2
divisao = n1 / n2

while True:
    
    if op == "+":
        print(f"{n1} + {n2} é igual a {soma}")

    elif op == "-":
        print(f"{n1} - {n2} é igual a {subtrai}")

    elif op == "*":
        print(f"{n1} x {n2} é igual a {multiplica}")

    elif op == "/":
        print(f"{n1} / {n2} é igual a {divisao}")

    else:
        print("Insira um operador correto (+, -, *, /)")
    break

print("Fim")