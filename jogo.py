import random

# Boa vindas ao jogo de adivinhação
print("********************************")
print("Bem vindo ao jogo de Adivinhação")
print("********************************")

# geração de numero aleatório entre 1 e 51
numerosecreto = random.randrange(1, 51)
totaldetentativas = 0
pontos = 1000

# informando o nível de dificuldade do jogo
print("Qual nível de dificuldade voce vai escolher?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Escolha o nível: "))

if(nivel == 1):
    totaldetentativas = 20
    pontos = 200
elif(nivel == 2):
    totaldetentativas = 10
    pontos = 100
else:
    totaldetentativas = 5
    pontos = 50

# loop para o jogador chutar o número secreto
while(totaldetentativas > 0):
    print("Você tem ", totaldetentativas, " tentativas")   
    
    chute = input("Digite o seu número: ")
    print("Você digitou: ", chute )

    chuteNumerico = int(chute)    

    if(totaldetentativas == 0):
        print("Você não tem mais tentativas. Fim do jogo.")
        break


# verificando se o chute 
acertou = chuteNumerico == numerosecreto
maior = chuteNumerico > numerosecreto
menor = chuteNumerico < numerosecreto


# se voce digitar qualquer numero vou verificar se acertou ou errou
if(acertou):
    print("Parabéns! Você acertou! E Fez um Total de ", pontos, " pontos na partidad. ")
    print("Fim do jogo")
   
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

# Operação matemática para calcular a pontuação do jogador
totaldetentativas = totaldetentativas - 1
pontosperdidos = abs(numerosecreto - chuteNumerico)
pontos = pontos - pontosperdidos

print("Fim do jogo")
