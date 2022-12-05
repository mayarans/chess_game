import funcs_auxiliares as f

# Função que retorna uma lista de movimentos possíveis para a peça escolhida pelo jogador
def possibilidades(tabuleiro, origem, cor):
  # Guardando o valor da peça na variável
  peca = tabuleiro[f.linha(origem)][f.coluna(origem)]
  # Verificando se a peça é um peão
  if peca in ['p_peao', 'b_peao']:
    return peaoPossibilidades(tabuleiro, origem, cor)

# Função que retorna todas as possibilidades de movimento caso a peça seja o peão
def peaoPossibilidades(tabuleiro, origem, cor):
  linha = f.linha(origem)
  coluna = f.coluna(origem)
  resultado = []
  quadrados = ['p_quadrado', 'b_quadrado']
  pecasPretas = ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre', 'p_peao']
  pecasBrancas = ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre', 'b_peao']
  if cor == 'branca':
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
  elif cor == 'preta':
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

# Função para verificar se o destino da peça está dentro das possibilidades determinadas na função possibilidades()
def verificarDestinoValido(destino, possibilidades):
  posicaoDestino = [f.linha(destino), f.coluna(destino)]
  return posicaoDestino in possibilidades

# Função para realizar o movimento da peça e substituir sua posição de origem pelo quadrado correspondente
def realizarMovimento(tabuleiro, origem, destino):
  tabuleiro[f.linha(destino)][f.coluna(destino)] = tabuleiro[f.linha(origem)][f.coluna(origem)]
  if (f.linha(origem) + f.coluna(origem)) % 2 == 0:
    tabuleiro[f.linha(origem)][f.coluna(origem)] = 'b_quadrado'
  else:
    tabuleiro[f.linha(origem)][f.coluna(origem)] = 'p_quadrado'


