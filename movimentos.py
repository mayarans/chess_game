import funcs_auxiliares as f
import xequeEMate as x

# Variáveis utilizadas em todas as funções de movimento
quadrados = ['p_quadrado', 'b_quadrado']
pecasPretas = ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre', 'p_peao']
pecasBrancas = ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre', 'b_peao']

# Função que retorna uma lista de movimentos possíveis para a peça escolhida pelo jogador
def possibilidades(tabuleiro, origem, cor):
  # Guardando o valor da peça na variável
  peca = tabuleiro[f.linha(origem)][f.coluna(origem)]
  # Verificando se a peça é um peão
  if peca in ['p_peao', 'b_peao']:
    return peaoPossibilidades(tabuleiro, origem, cor)
  # Verificando se a peça é um cavalo
  elif peca in ['p_cavalo', 'b_cavalo']:
    return cavaloPossibilidades(tabuleiro, origem, cor)
  # Verificando se a peça é uma torre
  elif peca in ['p_torre', 'b_torre']:
    return torrePossibilidades(tabuleiro, origem, cor)
  elif peca in ['p_bispo','b_bispo']:
    return bispoPossibilidades(tabuleiro,origem,cor)
  elif peca in['b_rainha','p_rainha']:
    return rainhaPossibilidades(tabuleiro,origem,cor)
  elif peca in ['b_rei','p_rei']:
    return reiPossibilidades(tabuleiro,origem,cor)

# Função que retorna todas as possibilidades de movimento caso a peça seja o peão
def peaoPossibilidades(tabuleiro, origem, cor):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  resultado = []

  if cor == 'branca': # Condição para as peças brancas
    # Movimento do peão duas casas para frente caso seja a primeira jogada
    if linha == 6:
      if tabuleiro[linha - 2][coluna] in quadrados:
        lista = [linha - 2, coluna]
        resultado.append(lista)
    if linha > 0:
      # Movimento do peão uma casa para frente
      if tabuleiro[linha - 1][coluna] in quadrados:
        lista = [linha - 1, coluna]
        resultado.append(lista)
      # Movimento do peão para as diagonais (comer uma peça)
      if coluna < 7:
        if (tabuleiro[linha - 1][coluna + 1] in pecasPretas):
          lista = [linha - 1, coluna + 1]
          resultado.append(lista)
      if coluna > 0:
        if (tabuleiro[linha - 1][coluna - 1] in pecasPretas):
          lista = [linha - 1, coluna - 1]
          resultado.append(lista)
  
  elif cor == 'preta': # Condição para as peças pretas
    # Movimento do peão duas casas para frente caso seja a primeira jogada
    if linha == 1:
      if tabuleiro[linha + 2][coluna] in quadrados:
        lista = [linha + 2, coluna]
        resultado.append(lista)
    if linha < 7:
      # Movimento do peão uma casa para frente
      if tabuleiro[linha + 1][coluna] in quadrados:
        lista = [linha + 1, coluna]
        resultado.append(lista)
      # Movimento do peão para as diagonais (comer uma peça)
      if coluna < 7:
        if (tabuleiro[linha + 1][coluna + 1] in pecasBrancas):
          lista = [linha + 1, coluna + 1]
          resultado.append(lista)
      if coluna >= 0:
        if (tabuleiro[linha + 1][coluna - 1] in pecasBrancas):
          lista = [linha + 1, coluna - 1]
          resultado.append(lista)
  return resultado

