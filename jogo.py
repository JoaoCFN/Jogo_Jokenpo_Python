import random

opcoes = ['pedra', 'papel', 'tesoura']

escolha_computador = random.randint(0, 2)
#print(opcoes[escolha_computador])

print("-"*40)
print("SEJA BEM VINDO AO PEDRA, PAPEL E TESOURA")
print("-"*40)
numero_usuario = int(input("ESCOLHA: \n 1 - PARA PEDRA \n 2 - PARA PAPEL \n 3 - PARA TESOURA \n\n"))


if numero_usuario == 1:
    escolha = 'pedra'
elif numero_usuario == 2:
    escolha = 'papel'
elif numero_usuario == 3:
    escolha = 'tesoura'
else:
    print("Escolha inválida")
    escolha = ''


if escolha == opcoes[escolha_computador]:
    print("-" * 40)
    print("O COMPUTADOR ESCOLHEU: ", opcoes[escolha_computador])
    print("VOCÊ ESCOLHEU: ", escolha)
    print("DEU EMPATE|")
    print("-" * 40)
elif opcoes[escolha_computador] == escolha:
    print("-" * 40)
    print("O COMPUTADOR ESCOLHEU: ", opcoes[escolha_computador])
    print("VOCÊ ESCOLHEU: ", escolha)
    print("DEU EMPATE|")
    print("-" * 40)

if escolha == 'pedra' and opcoes[escolha_computador] == 'papel':
    print("-" * 40)
    print("O COMPUTADOR ESCOLHEU: ", opcoes[escolha_computador])
    print("VOCÊ ESCOLHEU: ", escolha)
    print("O COMPUTADOR VENCEU!")
    print("-" * 40)
elif escolha == 'pedra' and opcoes[escolha_computador] == 'tesoura':
    print("-" * 40)
    print("O COMPUTADOR ESCOLHEU: ", opcoes[escolha_computador])
    print("VOCÊ ESCOLHEU: ", escolha)
    print("VOCÊ VENCEU!")
    print("-" * 40)
elif escolha == 'papel' and opcoes[escolha_computador] == 'pedra':
    print("-" * 40)
    print("O COMPUTADOR ESCOLHEU: ", opcoes[escolha_computador])
    print("VOCÊ ESCOLHEU: ", escolha)
    print("VOCÊ VENCEU!")
    print("-" * 40)
elif escolha == 'papel' and opcoes[escolha_computador] == 'tesoura':
    print("-" * 40)
    print("O COMPUTADOR ESCOLHEU: ", opcoes[escolha_computador])
    print("VOCÊ ESCOLHEU: ", escolha)
    print("O COMPUTADOR VENCEU")
    print("-" * 40)
elif escolha == 'tesoura' and opcoes[escolha_computador] == 'papel':
    print("O COMPUTADOR ESCOLHEU: ", opcoes[escolha_computador])
    print("VOCÊ ESCOLHEU: ", escolha)
    print("VOCÊ VENCEU!")
elif escolha == 'tesoura' and opcoes[escolha_computador] == 'pedra':
    print("-" * 40)
    print("O COMPUTADOR ESCOLHEU: ", opcoes[escolha_computador])
    print("VOCÊ ESCOLHEU: ", escolha)
    print("A COMPUTADOR VENCEU")
    print("-" * 40)



