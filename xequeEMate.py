import funcs_auxiliares as f


# Variáveis utilizadas em todas as funções de movimento
quadrados = ['p_quadrado', 'b_quadrado']
pecasPretas = ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre', 'p_peao']
pecasBrancas = ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre', 'b_peao']

def verificacaoDiagonal(tabuleiro, contLinha, contColuna, proximaLinha, proximaColuna, limiteLinha, limiteColuna):
    while True:
        if contColuna == limiteColuna or contLinha == limiteLinha:
            break
        if (tabuleiro[contLinha][contColuna] in pecasBrancas and tabuleiro[contLinha][contColuna]!= 'b_rei') or (tabuleiro[contLinha][contColuna] in pecasPretas and tabuleiro[contLinha][contColuna] not in ['p_bispo','p_rainha']):
            return False
        posicao = tabuleiro[contLinha][contColuna]
        if posicao in pecasPretas and posicao in ['p_bispo', 'p_rainha']:
            return True
        contLinha += proximaLinha
        contColuna += proximaColuna
def verificacaoL(tabuleiro, proximaLinha, proximaColuna, limiteLinha, limiteColuna):       
    for linha in range(1, 3):
        for coluna in range(1, 3):
            for sinal in [-1, +1]:
                print(linha * sinal, coluna * sinal)
def possibilidadesL(linha=0, coluna=1):
  valores = []
  limites = range(8)
  for i in range(-1,2,2):
    for j in range(-2,3,4):
      if linha+i in limites and coluna+j in limites:
        valores.append([linha+i, coluna+j])
      if linha+j in limites and coluna+i in limites:
        valores.append([linha+j, coluna+i]) 
  return valores

def xeque(tabuleiro,linha,coluna,cor):
    resultado = False
    contLinha= linha
    contColuna= coluna
    if cor == 'branca':
        print(linha, coluna)
        #CASAS DIAGONAIS (Para verificar se está ameaçado por bispos, rainha ou peões)
        #Casas superiores direita (bispo rainha e peão)  
        #Verificação se há um peão na diagonal imediata antes de verificar as demais casas
        if tabuleiro[linha - 1][coluna + 1] == 'p_peao' or tabuleiro[linha -1][coluna - 1] == 'p_peao':
            return True
        #Função que faz a verificação diagonal
        if verificacaoDiagonal(tabuleiro, contLinha, contColuna, -1, 1, -1, 8) == True:
            return True
        #Casas superiores esquerda (bispo, rainha e peão)
        if verificacaoDiagonal(tabuleiro, contLinha, contColuna, -1, -1, -1,-1) == True:
            return True
        #Casas inferior direita (Bispo e rainha)
        if verificacaoDiagonal(tabuleiro, contLinha, contColuna, +1, +1, 8,8) == True:
            return True
        #Casas inferior esquerda (Bispo e rainha)
        if verificacaoDiagonal(tabuleiro, contLinha, contColuna, +1, -1, 8,-1) == True:
            return True
        #VERIFICAÇÃO DAS CASAS EM "L" (Movimento do cavalo)
        for listas in possibilidadesL(linha,coluna):
            linha  = listas[0]
            coluna = listas[1]
            if tabuleiro[linha][coluna]=='p_cavalo':
                return True

        #VERIFICAÇÃO DAS CASAS HORIZINTAIS (Movimento da torre e da rainha)
        #Para cima
        if linha > 0:
            for i in range(linha, 0, -1):
                if tabuleiro[i][coluna] in pecasBrancas and tabuleiro[i][coluna]!= 'b_rei':
                    break
                elif tabuleiro[i][coluna] in pecasPretas and tabuleiro[i][coluna]!= 'p_torre' and tabuleiro[i][coluna]!= 'p_rainha':
                    break
                elif tabuleiro[i][coluna] == 'p_torre' or tabuleiro[i][coluna] == 'p_rainha':
                    resultado = True
        #Para baixo
        if linha < 7:
            for i in range(linha, 8):
                if tabuleiro[i][coluna] in pecasBrancas and tabuleiro[i][coluna]!=  'b_rei':
                    break
                elif tabuleiro[i][coluna] in pecasPretas and tabuleiro[i][coluna]!= 'p_torre' and tabuleiro[i][coluna]!= 'p_rainha':
                    break
                elif tabuleiro[i][coluna] == 'p_torre' or tabuleiro[i][coluna] == 'p_rainha':
                    resultado = True
        #Para direita
        if coluna < 7:
            for i in range(coluna, 8):
                if tabuleiro[i][linha] in pecasBrancas and tabuleiro[i][linha]!= 'b_rei':
                    break
                elif tabuleiro[i][linha] in pecasPretas and tabuleiro[i][linha] not in ['p_torre','p_rainha']:
                    break
                elif tabuleiro[i][linha] == 'p_torre' or tabuleiro[i][linha] == 'p_rainha':
                    resultado = True
        #Para esquerda
        if coluna > 0:
            for i in range(coluna,0,-1):
                if tabuleiro[i][linha] in pecasBrancas and tabuleiro[i][linha]!= 'b_rei':
                    break
                elif tabuleiro[i][linha] in pecasPretas and tabuleiro[i][linha] not in ['p_torre','p_rainha']:
                    break
                elif tabuleiro[i][linha] == 'p_torre' or tabuleiro[i][linha] == 'p_rainha':
                    resultado = True
    return resultado

