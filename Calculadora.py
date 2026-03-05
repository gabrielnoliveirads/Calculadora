print("""
========================
      CALCULADORA
========================""")
while True:
    print("\nEscolha o que deseja fazer agora:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair\n")
    entrada = input("Digite o número correspondente à ação que deseja fazer:")
    # Verificando se o usuario digitou apenas número:
    if entrada.isdigit():
        operacao = int(entrada)
    else:
        print("DIGITE APENAS NÚMERO!")
        continue
    # Analisando se escolheu "sair":
    if operacao == 5:
        print("Você escolheu sair, saindo...") 
        break 
    
    # Checando se escolheu um número entre 1 a 5:
    if operacao < 1 or operacao > 5: 
        print("Apenas número de 1 a 5!")
        continue 
    
    # Pegando os números com o usuário e analisando se ele digitou apenas número:
    while True:
        entrada1 = input("Escolha o primeiro número:")

        try:
            numero1 = float(entrada1)
            break
        except ValueError:
            print("Digite apenas números!")
    
    while True:
        entrada2 = input("Escolha o segundo número:")

        try:
            numero2 = float(entrada2)
            break
        except ValueError:
            print("Digite apenas números!")

        
    # Operações:
    if operacao == 1:
        soma = numero1+numero2
        print(f'✔ Resultado: {numero1} + {numero2} = {soma}')
        print("-" * 30)
        
    elif operacao == 2:
        sub = numero1-numero2
        print(f'✔ Resultado: {numero1} - {numero2} = {sub}')
        print("-" * 30)
        
    elif operacao == 3:
        mult = numero1*numero2
        print(f'✔ Resultado: {numero1} x {numero2} = {mult}')
        print("-" * 30)
        
    elif operacao == 4:
        if numero2 == 0:
            print("Não é possível dividir por zero!")
            print("-" * 30)
        else:
            div = numero1 / numero2
            print(f'✔ Resultado: {numero1} / {numero2} = {div}')
            print("-" * 30)