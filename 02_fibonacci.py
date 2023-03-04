#02_fibonacci.py

# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa 
# na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

print("\nBem-vindo(a)!\nVamos checar se o número digitado pelo usuário pertence ao conjunto de valores que compõe à Sequência de Fibonacci.")

escolha = True
while escolha:

    valor = int(input("\nDigite o número desejado: "))

    primeiros_termos = [0, 1]  

    while primeiros_termos[-1] <= valor:
        primeiros_termos.append(primeiros_termos[-1] + primeiros_termos[-2])

    if valor in primeiros_termos:
        print(f"\nO número {valor} pertence ao conjunto de valores que compõe a Sequência de Fibonacci.")
    else:
        print(f"\nO número {valor} não pertence ao conjunto de valores que compõe a Sequência de Fibonacci.")
    
    escolha = input('Você deseja checar outro número? Digite "Sim" ou "Não": ').lower()
    while escolha != "sim" and escolha != "não":
        escolha = input('Você inseriu um valor inválido.\nPor favor, digite "Sim" ou "Não": ').lower()
    
    if escolha == "não":
            escolha = False
            print("\nObrigado pela escolha.")
