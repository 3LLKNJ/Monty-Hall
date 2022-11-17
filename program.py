from random import randint

# Jogador A troca de porta
# Jogador B não troca de porta
# Jogador C troca de porta 50% das vezes (controle)

# Número de iterações
iterations = 1000000

# Contagem de sucessos
playerASuccesses = 0 
playerBSuccesses = 0 
playerCSuccesses = 0 

for i in range(iterations):

    # Setup inicial do problema
    doors = {'1':False,'2':False,'3':False}
    doors[str(randint(1,3))] = True

    # Escolha inicial da porta (aleatória)
    chosenDoor = str(randint(1,3))


    # Se a porta escolhida inicialmente for correta
    if doors[chosenDoor]:

        # Elimina uma das portas não escolhidas, que são ambas garantidas serem as portas erradas
        # Essa etapa é irrelevante pois a porta removida não afeta o resultado
        # Porém a etapa é executada para manter fidelidade com o problema original
        numbers = [1,2,3]
        numbers.remove(int(chosenDoor))
        del doors[str(numbers[randint(0,1)])]

    # Se a porta escolhida inicialmente for errada
    else:
        
        # Elimina uma das portas não escolhidas
        # Especificamente a outra porta errada (que não foi escolhida)
        # Essa etapa é irrelevante pois a porta removida não afeta o resultado
        # Porém a etapa é executada para manter fidelidade com o problema original
        numbers = [1,2,3]
        numbers.remove(int(chosenDoor))
        numbers.remove(int(list(doors.keys())[list(doors.values()).index(True)]))
        del doors[str(numbers[0])]

    # Caso a porta atual seja a correta
    if doors[chosenDoor]:
        playerBSuccesses += 1
        
    # Caso a outra porta seja a correta
    else:
        playerASuccesses += 1

    # Jogador C escolhe uma das duas portas restantes
    # Equivale a escolher entre trocar ou não
    playerCChoice = list(doors.values())[randint(0,1)]

    if playerCChoice:
        playerCSuccesses +=1

print('Jogador A ganhou ' + str(playerASuccesses) + ' vezes de ' + str(iterations) + ' totalizando ' + str(round(100*playerASuccesses/iterations, 4)) + r'% de acertos utilizando a estratégia de trocar de porta')
print('Jogador B ganhou ' + str(playerBSuccesses) + ' vezes de ' + str(iterations) + ' totalizando ' + str(round(100*playerBSuccesses/iterations, 4)) + r'% de acertos utilizando a estratégia de não trocar de porta')
print('Jogador C ganhou ' + str(playerCSuccesses) + ' vezes de ' + str(iterations) + ' totalizando ' + str(round(100*playerCSuccesses/iterations, 4)) + r'% de acertos trocando de porta ou não aleatóriamente e servindo como controle')