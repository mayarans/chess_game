import estilos

# Dicionário de peças utilizadas para montar o tabuleiro de xadrez
pecas = {
    'p_quadrado': u'\u25FC',
    'p_peao': u'\u265F',
    'p_torre': u'\u265C',
    'p_cavalo': u'\u265E',
    'p_bispo': u'\u265D',
    'p_rei': u'\u265A',
    'p_rainha': u'\u265B',
    'b_quadrado': u'\u25FB',
    'b_peao': u'\u2659',
    'b_torre': u'\u2656',
    'b_cavalo': u'\u2658',
    'b_bispo': u'\u2657',
    'b_rei': u'\u2654',
    'b_rainha': u'\u2655'

}

# Função para montagem do tabuleiro de xadrez
def montarTabuleiro():
  # Listas utilizadas para compor o tabuleiro
  pecasPretas = ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre']
  pecasBrancas = ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre']
  tabuleiro = []
  tabuleiro.append(pecasPretas)
  tabuleiro.append(['p_peao']*8)
  for i in range(2, 6):
    linha = []
    tabuleiro.append(linha)
    if i%2 == 0:
      tabuleiro[i].extend(['b_quadrado', 'p_quadrado']*4)
    elif i%2 != 0:
      tabuleiro[i].extend(['p_quadrado', 'b_quadrado']*4)
  tabuleiro.append(['b_peao']*8)
  tabuleiro.append(pecasBrancas)

  return tabuleiro

# Função para printar o tabuleiro no terminal
def mostrarTabuleiro(tabuleiro, letras,possibilidades=[]):
  print()
  # Colunas
  print('  ','  '.join(letras))
  for i in range(len(tabuleiro)):
    # Número de linhas
    print(i+1, end=" ")
    for j in range(len(tabuleiro[i])):
      # Adicionando estilos para o tabuleiro
      print(estilos.estilos['FUNDO_VERDE' if [i,j] in possibilidades else 'FUNDO_BRANCO'], end='')
      print(estilos.estilos['PRETO'], end ='')
      print('',pecas[tabuleiro[i][j]], end=" ")
      print(estilos.estilos['REDEFINIR'] + estilos.estilos['REDEFINIR'], end='')
    print()
  print()

