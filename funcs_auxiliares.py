#ARQUIVO QUE CONTÉM FUNÇÕES QUE AULIXIAM NO FUNCIONAMENTO DO RESTANTE DO PROGRAMA 

import time, sys #Importação de módulos que auxiliam no carregamento
import estilos as e #Importa os estilos aplicados as strings
from os import system, name #Importação de módulos que auxiliam na limpeza de tela
import movimentos as m #Importa os movimentos das peças

# Função utilizada para limpar a tela a cada jogada
def limparTela():
    # Para windows
    if name == 'nt':
      system('cls')
    # Para mac e linux
    else:
      system('clear')

# Função auxiliar para simular o carregamento do jogo de xadrez
def carregamentoJogo():
  print("Carregando o jogo...")
  for i in range(0, 100):
    time.sleep(0.1) # Pausa o programa por 0.1s
    tamanhoBarra = int((i + 1) / 4)
    barra = "[" + "#" * tamanhoBarra + " " * (25 - tamanhoBarra) + "]"
    sys.stdout.write(u"\u001b[1000D" +  barra)
    sys.stdout.flush()
  print()

# Letras que representam as colunas da matriz tabuleiro
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Função que retorna linha em que está localizada a peça
def linha(posicao):
  if len(posicao) > 1 and int(posicao[1:]) in range(1, 9):
    return int(posicao[1:])-1

# Função que retorna coluna em que está localizada a peça
def coluna(posicao):
  if posicao[0] in letras:
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
        resposta = f'\n{e.estilos["VERMELHO"]}Você está tentando mover uma peça preta. Aguarde sua vez!{e.estilos["REDEFINIR"]}\n'
    # Verificando se a posição de origem contém uma peça preta
    elif cor == 'preta' and tabuleiro[lista[0]][lista[1]] not in quadrados:
      if tabuleiro[lista[0]][lista[1]] not in pecasBrancas:
        resposta = 'ok'
      else:
        resposta = f'\n{e.estilos["VERMELHO"]}Você está tentando mover uma peça branca. Aguarde sua vez!{e.estilos["REDEFINIR"]}\n'
    else:
      resposta = f'\n{e.estilos["VERMELHO"]}Não há peças nesta posição. Indique uma posição válida!{e.estilos["REDEFINIR"]}\n'
  except (ValueError, IndexError, TypeError):
    resposta = f'\n{e.estilos["VERMELHO"]}Esta posição não está dentro dos limites do tabuleiro. Tente novamente!{e.estilos["REDEFINIR"]}\n'

  return resposta

# Função que define o jogador na rodada atual

def jogadorDaVez(cor, jogador1, jogador2):
  if cor == 'branca':
    return jogador1
  return jogador2

#Funções para dinamizar o uso da cor -  CorEPeca() retorna o nome de uma peça da cor atual - inverteCor() inverte a cor atual
def corEpeca(cor, nome):
  if cor == 'preta':
    return 'p_' + nome
  elif cor == 'branca':
    return 'b_' + nome

def inverteCor(cor):
  if cor == 'branca':
    cor='preta'
  else:
    cor='branca'
  return cor