# Função que retorna todas as possibilidades de movimento caso a peça seja o cavalo
def cavaloPossibilidades(tabuleiro, origem, cor):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  resultado = []

  if cor == 'branca': # Condição para as peças brancas
    # Movimento do cavalo em forma de L para as quatro direções:
    # Para baixo
    if linha < 6: 
      if coluna < 7:
        if (tabuleiro[linha + 2][coluna + 1] in quadrados) or (tabuleiro[linha + 2][coluna + 1] in pecasPretas):
          resultado.append([linha + 2, coluna + 1])
      if coluna > 0:
        if (tabuleiro[linha + 2][coluna - 1] in quadrados) or (tabuleiro[linha + 2][coluna - 1] in pecasPretas):
          resultado.append([linha + 2, coluna - 1])
    # Para cima
    if linha > 1:
      if coluna < 7:
        if (tabuleiro[linha - 2][coluna + 1] in quadrados) or (tabuleiro[linha - 2][coluna + 1] in pecasPretas):
          resultado.append([linha - 2, coluna + 1])
      if coluna > 0:
        if (tabuleiro[linha - 2][coluna - 1] in quadrados) or (tabuleiro[linha - 2][coluna - 1] in pecasPretas):
          resultado.append([linha - 2, coluna - 1])
    # Lado direito
    if coluna < 6:
      if linha < 7:
        if (tabuleiro[linha+1][coluna+2] in quadrados) or (tabuleiro[linha+1][coluna+2] in pecasPretas):
          resultado.append([linha+1, coluna+2])
      if linha > 0:
        if (tabuleiro[linha-1][coluna+2] in quadrados) or (tabuleiro[linha-1][coluna+2] in pecasPretas):
          resultado.append([linha-1, coluna+2])
    # Lado esquerdo
    if coluna > 1:
      if linha < 7:
        if (tabuleiro[linha+1][coluna-2] in quadrados) or (tabuleiro[linha+1][coluna-2] in pecasPretas):
          resultado.append([linha+1, coluna-2])
      if linha > 0:
        if (tabuleiro[linha-1][coluna-2] in quadrados) or (tabuleiro[linha-1][coluna-2] in pecasPretas):
          resultado.append([linha-1, coluna-2])
    
  elif cor == 'preta': # Condição para as peças pretas
    # Movimento do cavalo em forma de L para as quatro direções:
    # Para baixo
    if linha < 6: 
      if coluna < 7:
        if (tabuleiro[linha + 2][coluna + 1] in quadrados) or (tabuleiro[linha + 2][coluna + 1] in pecasBrancas):
          resultado.append([linha + 2, coluna + 1])
      if coluna > 0:
        if (tabuleiro[linha + 2][coluna - 1] in quadrados) or (tabuleiro[linha + 2][coluna - 1] in pecasBrancas):
          resultado.append([linha + 2, coluna - 1])
    # Para cima
    if linha > 1:
      if coluna < 7:
        if (tabuleiro[linha - 2][coluna + 1] in quadrados) or (tabuleiro[linha - 2][coluna + 1] in pecasBrancas):
          resultado.append([linha - 2, coluna + 1])
      if coluna > 0:
        if (tabuleiro[linha - 2][coluna - 1] in quadrados) or (tabuleiro[linha - 2][coluna - 1] in pecasBrancas):
          resultado.append([linha - 2, coluna - 1])
    # Lado direito
    if coluna < 6:
      if linha < 7:
        if (tabuleiro[linha+1][coluna+2] in quadrados) or (tabuleiro[linha+1][coluna+2] in pecasBrancas):
          resultado.append([linha+1, coluna+2])
      if linha > 0:
        if (tabuleiro[linha-1][coluna+2] in quadrados) or (tabuleiro[linha-1][coluna+2] in pecasBrancas):
          resultado.append([linha-1, coluna+2])
    # Lado esquerdo
    if coluna > 1:
      if linha < 7:
        if (tabuleiro[linha+1][coluna-2] in quadrados) or (tabuleiro[linha+1][coluna-2] in pecasBrancas):
          resultado.append([linha+1, coluna-2])
      if linha > 0:
        if (tabuleiro[linha-1][coluna-2] in quadrados) or (tabuleiro[linha-1][coluna-2] in pecasBrancas):
          resultado.append([linha-1, coluna-2])

  return resultado


