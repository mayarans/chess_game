import funcs_auxiliares as f
import movimentos as m
# Variáveis utilizadas em todas as funções de movimento
quadrados = ['p_quadrado', 'b_quadrado']

def xeque(tabuleiro,linha,coluna,cor):

    #Verificação se há um peão na diagonal imediata antes de verificar as demais casas
    if cor == 'branca':
        if coluna < 7:
            if tabuleiro[linha - 1][coluna + 1] == f.corEpeca(f.inverteCor(cor), 'peao'):
                return True
        if coluna > 0:
            if tabuleiro[linha -1][coluna - 1] == f.corEpeca(f.inverteCor(cor), 'peao'):
                return True
    else:
        if coluna < 7:
            if tabuleiro[linha + 1][coluna + 1] == f.corEpeca(f.inverteCor(cor), 'peao'):
                return True
        if coluna > 0:
            if tabuleiro[linha + 1][coluna - 1] == f.corEpeca(f.inverteCor(cor), 'peao'):
                return True
    
    if f.verificacaoDiagonal(tabuleiro, linha, coluna, -1, 1, -1, 8,cor):
        return True #Casas superiores direita 
  
    if f.verificacaoDiagonal(tabuleiro, linha, coluna, -1, -1, -1, -1, cor):
        return True   #Casas superiores esquerda
    
    if f.verificacaoDiagonal(tabuleiro, linha, coluna, +1, +1, 8, 8, cor):
        return True #Casas inferior direita 
    
    if f.verificacaoDiagonal(tabuleiro, linha, coluna, +1, -1, 8, -1, cor):
        return True #Casas inferior esquerda 
    
    #VERIFICAÇÃO DAS CASAS EM "L" (Movimento do cavalo)
    for listas in m.possibilidadesL([linha, coluna]):
        i  = listas[0]
        j = listas[1]
        if tabuleiro[i][j] == f.corEpeca(f.inverteCor(cor), 'cavalo'):
            return True

    #VERIFICAÇÃO DAS CASAS HORIZINTAIS (Movimento da torre e da rainha)
    if f.verificacaoHorizontalEVertical(tabuleiro, linha, coluna, -1, 0, -1, 8, cor):
        return True #cima
    if f.verificacaoHorizontalEVertical(tabuleiro, linha, coluna, 1, 0, 8, 8, cor):
        return True #baixo
    if f.verificacaoHorizontalEVertical(tabuleiro, linha, coluna, 0, 1, 8, 8, cor):
        return True #direita
    if f.verificacaoHorizontalEVertical(tabuleiro, linha, coluna, 0, -1, 8, -1, cor):
        return True #esquerda
   
    return False

def formacaoOriginal(tabuleiro, posicaoRei, cor):
    multiplicador = -1 if cor == 'branca' else 1
    prefixoPeca = 'b_' if cor == 'branca' else 'p_'
    if tabuleiro[posicaoRei[0] + (1 * multiplicador)][posicaoRei[1]] == (prefixoPeca + 'peao') and tabuleiro[posicaoRei[0]][posicaoRei[1] + 1] == (prefixoPeca + 'bispo')and tabuleiro[posicaoRei[0]][posicaoRei[1] - 1] == (prefixoPeca + 'rainha'):
        return True
    return False

def xequeMate(tabuleiro, cor):
    posicaoRei = f.localizarRei(tabuleiro, cor)
    if (xeque(tabuleiro, posicaoRei[0], posicaoRei[1], cor)) and (m.reiPossibilidades(tabuleiro, f.valorOrigem(posicaoRei[1], posicaoRei[0]), cor) == []) and (not formacaoOriginal(tabuleiro, posicaoRei, cor)):
        return True
    else:
        return False
