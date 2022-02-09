def calculadora():
    print("Bem vindo a calculadora")

    n1 = float(input("Digite o primeiro valor: ")
    op = input("Digite a operação desejada: (+, -, *, /):")
    n2 = float(input("Digite o segundo valor: "))
    

    if op == "+":
        print(n1+n2)
    elif op == "-":
        print(n1-n2)
    elif op == "*":
        print(n1+n2)
    elif op == "/":
        print(n1/n2)
    else:
        print("Porfavor insira um valor valido")

calculadora()
