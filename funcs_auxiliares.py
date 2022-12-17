import time, sys
import estilos as e
import movimentos as m
import xequeEMate as x

# Letras que representam as colunas da matriz tabuleiro
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Função que retorna linha em que está localizada a peça
def linha(posicao):
  if len(posicao) > 1 and posicao[1:] in range(1, 9):
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
        resposta = f'\n{e.estilos["VERMELHO"]}Você está tentando mover uma peça preta. Aguarde sua vez!{e.estilos["RESET"]}\n'
    # Verificando se a posição de origem contém uma peça preta
    elif cor == 'preta' and tabuleiro[lista[0]][lista[1]] not in quadrados:
      if tabuleiro[lista[0]][lista[1]] not in pecasBrancas:
        resposta = 'ok'
      else:
        resposta = f'\n{e.estilos["VERMELHO"]}Você está tentando mover uma peça branca. Aguarde sua vez!{e.estilos["RESET"]}\n'
    else:
      resposta = f'\n{e.estilos["VERMELHO"]}Não há peças nesta posição. Indique uma posição válida!{e.estilos["RESET"]}\n'
  except (ValueError, IndexError):
    resposta = f'\n{e.estilos["VERMELHO"]}Esta posição não está dentro dos limites do tabuleiro. Tente novamente!{e.estilos["RESET"]}\n'

  return resposta

# Função que define o jogador na rodada atual

def jogadorDaVez(cor,jogador1,jogador2):
  if cor=='branca':
    return jogador1
  else:
    return jogador2
    
# def jogadorDaVez(cor, jogador1, jogador2):
#   if cor == 'branca':
#     return f'{e.estilos["CIANO_NEGRITO"]}Jogador da vez: {jogador1.upper()}{e.estilos["RESET"]}'
#   else: # Cor preta
#     return f'{e.estilos["CIANO_NEGRITO"]}Jogador da vez: {jogador2.upper()}{e.estilos["RESET"]}'

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

#Funções para dinamizar o uso da cor -  CorEPeca() retorna o nome de uma peça da cor atual - inverteCor() inverte a cor atual - listaDePecas() retorna a lista de todas as pecas da cor atual
def corEpeca(cor,nome):
  if cor=='preta':
    return 'p_'+nome
  elif cor=='branca':
    return 'b_'+nome

def inverteCor(cor):
  if cor=='branca':
    cor='preta'
  else:
    cor='branca'
  return cor

def listaDePecas(cor):
  if cor=='preta':
    return ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre', 'p_peao']
  elif cor=='branca':
    return ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre', 'b_peao']

#Funções que verificam se peças ao redor ameaçam ou não uma determinada posição
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

def verificacaoHorizontalEVertical(tabuleiro, linha, coluna, proximaLinha, proximaColuna, limiteLinha, limiteColuna,cor):
  while True:
    coluna+=proximaColuna
    linha+=proximaLinha

    if coluna == limiteColuna or  linha == limiteLinha:
      break
    peca = tabuleiro[linha][coluna]
    if peca in listaDePecas(cor) and peca!= corEpeca(cor,'rei'):
      return False
    if peca in listaDePecas(inverteCor(cor)) and peca not in [corEpeca(inverteCor(cor),'torre'),corEpeca(inverteCor(cor),'rainha')]:
      return False
    if peca in listaDePecas(inverteCor(cor)) and peca in [corEpeca(inverteCor(cor),'torre'),corEpeca(inverteCor(cor),'rainha')]:
      return True 
    

def verificacaoDiagonal(tabuleiro, contLinha, contColuna, proximaLinha, proximaColuna, limiteLinha, limiteColuna,cor):
  while True:
    contLinha += proximaLinha
    contColuna += proximaColuna

    if contColuna == limiteColuna or contLinha == limiteLinha:
        break
    peca = tabuleiro[contLinha][contColuna]
    if (peca in listaDePecas(cor) and peca != corEpeca(cor,'rei')):
        return False
    if (peca in listaDePecas(inverteCor(cor)) and peca not in [corEpeca(inverteCor(cor),'bispo'),corEpeca(inverteCor(cor),'rainha')]):
       return False
    if peca in listaDePecas(inverteCor(cor)) and peca in [corEpeca(inverteCor(cor),'bispo'),corEpeca(inverteCor(cor),'rainha')]:  
        return True


def localizarRei(tabuleiro, cor):
  for i in range(8):
    for j in range(8):
      if tabuleiro[i][j] == corEpeca(cor,'rei'):
        return [i, j]

def valorOrigem (coluna,linha):
  return '%s%s' %(letras[coluna],linha+1)


def chequeReiparaRei (tabuleiro,cor):
    possibilideReiAtual=m.reiPossibilidades(tabuleiro,valorOrigem(localizarRei(tabuleiro, cor)[1],localizarRei(tabuleiro, cor)[0]),cor)
    possibilideReiInimgo= m.reiPossibilidades(tabuleiro,valorOrigem(localizarRei(tabuleiro, inverteCor(cor))[1],localizarRei(tabuleiro, inverteCor(cor))[0]),inverteCor(cor))
    interseccao = []
    for possibilidades_a in possibilideReiAtual:
      for possibilidades_b in possibilideReiInimgo:
        if possibilidades_a == possibilidades_b:
          interseccao.append(possibilidades_a)
    return interseccao




    







