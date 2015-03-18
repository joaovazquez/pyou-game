import random
opcao=0
sorteio=0
while opcao!=3 and sorteio!=3:                                                       
    opcao_jogador=input('escolha umas das opcoes: pedra, papel, tesoura, lagarto, spock:')
    lista=['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
    sorteio_jogador=random.choice(lista)
    #print("sorteio_jogador: ",sorteio_jogador)
    print('o elemento sorteado foi:', sorteio_jogador)
    if opcao_jogador=='pedra' and sorteio_jogador=='papel':
        print('voce perdeu')
        opcao=0
        sorteio=sorteio+1         
    if opcao_jogador=='papel' and sorteio_jogador=='pedra':
        print('voce ganhou')
        opcao=opcao+1
        sorteio=0
    if opcao_jogador=='tesoura' and sorteio_jogador=='papel':
        print('voce ganhou')
        opcao=opcao+1
        sorteio=0
    if opcao_jogador=='papel' and sorteio_jogador=='tesoura':
        print('voce perdeu')
        opcao=0
        sorteio=sorteio+1
    if opcao_jogador=='pedra' and sorteio_jogador=='tesoura':
        print('voce ganhou')
        opcao=opcao+1
        sorteio=0
    if opcao_jogador=='tesoura' and sorteio_jogador=='pedra':
        print('voce perdeu')
        opcao=0 
        sorteio=sorteio+1
    if opcao_jogador=='lagarto' and sorteio_jogador=='spock':
        print('voce ganhou')
        opcao=opcao+1 
        sorteio=0
    if opcao_jogador=='spock'and sorteio_jogador=='lagarto':
        print('voce perdeu')
        opcao=0 
        sorteio=sorteio+1
    if opcao_jogador=='lagarto'and sorteio_jogador=='papel':
        print('voce ganhou')
        opcao=opcao+1
        sorteio=0
    if opcao_jogador=='papel' and sorteio_jogador=='lagarto':
        print('voce perdeu')
        opcao=0 
        sorteio=sorteio+1
    if opcao_jogador=='spock'and sorteio_jogador=='pedra':
        print('voce ganhou')
        opcao=opcao+1 
        sorteio=0
    if opcao_jogador=='pedra'and sorteio_jogador=='spock':
        print('voce perdeu')
        opcao=0 
        sorteio=sorteio+1
    if opcao_jogador=='spock'and sorteio_jogador=='tesoura':
        print('voce ganhou')
        opcao=opcao+1
        sorteio=0
    if opcao_jogador=='tesoura'and sorteio_jogador=='spock':
        print('voce perdeu')
        opcao=0
        sorteio=sorteio+1
    if opcao_jogador==sorteio_jogador:
        print('houve um empate')
        opcao=opcao+0 
        sorteio=sorteio+0
    if opcao_jogador=='pedra'and sorteio_jogador=='lagarto':
        print('voce ganhou')
        opcao=opcao+1
        sorteio=0
    if opcao_jogador=='lagarto'and sorteio_jogador=='pedra':
        print('voce perdeu')
        opcao=0
        sorteio=sorteio+1
    print('voce:',opcao)
    print('computador:',sorteio)
print("fim")        
    