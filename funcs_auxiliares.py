import time, sys

# Letras que representam as colunas da matriz tabuleiro
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Função que retorna linha em que está localizada a peça
def linha(posicao):
  return int(posicao[1:])-1

# Função que retorna coluna em que está localizada a peça
def coluna(posicao):
  return letras.index(posicao[0])

# Função que verifica e retorna se a posição de origem é uma peça válida
def verificarOrigemValida(tabuleiro, origem, cor):
  quadrados = ['p_quadrado', 'b_quadrado']
  pecasPretas = ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre', 'p_peao']
  pecasBrancas = ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre', 'b_peao']
  try:
    # Lista de posicão de linha e coluna da peça
    lista = [linha(origem), coluna(origem)]
    # Verificando se a posição de origem contém uma peça branca
    if cor == 'branca' and tabuleiro[lista[0]][lista[1]] not in quadrados:
      if tabuleiro[lista[0]][lista[1]] not in pecasPretas:
        resposta = 'ok'
      else:
        resposta = 'Você está tentando mover uma peça preta. Aguarde sua vez!'
    # Verificando se a posição de origem contém uma peça preta
    elif cor == 'preta' and tabuleiro[lista[0]][lista[1]] not in quadrados:
      if tabuleiro[lista[0]][lista[1]] not in pecasBrancas:
        resposta = 'ok'
      else:
        resposta = 'Você está tentando mover uma peça branca. Aguarde sua vez!'
    else:
      resposta = 'Não há peças nesta posição. Tente novamente!'
  except (ValueError, IndexError):
    resposta = 'Esta posição não está dentro dos limites do tabuleiro. Tente novamente!'
  return resposta


# Função auxiliar para simular o carregamento do jogo de xadrez
def loading():
  print("Carregando o jogo...")
  for i in range(0, 100):
    time.sleep(0.1)
    width = int((i + 1) / 4)
    bar = "[" + "#" * width + " " * (25 - width) + "]"
    sys.stdout.write(u"\u001b[1000D" +  bar)
    sys.stdout.flush()
  print()