def torrePossibilidades(tabuleiro, origem, cor):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  resultado = []

  if cor == 'branca': # Possibilidades de movimentos para as peças brancas
    # Movimento da peça para cima
    if linha > 0:
      for i in range(linha-1, 0, -1):
        if tabuleiro[i][coluna] in pecasBrancas:
          break
        elif tabuleiro[i][coluna] in pecasPretas:
          resultado.append([i, coluna])
          break
        elif tabuleiro[i][coluna] in quadrados:
          resultado.append([i, coluna])

    # Movimento da peça para baixo
    if linha < 7:
      for i in range(linha+1, 8):
        if tabuleiro[i][coluna] in pecasBrancas:
          break
        elif tabuleiro[i][coluna] in pecasPretas:
          resultado.append([i, coluna])
          break
        elif tabuleiro[i][coluna] in quadrados:
          resultado.append([i, coluna])
    
    # Movimento da peça para o lado direito
    if coluna < 7:
      for i in range(coluna+1, 8):
        if tabuleiro[linha][i] in pecasBrancas:
          break
        elif tabuleiro[linha][i] in pecasPretas:
          resultado.append([linha, i])
          break
        elif tabuleiro[linha][i] in quadrados:
          resultado.append([linha, i])

    # Movimento da peça para o lado esquerdo
    if coluna > 0:
      for i in range(coluna-1, 0, -1):
        if tabuleiro[linha][i] in pecasBrancas:
          break
        elif tabuleiro[linha][i] in pecasPretas:
          resultado.append([linha, i])
          break
        elif tabuleiro[linha][i] in quadrados:
          resultado.append([linha, i])

  if cor == 'preta': # Possibilidades de movimentos para as peças pretas
    # Movimento da peça para cima
    if linha > 0:
      for i in range(linha-1, 0, -1):
        if tabuleiro[i][coluna] in pecasPretas:
          break
        elif tabuleiro[i][coluna] in pecasBrancas:
          resultado.append([i, coluna])
          break
        elif tabuleiro[i][coluna] in quadrados:
          resultado.append([i, coluna])

    # Movimento da peça para baixo
    if linha < 7:
      for i in range(linha+1, 8):
        if tabuleiro[i][coluna] in pecasPretas:
          break
        elif tabuleiro[i][coluna] in pecasBrancas:
          resultado.append([i, coluna])
          break
        elif tabuleiro[i][coluna] in quadrados:
          resultado.append([i, coluna])
    
    # Movimento da peça para o lado direito
    if coluna < 7:
      for i in range(coluna+1, 8):
        if tabuleiro[linha][i] in pecasPretas:
          break
        elif tabuleiro[linha][i] in pecasBrancas:
          resultado.append([linha, i])
          break
        elif tabuleiro[linha][i] in quadrados:
          resultado.append([linha, i])

    # Movimento da peça para o lado esquerdo
    if coluna > 0:
      for i in range(coluna-1, 0, -1):
        if tabuleiro[linha][i] in pecasPretas:
          break
        elif tabuleiro[linha][i] in pecasBrancas:
          resultado.append([linha, i])
          break
        elif tabuleiro[linha][i] in quadrados:
          resultado.append([linha, i])
  return resultado

def bispoPossibilidades(tabuleiro,origem,cor):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  resultado = []
  contLinha= linha
  contColuna= coluna
  if cor == 'branca':
    #Movimento superior direito do bispo
    while True:
      if contColuna>= 7 or contLinha<=0:
        break
      else:
        contLinha-=1
        contColuna+=1
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
            break
        if tabuleiro[contLinha][contColuna] in pecasPretas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna
    #movimento superior esquerdo
    while True:
      if contColuna <= 0 or contLinha<=0:
        break
      else:
        contLinha-=1
        contColuna-=1
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          break
        if tabuleiro[contLinha][contColuna] in pecasPretas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna      
    #Movimento inferior direito
    while True:
      if contColuna >= 7 or contLinha >= 7:
        break
      else:
        contLinha+=1
        contColuna+=1
        print(contLinha,contColuna)
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
            break
        if tabuleiro[contLinha][contColuna] in pecasPretas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna
    #Movimento inferior esquerdo   
    while True:
      if contColuna <= 0 or contLinha >= 7:
        break
      else:
        contLinha+=1
        contColuna-=1
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
            break
        if tabuleiro[contLinha][contColuna] in pecasPretas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna   

  elif cor == 'preta':
    #Movimento superior direito do bispo
    while True:
      if contColuna>= 7 or contLinha<=0:
        break
      else:
        contLinha-=1
        contColuna+=1
        if tabuleiro[contLinha][contColuna] in pecasPretas:
            break
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna
    #movimento superior esquerdo
    while True:
      if contColuna <= 0 or contLinha<=0:
        break
      else:
        contLinha-=1
        contColuna-=1
        if tabuleiro[contLinha][contColuna] in pecasPretas:
            break
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna      
    #Movimento inferior direito
    while True:
      if contColuna >= 7 or contLinha >= 7:
        break
      else:
        contLinha+=1
        contColuna+=1
        if tabuleiro[contLinha][contColuna] in pecasPretas:
            break
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna
    #Movimento inferior esquerdo   
    while True:
      if contColuna < 0 or contLinha > 7:
        break
      else:
        contLinha+=1
        contColuna-=1
        if tabuleiro[contLinha][contColuna] in pecasPretas:
            break
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna   
  return resultado    

