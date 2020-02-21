import random
linhas = open('palavras.txt').read().splitlines()
linhaEscolhida = random.choice(linhas)

linhas2 = open('respostas.txt').read().splitlines()

palavra = linhaEscolhida
embaralhada = "".join(random.sample(palavra, len(palavra)))
separacao = '-------------------' #Variável só para separar e não ficar bagunçado na visão do jogador
plvEmb = print(embaralhada)
print(separacao)


tentativa = input('Você consegue acertar qual palavra está escrita?: ')

def tentativaAcerto(tentativa):
    if tentativa == linhaEscolhida:
        return print('Parabéns! Você acertou.')
    tentativaRestante = 5

    while tentativa != linhaEscolhida:
        mensagemErrado = random.choice(linhas2)
        print(mensagemErrado)
        tentativaRestante -= 1
        print('Você tem {} tentativas!'.format(tentativaRestante))
        tentativa = input('Consegue advinhar?: ')
        if tentativaRestante == 0:
            print('Que pena, você não conseguiu acertar :c')
            break
        if tentativa == linhaEscolhida:
            return print('Parabéns! Você acertou.')
            
tentativaAcerto(tentativa)