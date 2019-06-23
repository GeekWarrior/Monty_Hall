import numpy as np
import random

acertos = 0
erros = 0
novo = 'S'
tot = 0

while tot < 1000:

    grupozero = ['porta 1', 'porta 2', 'porta 3']
    grupo = grupozero
    certa = np.random.choice(grupo)
    print(grupo)
    print(certa)

    jogador = np.random.choice(grupo)

    if certa == jogador:
        grupo.remove(jogador)
        grupo.remove(random.choice(grupo))
        grupo.append(jogador)

        print('''Retiramos uma porta errada.
    Portas restantes: {}'''.format( grupo))

    if certa != jogador:
        grupo.remove(certa)
        grupo.remove(jogador)

        el = grupo.pop()
        grupo.append(jogador)
        grupo.append(certa)


        print('''Retiramos uma porta errada.
    Portas restantes: {}'''.format(grupo))

        print('Deseja mudar sua resposta? ')

    resposta = "S"
    print(resposta)

    if resposta == 'N':
        if certa == jogador:
            print("Você acertou! Porta prêmiada: {}.".format(certa))
            acertos += 1
        elif certa != jogador:
            print("Você errou! Porta prêmiada: {}.".format(certa))
            erros += 1
    elif resposta == 'S':
        if certa == jogador:
            print("Você errou! Porta prêmiada: {}.".format(certa))
            erros += 1
        elif certa != jogador:
            print("Você acertou! Porta prêmiada: {}.".format(certa))
            acertos += 1
    else:
        print('ERRO!')
    tot +=1
    

ac = round((acertos/ tot) * 100)
ec = round((erros/ tot) * 100)
print('Rodadas: {}'.format(tot))
print('Total de acertos: {}'.format(acertos))
print('{} %'.format(ac))
print('Total de erros: {}'.format(erros))
print('{}%.'.format(ec))