def rainhaPossibilidades(tabuleiro,origem,cor):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  resultado = []
  contLinha= linha
  contColuna= coluna

  if cor == 'branca':
    #MOVIMENTOS VERTICAIS E HORIZONTAIS
    # Movimento da peça para cima
    if linha > 0:
      for i in range(linha-1, 0, -1):
        if tabuleiro[i][coluna] in pecasBrancas:
          break
        elif tabuleiro[i][coluna] in pecasPretas:
          resultado.append([i, coluna])
          break
        elif tabuleiro[i][coluna] in quadrados:
          resultado.append([i, coluna])

    # Movimento da peça para baixo
    if linha < 7:
      for i in range(linha+1, 8):
        if tabuleiro[i][coluna] in pecasBrancas:
          break
        if tabuleiro[i][coluna] in pecasPretas:
          resultado.append([i, coluna])
          break
        if tabuleiro[i][coluna] in quadrados:
          resultado.append([i, coluna])
    
    # Movimento da peça para o lado direito
    if coluna < 7:
      for i in range(coluna+1, 8):
        if tabuleiro[linha][i] in pecasBrancas:
          break
        elif tabuleiro[linha][i] in pecasPretas:
          resultado.append([linha, i])
          break
        elif tabuleiro[linha][i] in quadrados:
          resultado.append([linha, i])

    # Movimento da peça para o lado esquerdo
    if coluna > 0:
      for i in range(coluna-1, 0, -1):
        if tabuleiro[linha][i] in pecasBrancas:
          break
        elif tabuleiro[linha][i] in pecasPretas:
          resultado.append([linha, i])
          break
        elif tabuleiro[linha][i] in quadrados:
          resultado.append([linha, i])
    #MOVIMENTOS DIAGONAIS
    #Movimento superior direito do bispo
    while True:
      if contColuna>= 7 or contLinha<=0:
        break
      else:
        contLinha-=1
        contColuna+=1
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
            break
        if tabuleiro[contLinha][contColuna] in pecasPretas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna
    #movimento superior esquerdo
    while True:
      if contColuna <= 0 or contLinha<=0:
        break
      else:
        contLinha-=1
        contColuna-=1
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          break
        if tabuleiro[contLinha][contColuna] in pecasPretas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna      
    #Movimento inferior direito
    while True:
      if contColuna >= 7 or contLinha >= 7:
        break
      else:
        contLinha+=1
        contColuna+=1
        print(contLinha,contColuna)
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
            break
        if tabuleiro[contLinha][contColuna] in pecasPretas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna
    #Movimento inferior esquerdo   
    while True:
      if contColuna <= 0 or contLinha >= 7:
        break
      else:
        contLinha+=1
        contColuna-=1
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
            break
        if tabuleiro[contLinha][contColuna] in pecasPretas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna   

  elif cor == 'preta':
    #MOVIMENTOS VERTICAIS E HORIZONTAIS 
    # Movimento da peça para cima
    if linha > 0:
      for i in range(linha-1, 0, -1):
        if tabuleiro[i][coluna] in pecasPretas:
          break
        elif tabuleiro[i][coluna] in pecasBrancas:
          resultado.append([i, coluna])
          break
        elif tabuleiro[i][coluna] in quadrados:
          resultado.append([i, coluna])

    # Movimento da peça para baixo
    if linha < 7:
      for i in range(linha+1, 8):
        if tabuleiro[i][coluna] in pecasPretas:
          break
        elif tabuleiro[i][coluna] in pecasBrancas:
          resultado.append([i, coluna])
          break
        elif tabuleiro[i][coluna] in quadrados:
          resultado.append([i, coluna])
    
    # Movimento da peça para o lado direito
    if coluna < 7:
      for i in range(coluna+1, 8):
        if tabuleiro[linha][i] in pecasPretas:
          break
        elif tabuleiro[linha][i] in pecasBrancas:
          resultado.append([linha, i])
          break
        elif tabuleiro[linha][i] in quadrados:
          resultado.append([linha, i])

    # Movimento da peça para o lado esquerdo
    if coluna > 0:
      for i in range(coluna-1, 0, -1):
        if tabuleiro[linha][i] in pecasPretas:
          break
        elif tabuleiro[linha][i] in pecasBrancas:
          resultado.append([linha, i])
          break
        elif tabuleiro[linha][i] in quadrados:
          resultado.append([linha, i])
    #MOVIMENTOS HORIZONTAIS
    #Movimento superior direito do bispo
    while True:
      if contColuna>= 7 or contLinha<=0:
        break
      else:
        contLinha-=1
        contColuna+=1
        if tabuleiro[contLinha][contColuna] in pecasPretas:
            break
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna
    #movimento superior esquerdo
    while True:
      if contColuna <= 0 or contLinha<=0:
        break
      else:
        contLinha-=1
        contColuna-=1
        if tabuleiro[contLinha][contColuna] in pecasPretas:
            break
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna      
    #Movimento inferior direito
    while True:
      if contColuna >= 7 or contLinha >= 7:
        break
      else:
        contLinha+=1
        contColuna+=1
        if tabuleiro[contLinha][contColuna] in pecasPretas:
            break
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])
    contLinha= linha
    contColuna= coluna
    #Movimento inferior esquerdo   
    while True:
      if contColuna <= 0 or contLinha >= 7:
        break
      else:
        contLinha+=1
        contColuna-=1
        if tabuleiro[contLinha][contColuna] in pecasPretas:
            break
        if tabuleiro[contLinha][contColuna] in pecasBrancas:
          resultado.append([contLinha,contColuna])
          break
        if tabuleiro[contLinha][contColuna] in quadrados:
          resultado.append([contLinha,contColuna])   
  return resultado
   
