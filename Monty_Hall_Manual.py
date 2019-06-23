import numpy as np
import random

acertos = 0
erros = 0
novo = 'S'
tot = 0

while novo not in 'N':


    grupozero = ['porta 1', 'porta 2', 'porta 3']
    grupo = grupozero
    certa = np.random.choice(grupo)
    print('\033[31m{} \033[34m{} \033[33m{}\033[00m'.format(grupo[0], grupo[1], grupo[2]))


    jogador = str(input('\033[96mEscolha a porta vencedora:\033[00m ')).lower()

    if certa == jogador:
        grupo.remove(jogador)
        grupo.remove(random.choice(grupo))
        grupo.append(jogador)

        print('''\033[96mRetiramos uma porta errada.
Portas restantes: \033[31m{} \033[33m{}\033[00m'''.format(grupo[0], grupo[1]))

    if certa != jogador:
        grupo.remove(certa)
        grupo.remove(jogador)

        el = grupo.pop()
        grupo.append(jogador)
        grupo.append(certa)


        print('''\033[36mRetiramos uma porta errada.
    Portas restantes: \033[31m{} \033[32m{}\033[00m'''.format(grupo[0], grupo[1]))

    resposta = str(input('\033[96mVocê deseja mudar sua resposta? [Sim/Não]\033[00m ')).strip().upper()[0]



    if resposta == 'N':
        if certa == jogador:
            print("Você acertou! Porta prêmiada: {}.".format(certa))
            acertos += 1
        elif certa != jogador:
            print("Você errou! Porta prêmiada: {}.".format(certa))
            erros += 1
    elif resposta == 'S':
        if certa == jogador:
            print("\033[96mVocê errou! Porta prêmiada: {}.".format(certa))
            erros += 1
        elif certa != jogador:
            print("\033[96mVocê acertou! Porta prêmiada: {}.".format(certa))
            acertos += 1
    else:
        print('ERRO!')
    tot +=1
    novo = str(input('Você deseja jogar novamente? ')).strip().upper()

ac = round((acertos/ tot) * 100)
ec = round((erros/ tot) * 100)
print('\033[31mRodadas: {}'.format(tot))
print('\033[32mTotal de acertos: {}'.format(acertos))
print('\033[32m{} %'.format(ac))
print('\033[32mTotal de erros: {}'.format(erros))
print('\033[32m{}%.'.format(ec))