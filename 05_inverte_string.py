# 05_inverte_string.py

# Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverte(expressao):
    expressao = expressao[::-1]
    return expressao

print("Bem-vindo(a)!\nO propósito deste aplicativo é apresentar a versão invertida de uma palavra ou frase informada pelo usuário.")

repete = True
while repete:
    expressao = input("\nInforme uma palavra ou frase para vê-la invertida:\n")
    print(f"\nA expressão {expressao} em sua forma invertida é {inverte(expressao)}")

    repete = input('\nDeseja ver outra palavra ou frase invertida? Digite "Sim" ou "Não"\n').lower()
    while repete != "sim" and repete != "não":
        repete = input('Valor informado inválido.\nVocê deve informar "Sim" ou "Não"\n').lower()
    
    if repete == "não":
        repete = False