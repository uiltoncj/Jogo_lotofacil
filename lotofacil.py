from random import randint

quantidade_de_jogos = int(input('Quantos jogos deseja fazer? '))
minha_lista = list()
contador = 1
jogos_ganhos = 0

while contador <= quantidade_de_jogos:
    contador02 = 0
    lista = list()
    while contador02 <= 15:
        numero_gerado = randint(1,25)
        if numero_gerado not in lista:
            lista.append(numero_gerado)
            contador02 = contador02 +1

    lista.sort()
    minha_lista.append(lista[:])
    lista.clear()
    contador += 1

def acertos(jogo, resultado):
    acerto = 0
    for numero in jogo:
        if numero in resultado:
            acerto = acerto + 1
    return acerto

contador_03 = 0

for i,l in enumerate(minha_lista):
    print('_'*65)
    print('Jogo {}: {}'.format(i,l))

    resultado = [1, 2, 3, 5, 7, 9, 10, 11, 14, 15, 16, 19, 20, 21, 23, 24]

    if resultado == l:
        jogos_ganhos += 1
        print('Acertou')
    else:
        contador_03 += 1
        print('perdeu')
    print('acertos', acertos(l,resultado))
print('_'*65)

print('Quantidade de jogos ganho {}'.format(jogos_ganhos))
print('Quantidade de jogos perdidos {}'.format(contador_03))

print('+'*120)
def conta_acertos(quantidade_de_acertos):
    contador = 0
    for n, jogo in enumerate(minha_lista):
        total_de_acertos = acertos(jogo, resultado)
        if quantidade_de_acertos <= total_de_acertos <=quantidade_de_acertos:
            print('Jogo {} com a aposta: {} teve total de {} acertos'.format(n,jogo, total_de_acertos))
            if total_de_acertos == quantidade_de_acertos:
                contador += 1
    print('Total de jogos com {} acertos: {}'.format(quantidade_de_acertos, contador))
    print('#'*120)
conta_acertos(8)
conta_acertos(9)
conta_acertos(10)
conta_acertos(11)
conta_acertos(12)
conta_acertos(13)
conta_acertos(14)
conta_acertos(15)
