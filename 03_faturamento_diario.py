# 03_faturamento_diario.py

# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open("dados.json") as faturamento:
    new_dados = json.load(faturamento)

#Menor e maior valor de faturamento ocorrido em um dia do mês
armazena_valor = []
for i in new_dados:
     if i["valor"] > 0:
          armazena_valor.append(i["valor"])

menor = min(armazena_valor)
maior = max(armazena_valor)

print("\n===================== Menor faturamento do mês =====================")
print(f"O menor faturamento do mês é igual a R${menor:.2f}")

print("\n===================== Maior faturamento do mês =====================")
print(f"O maior faturamento do mês é igual a R${maior:.2f}")

# Cálculo da média
media = 0
count = 0
for i in new_dados:
    if i["valor"] > 0:
            count += 1

soma = 0
for i in new_dados:
     if i["valor"] > 0:
          soma += i["valor"]

media = soma / count
print("\n===================== Média Mensal =====================")
print(f"A média mensal de faturamento é igual a R${media:.2f}")

#Cálculo do número de dias em que o faturamento foi maior que a média
print("\n===================== Dias em que o faturamento foi maior que a média mensal =====================")
count = 0
for i in new_dados:
     if i["valor"] > media:
          count += 1

print(f"O número de dias em que o faturamento foi superior a média mensal é {count} dias.\n")
