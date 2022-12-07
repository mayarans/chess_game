import movimentos as m
import funcs_auxiliares as f
import tabuleiro as t
import estilos as e

# Chamando a função de carregamento do jogo
f.loading()

# Print do nome do jogo e de suas instruções
print('''
██╗  ██╗ █████╗ ██████╗ ██████╗ ███████╗███████╗    
╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══███╔╝    
 ╚███╔╝ ███████║██║  ██║██████╔╝█████╗    ███╔╝     
 ██╔██╗ ██╔══██║██║  ██║██╔══██╗██╔══╝   ███╔╝      
██╔╝ ██╗██║  ██║██████╔╝██║  ██║███████╗███████╗    
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝    
                                                    ''')
print(f'''INSTRUÇÕES:\n
1. {e.estilos["MAGENTA_NEGRITO"]}Cada jogador realizará apenas um movimento por vez;{e.estilos["RESET"]}
2. {e.estilos["MAGENTA_NEGRITO"]}O jogador com as peças brancas sempre move primeiro;{e.estilos["RESET"]}
3. {e.estilos["MAGENTA_NEGRITO"]}Indique a posição de origem e de destino da peça que deseja mover. Para isso, informe a coluna (identificada pelas letras de A a H) e a linha (que vai de 1 a 8) onde a peça que você deseja mover está localizada;{e.estilos["RESET"]}
4. {e.estilos["MAGENTA_NEGRITO"]}A partida termina quando ocorrer xeque-mate;{e.estilos["RESET"]}
5. {e.estilos["MAGENTA_NEGRITO"]}Divirta-se! 😜{e.estilos["RESET"]}\n''')

# A montagem do tabuleiro retorna a matriz que será armazenada na variável "tabuleiro"
tabuleiro = t.montarTabuleiro()
# Letras de identificação das colunas
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Recebendo informações dos jogadores
jogador1 = input('Nome do jogador 1 (peças brancas): ')
jogador2 = input('Nome do jogador 2 (peças pretas): ')

# Condição de parada do jogo
aindaJogando = True
cor = 'branca'
while True:
  # Chamada de função para print do tabuleiro
  t.mostrarTabuleiro(tabuleiro, letras)
  if not aindaJogando:
    break
  while True:
    # Recebendo a origem da jogada do usuário
    origemJogada = input('Origem (ex.: e5): ')
    # Chamando a função para verificar se a origem é válida
    verificacao = f.verificarOrigemValida(tabuleiro, origemJogada, cor)
    if verificacao == 'ok':
      # Chamando a função que verifica a possibilidade de movimentar a peça
      possibilidades = m.possibilidades(tabuleiro, origemJogada, cor)
      if possibilidades == []:
        print('Não é possível mover esta peça no momento. Tente novamente!')
        continue
      else:
        print(possibilidades)
        break
    print(verificacao)

  # Chamada de função para print do tabuleiro
  t.mostrarTabuleiro(tabuleiro, letras)
  while True:
    # Recebendo o destino da jogada do usuário
    destinoJogada = input('Destino (ex.: e5): ')
    # Chamando a função para verificar se o destino é válido
    verificacao = m.verificarDestinoValido(destinoJogada, possibilidades)
    if verificacao == True:
      break
    else:
      print('Este não é um movimento válido para esta peça. Tente novamente!')
      continue
  # Chamando a função que define o movimento a ser feito
  m.realizarMovimento(tabuleiro, origemJogada, destinoJogada)
  # Alternando o jogador
  if cor == 'branca':
    cor = 'preta'
  else:
    cor = 'branca'
