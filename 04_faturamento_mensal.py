# 04_faturamento_mental.py

# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar que calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

estado_sp = 67836.43
estado_rj = 36678.66
estado_mg = 29229.88
estado_es = 27165.48
outros_estados = 19849.53

total = estado_sp + estado_rj + estado_mg + estado_es + outros_estados

print("\nBem-vindo(a)!")
print(f"O faturamento mensal da distribuidora foi igual a:\nNo Estado do Espírito Santo: R${estado_es}\nNo Estado de Minas Gerais: R${estado_mg}\nNo Estado do Rio de Janeiro: R${estado_rj}\nNo Estado de São Paulo: R${estado_sp}\nNos demais estados: R${outros_estados}")
print(f"O total do faturamento é de: R${total}")
def calculo_percentual(x):
    resultado = (x / total) * 100
    return resultado


def escolha_estado():
    repete = True
    while repete == True:
        print("\nPara informar o percentual de representação de determinado Estado da Federação em relação ao faturamento total da distribuidora, escolha o número correspondente.")
        estado = int(input(
            "\n1 - Espírito Santo\n2 - Minas Gerais\n3 - Rio de Janeiro\n4 - São Paulo\n5 - Demais Estado\n\n"))

        match estado:
            case 1:
                print(
                    f"\nO percentual de representação do Estado do Espírito Santo em relação ao faturamento total da distribuidora é de {calculo_percentual(estado_es):.2f}%.")
                print("\n===========Consulta concluída===========")
            case 2:
                print(
                    f"\nO percentual de representação do Estado de Minas Gerais em relação ao faturamento total da distribuidora é de {calculo_percentual(estado_mg):.2f}%.")
                print("\n===========Consulta concluída===========")
            case 3:
                print(
                    f"\nO percentual de representação do Estado do Rio de Janeiro em relação ao faturamento total da distribuidora é de {calculo_percentual(estado_rj):.2f}%.")
                print("\n===========Consulta concluída===========")
            case 4:
                print(
                    f"\nO percentual de representação do Estado de São Paulo em relação ao faturamento total da distribuidora é de {calculo_percentual(estado_sp):.2f}%.")
                print("\n===========Consulta concluída===========")
            case 5:
                print(
                    f"\nO percentual de representação dos demais estados da federação em relação ao faturamento total da distribuidora é de {calculo_percentual(outros_estados):.2f}%")
                print("\n===========Consulta concluída===========")
            case _:
                print("\nPor favor, digite um número válido.")

        repete = input('\nDeseja realizar outra consulta? Digite "Sim" ou "Não"\n').lower()

        while repete != "sim" and repete != "não":
            repete = input('\nATENÇÃO! Você deve digitar "Sim" ou "Não"\n').lower()

        if repete == "não":
            print("Obrigado pela preferência.")
            repete = False
        else:
            repete = True

escolha_estado()