def reiPossibilidades(tabuleiro,origem,cor):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  resultado = []
  #MOVIMENTOS HORIZONTAIS E VERTICAIS
  #Movimento para cima
  if linha > 0:
    if tabuleiro[linha-1][coluna] in quadrados or tabuleiro[linha-1][coluna] in f.listaDePecas(f.inverteCor(cor)):
      if not x.xeque(tabuleiro,(linha-1),coluna,cor):
        resultado.append([linha-1,coluna])
#Movimento para baixo
  if linha<7:
    if tabuleiro[linha+1][coluna] in quadrados or tabuleiro[linha+1][coluna] in f.listaDePecas(f.inverteCor(cor)):
      if not x.xeque(tabuleiro,linha+1,coluna,cor):
        resultado.append([linha+1,coluna]) 
#Movimento para direita  
  if coluna<7:
    if tabuleiro[linha][coluna+1] in quadrados or tabuleiro[linha][coluna+1] in f.listaDePecas(f.inverteCor(cor)):
      if not x.xeque(tabuleiro,linha,coluna+1,cor):
        resultado.append([linha,coluna+1])    
#Movimento para esquerda
  if coluna>0:
    if tabuleiro[linha][coluna-1] in quadrados or tabuleiro[linha][coluna-1] in f.listaDePecas(f.inverteCor(cor)):
      if not x.xeque(tabuleiro,linha,coluna-1,cor):
        resultado.append([linha,coluna-1])
#MOVIMENTOS DIAGONAIS
#Movimento superior direito
  if coluna<7 and linha>0:
    if tabuleiro[linha-1][coluna+1] in quadrados or tabuleiro[linha-1][coluna+1] in f.listaDePecas(f.inverteCor(cor)):
      if not x.xeque(tabuleiro,linha-1,coluna+1,cor):
        resultado.append([linha-1,coluna+1])
#Movimento superior esquerdo
  if coluna>0 and linha>0:
    if tabuleiro[linha-1][coluna-1] in quadrados or tabuleiro[linha-1][coluna-1] in f.listaDePecas(f.inverteCor(cor)):
      if not x.xeque(tabuleiro,linha-1,coluna-1,cor):
        resultado.append([linha-1,coluna-1])
#Movimento inferior direito
  if coluna<7 and linha<7:
    if tabuleiro[linha+1][coluna+1] in quadrados or tabuleiro[linha+1][coluna+1] in f.listaDePecas(f.inverteCor(cor)):
      if not x.xeque(tabuleiro,linha+1,coluna+1,cor):
        resultado.append([linha+1,coluna+1])
#Movimento inferior esquerdo
  if coluna>0 and linha<7:
    if tabuleiro[linha+1][coluna-1] in quadrados or tabuleiro[linha+1][coluna-1] in f.listaDePecas(f.inverteCor(cor)):
      if not x.xeque(tabuleiro,linha+1,coluna-1,cor):
        resultado.append([linha+1,coluna-1])
  return resultado



# Função para verificar se o destino da peça está dentro das possibilidades determinadas na função possibilidades()
def verificarDestinoValido(destino, possibilidades):
    posicaoDestino = [f.linha(destino), f.coluna(destino)]
    return posicaoDestino in possibilidades


# Função para realizar o movimento da peça e substituir sua posição de origem pelo quadrado correspondente
def realizarMovimento(tabuleiro, origem, destino):
  tabuleiro[f.linha(destino)][f.coluna(destino)] = tabuleiro[f.linha(origem)][f.coluna(origem)]
  # Lógica para identificar se o quadrado é branco ou preto
  if (f.linha(origem) + f.coluna(origem)) % 2 == 0:
    tabuleiro[f.linha(origem)][f.coluna(origem)] = 'b_quadrado'
  else:
    tabuleiro[f.linha(origem)][f.coluna(origem)] = 'p_quadrado'
