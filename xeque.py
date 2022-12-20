#ARQUIVO QUE CONTÉM TODAS AS FUNÇÕES DE XEQUE E XEQUE-MATE

import funcs_auxiliares as f #Importa as funções auxiliares
import movimentos as m #Importa os movimentos das peças



# Função que varre o tabuleiro verificando todas as posições na vertical e horizontal, analisando se o rei está em xeque
def verificacaoHorizontalEVertical(tabuleiro, linha, coluna, proximaLinha, proximaColuna, limiteLinha, limiteColuna,cor):
  while True:
    coluna += proximaColuna
    linha += proximaLinha

    if coluna == limiteColuna or  linha == limiteLinha:
      break
    peca = tabuleiro[linha][coluna]
    if peca in m.aliados[cor] and peca != f.corEpeca(cor, 'rei'):
      return False
    if peca in m.adversarios[cor] and peca not in [f.corEpeca(f.inverteCor(cor), 'torre'),f.corEpeca(f.inverteCor(cor), 'rainha')]:
      return False
    if peca in m.adversarios[cor] and peca in [f.corEpeca(f.inverteCor(cor), 'torre'), f.corEpeca(f.inverteCor(cor), 'rainha')]:
      return True 
    
# Função que varre o tabuleiro verificando todas as posições na diagonal, analisando se o rei está em xeque
def verificacaoDiagonal(tabuleiro, contLinha, contColuna, proximaLinha, proximaColuna, limiteLinha, limiteColuna, cor):
  while True:
    contLinha += proximaLinha
    contColuna += proximaColuna

    if contColuna == limiteColuna or contLinha == limiteLinha:
        break
    peca = tabuleiro[contLinha][contColuna]
    if (peca in m.aliados[cor] and peca != f.corEpeca(cor, 'rei')):
        return False
    if (peca in m.adversarios[cor] and peca not in [f.corEpeca(f.inverteCor(cor), 'bispo'), f.corEpeca(f.inverteCor(cor), 'rainha')]):
       return False
    if peca in m.adversarios[cor] and peca in [f.corEpeca(f.inverteCor(cor), 'bispo'), f.corEpeca(f.inverteCor(cor), 'rainha')]:
        return True

#Retorna a posição do rei do jogador atual 
def localizarRei(tabuleiro, cor):
  for i in range(8):
    for j in range(8):
      if tabuleiro[i][j] == f.corEpeca(cor,'rei'):
        return [i, j]

#Tranforma a posição do jogador de par ordenado para uma string
def valorOrigem (coluna,linha):
  return '%s%s' %(f.letras[coluna],linha+1)

#Função responsável por verificar se uma posição qualquer está ameaçada por peças adversárias
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
    
    if verificacaoDiagonal(tabuleiro, linha, coluna, -1, 1, -1, 8,cor):
        return True #Casas superiores direita 
  
    if verificacaoDiagonal(tabuleiro, linha, coluna, -1, -1, -1, -1, cor):
        return True   #Casas superiores esquerda
    
    if verificacaoDiagonal(tabuleiro, linha, coluna, +1, +1, 8, 8, cor):
        return True #Casas inferior direita 
    
    if verificacaoDiagonal(tabuleiro, linha, coluna, +1, -1, 8, -1, cor):
        return True #Casas inferior esquerda 
    
    #VERIFICAÇÃO DAS CASAS EM "L" (Movimento do cavalo)
    for listas in m.possibilidadesL([linha, coluna]):
        i  = listas[0]
        j = listas[1]
        if tabuleiro[i][j] == f.corEpeca(f.inverteCor(cor), 'cavalo'):
            return True

    #VERIFICAÇÃO DAS CASAS HORIZINTAIS (Movimento da torre e da rainha)
    if verificacaoHorizontalEVertical(tabuleiro, linha, coluna, -1, 0, -1, 8, cor):
        return True #cima
    if verificacaoHorizontalEVertical(tabuleiro, linha, coluna, 1, 0, 8, 8, cor):
        return True #baixo
    if verificacaoHorizontalEVertical(tabuleiro, linha, coluna, 0, 1, 8, 8, cor):
        return True #direita
    if verificacaoHorizontalEVertical(tabuleiro, linha, coluna, 0, -1, 8, -1, cor):
        return True #esquerda
   
    return False

#Função que retorna um booleano caso o jogador atual tenha sofrido xeque-mate
def xequeMate(tabuleiro, cor):
    posicaoRei = localizarRei(tabuleiro, cor)
    if (xeque(tabuleiro, posicaoRei[0], posicaoRei[1], cor)) and (m.reiPossibilidades(tabuleiro, valorOrigem(posicaoRei[1], posicaoRei[0]), cor) == []) and (not auxiliarReiForaDeXeque(tabuleiro,cor)):
        return True
    else:
        return False

#Retorna um booleano se a possibilidade de movimento de qualquer peça aliada retira o rei de xeque  
def auxiliarReiForaDeXeque(tabuleiro,cor):
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna] in m.aliados[cor]:
                origem =valorOrigem(coluna,linha)
                for possibilidade in m.possibilidades(tabuleiro,origem,cor):
                    destino =valorOrigem(possibilidade[1],possibilidade[0])
                    if reiForaDeXeque(tabuleiro,cor,origem,destino):
                        return True
    return False                 

#Retorna um booleano se o movimento de uma peça retira o rei de xeque          
def reiForaDeXeque(copiaTabuleiro,cor,origem,destino):
  pecaAdversaria = copiaTabuleiro[f.linha(destino)][f.coluna(destino)]
  m.realizarMovimento(copiaTabuleiro,origem,destino)
  posicaoReiAliado = localizarRei(copiaTabuleiro, cor)
  foraDeXeque=  not xeque(copiaTabuleiro,posicaoReiAliado[0],posicaoReiAliado[1],cor)
  m.realizarMovimento(copiaTabuleiro,destino,origem)
  copiaTabuleiro[f.linha(destino)][f.coluna(destino)] = pecaAdversaria
  return foraDeXeque 

#Função que retorna a intersecção do movimento dos dois reis
def xequeReiparaRei (tabuleiro,possibilidades,cor):
    posicaoReiInimigo = localizarRei(tabuleiro,f.inverteCor(cor))
    possibilidadeReiAtual=possibilidades
    possibilidadeReiInimgo= m.auxiliarReiPossibilidades(valorOrigem(posicaoReiInimigo[1],posicaoReiInimigo[0]))
    interseccao = []
    #Procurando a intersecção de movimento entre os dois reis
    for possibilidades_a in possibilidadeReiAtual:
      for possibilidades_b in possibilidadeReiInimgo:
        if possibilidades_a == possibilidades_b:
          interseccao.append(possibilidades_a)
    return interseccao