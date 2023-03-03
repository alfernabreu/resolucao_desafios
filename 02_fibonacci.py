import math


def check_raiz_perfeita(numero):
    quadrado = int(math.sqrt(numero))
    return quadrado * quadrado == numero


def fibonacci(num_inteiro):
    return check_raiz_perfeita(5 * num_inteiro * num_inteiro + 4) or check_raiz_perfeita(5 * num_inteiro * num_inteiro - 4)


print("\nVamos verificar se o número informado se encontra na sequência de Fibonacci.")
num_inteiro = int(input("Informe um número inteiro: "))

if fibonacci(num_inteiro):
    {
        print(f"O número {num_inteiro} faz parte da Sequência de Fibonacci.")
    }
else:
    print(f"O número {num_inteiro} não faz parte da Sequência Fibonacci.")