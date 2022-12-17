import funcs_auxiliares as f
import xeque as x

# Variáveis utilizadas em todas as funções de movimento
aliados = {"preta": ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre', 'p_peao'], "branca": ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre', 'b_peao']}
adversarios = {"branca": ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre', 'p_peao'], "preta": ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre', 'b_peao']}

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

  multiplicador = 1 if cor == "preta" else -1
    # Movimento do peão duas casas para frente caso seja a primeira jogada
  if linha in [1, 6]:
    if tabuleiro[linha + (2 * multiplicador)][coluna] not in (adversarios[cor] + aliados[cor]):
      lista = [linha + (2 * multiplicador), coluna]
      resultado.append(lista)
  # Movimento do peão uma casa para frente
  if tabuleiro[linha + (1 * multiplicador)][coluna] not in (adversarios[cor] + aliados[cor]):
    lista = [linha + (1 * multiplicador), coluna]
    resultado.append(lista)
  # Movimento do peão para as diagonais (comer uma peça)
  for i in range(-1, 2, 2):
    proximaLinha = linha + (1 * multiplicador)
    proximaColuna = coluna + i
    if proximaLinha in range(8) and proximaColuna in range(8):
      if (tabuleiro[proximaLinha][proximaColuna] in adversarios[cor]):
        lista = [proximaLinha, proximaColuna]
        resultado.append(lista)
  
  return limites(resultado)


def possibilidadesL(posicao):
  linha, coluna = posicao
  resultado = []
  for i in range(-1,2,2):
    for j in range(-2,3,4):
      resultado.append([linha+i, coluna+j])
      resultado.append([linha+j, coluna+i])
    
  return limites(resultado)


# Função que retorna todas as possibilidades de movimento caso a peça seja o cavalo
def cavaloPossibilidades(tabuleiro, origem, cor):
  linha, coluna = f.linha(origem), f.coluna(origem)
  pecasAliadas = aliados[cor]

  movimentosPossiveis = []
  for i in possibilidadesL([linha, coluna]):
    posicaoAtual = tabuleiro[i[0]][i[1]]
    if posicaoAtual not in pecasAliadas:
      movimentosPossiveis.append(i)
  return movimentosPossiveis


def torrePossibilidades(tabuleiro, origem, cor):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  
  movimentosPossiveis = []
  for i in range(-1, 2, 2): # -1 1
    possibilidadesVertical = auxiliarRainhaPossibilidades(tabuleiro, [linha, coluna], [i, 0], [-1 if i == -1 else 8, -1], cor)
    possibilidadesHorizontal = auxiliarRainhaPossibilidades(tabuleiro, [linha, coluna], [0, i], [-1, 8 if i == 1 else -1], cor)
    movimentosPossiveis.extend(possibilidadesVertical)
    movimentosPossiveis.extend(possibilidadesHorizontal)
  
  return movimentosPossiveis


def auxiliarRainhaPossibilidades(tabuleiro, posicao, proximaPosicao, limite, cor):
  contLinha, contColuna = posicao
  pecasAliadas = aliados[cor]
  pecasAdversarias = adversarios[cor]

  resultado = []
  while True:
    contLinha += proximaPosicao[0]
    contColuna += proximaPosicao[1]
    if contLinha == limite[0] or contColuna == limite[1]:
        break
    peca = tabuleiro[contLinha][contColuna]
    if peca in pecasAliadas:
        break
    elif peca in pecasAdversarias:
      resultado.append([contLinha, contColuna])
      break
    resultado.append([contLinha, contColuna])
  
  return resultado


def bispoPossibilidades(tabuleiro, origem, cor):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  movimentosPossiveis = []

  # Verificando movimento em todas as direções
  for i in range(-1, 2, 2):
    for j in range(-1, 2, 2):
      possibilidadesDiagonal = auxiliarRainhaPossibilidades(tabuleiro, [linha, coluna], [i, j], [-1 if i == -1 else 8, 8 if j == 1 else -1], cor)
      movimentosPossiveis.extend(possibilidadesDiagonal)
  
  return movimentosPossiveis


def rainhaPossibilidades(tabuleiro,origem,cor):
  return bispoPossibilidades(tabuleiro, origem, cor) + torrePossibilidades(tabuleiro, origem, cor)


def auxiliarReiPossibilidades(origem):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  resultado = []

  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      resultado.append([linha + i, coluna + j])
  
  return limites(resultado)

#Função que retorna a intersecção do movimento dos dois reis
def xequeReiparaRei (tabuleiro,possibilidades,cor):
    posicaoReiInimigo = f.localizarRei(tabuleiro,f.inverteCor(cor))
    possibilidadeReiAtual=possibilidades
    possibilidadeReiInimgo= auxiliarReiPossibilidades(f.valorOrigem(posicaoReiInimigo[1],posicaoReiInimigo[0]))
    interseccao = []
    #Procurando a intersecção de movimento entre os dois reis
    for possibilidades_a in possibilidadeReiAtual:
      for possibilidades_b in possibilidadeReiInimgo:
        if possibilidades_a == possibilidades_b:
          interseccao.append(possibilidades_a)
    return interseccao

# Função que retorna todas as possibilidades de movimento para um rei
def reiPossibilidades(tabuleiro, origem, cor):
  # Recebendo as peças da mesma cor
  pecasAliadas = aliados[cor]

  # Atualizando a lista dentro dos limites do tabuleiro e verificando as posições possíveis para movimento
  movimentosPossiveis = []
  possibilidades = auxiliarReiPossibilidades(origem)
  #Verficando se as possibilidades de movimento do rei atual
  for i in possibilidades:
    posicaoAtual = tabuleiro[i[0]][i[1]]
    if posicaoAtual not in pecasAliadas and not x.xeque(tabuleiro, i[0], i[1], cor) and i not in xequeReiparaRei(tabuleiro,possibilidades,cor):
      movimentosPossiveis.append([i[0], i[1]])
  
  return movimentosPossiveis


# Função para verificar se o destino da peça está dentro das possibilidades determinadas na função possibilidades()
def verificarDestinoValido(destino, possibilidades):
    posicaoDestino = [f.linha(destino), f.coluna(destino)]
    return posicaoDestino in possibilidades

def reiForaDeXeque(copiaTabuleiro,cor,origem,destino):
  realizarMovimento(copiaTabuleiro,origem,destino)
  posicaoReiAliado =f.localizarRei(copiaTabuleiro, cor)
  foraDeXeque=  not x.xeque(copiaTabuleiro,posicaoReiAliado[0],posicaoReiAliado[1],cor)
  realizarMovimento(copiaTabuleiro,destino,origem)
  return foraDeXeque

# Função para realizar o movimento da peça e substituir sua posição de origem pelo quadrado correspondente
def realizarMovimento(tabuleiro, origem, destino):
  tabuleiro[f.linha(destino)][f.coluna(destino)] = tabuleiro[f.linha(origem)][f.coluna(origem)]
  # Lógica para identificar se o quadrado é branco ou preto
  if (f.linha(origem) + f.coluna(origem)) % 2 == 0:
    tabuleiro[f.linha(origem)][f.coluna(origem)] = 'b_quadrado'
  else:
    tabuleiro[f.linha(origem)][f.coluna(origem)] = 'p_quadrado'


def limites(possibilidades):
  limites = range(8)
  return [i for i in possibilidades if i[0] in limites and i[1] in limites]
