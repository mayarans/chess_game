import movimentos as m
import funcs_auxiliares as f
import tabuleiro as t
import estilos as e
import xeque as x

# Chamada de função para limpar a tela
f.limparTela()

# Chamando a função de carregamento do jogo
f.carregamentoJogo()

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
1. {e.estilos["MAGENTA_NEGRITO"]}Cada jogador realizará apenas um movimento por vez;{e.estilos["REDEFINIR"]}
2. {e.estilos["MAGENTA_NEGRITO"]}O jogador com as peças brancas sempre move primeiro;{e.estilos["REDEFINIR"]}
3. {e.estilos["MAGENTA_NEGRITO"]}Indique a posição de origem e de destino da peça que deseja mover. Para isso, informe a coluna (identificada pelas letras de A a H) e a linha (que vai de 1 a 8) onde a peça que você deseja mover está localizada;{e.estilos["REDEFINIR"]}
4. {e.estilos["MAGENTA_NEGRITO"]}Para escolher um novo movimento digite '-1';{e.estilos["REDEFINIR"]}
5. {e.estilos["MAGENTA_NEGRITO"]}A partida termina quando ocorrer xeque-mate;{e.estilos["REDEFINIR"]}
6. {e.estilos["MAGENTA_NEGRITO"]}Divirta-se! 😜{e.estilos["REDEFINIR"]}\n''')

# A montagem do tabuleiro retorna a matriz que será armazenada na variável "tabuleiro"
tabuleiro = t.montarTabuleiro()
# Letras de identificação das colunas
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Recebendo informações dos jogadores
jogador1 = input('Nome do jogador 1 (peças brancas): ')
jogador2 = input('Nome do jogador 2 (peças pretas): ')

cor = 'branca'
while True:
  # Chamada de função para limpar a tela
  f.limparTela()
  escolherOutraOrigem = False
  # Chamada de função para print do tabuleiro
  t.mostrarTabuleiro(tabuleiro, letras)
  while True:
    # Recebendo a origem da jogada do usuário
    print(f'{e.estilos["CIANO_NEGRITO"]}Jogador da vez: {f.jogadorDaVez(cor,jogador1,jogador2).upper()}{e.estilos["REDEFINIR"]}')
    origemJogada = input('Origem (ex.: e5): ').lower()
    # Chamando a função para verificar se a origem é válida
    verificacao = f.verificarOrigemValida(tabuleiro, origemJogada, cor)
    if verificacao == 'ok':
      # Chamando a função que verifica a possibilidade de movimentar a peça
      possibilidades = m.possibilidades(tabuleiro, origemJogada, cor)
      if possibilidades == []:
        print(f'\n{e.estilos["VERMELHO"]}Não é possível mover esta peça no momento. Tente novamente!{e.estilos["REDEFINIR"]}\n')
        continue
      else:
        break
    print(verificacao)

  # Chamada de função para print do tabuleiro
  t.mostrarTabuleiro(tabuleiro, letras, possibilidades)
  while True:
    # Recebendo o destino da jogada do usuário
    destinoJogada = input('Destino (ex.: e5): ').lower()
    if destinoJogada == "-1":
      escolherOutraOrigem = True
      break
    # Chamando a função para verificar se o destino é válido
    verificacao = m.verificarDestinoValido(destinoJogada, possibilidades)
    if not verificacao:
      print(f'\n{e.estilos["VERMELHO"]}Este não é um movimento válido para esta peça. Tente novamente!{e.estilos["REDEFINIR"]}\n')
      continue
    elif not m.reiForaDeXeque(tabuleiro.copy(),cor,origemJogada,destinoJogada):
      print(f'\n{e.estilos["VERMELHO"]}Este movimento não retira o seu Rei de xeque. Tente novamente!{e.estilos["REDEFINIR"]}\n')
      continue
    break
  if escolherOutraOrigem:
    continue
  # Chamando a função que define o movimento a ser feito
  m.realizarMovimento(tabuleiro, origemJogada, destinoJogada)
  
  # Alternando o jogador
  if cor == 'branca':
    cor = 'preta'
  else:
    cor = 'branca'
  # Chamada de função para o xeque-mate e término do loop
  if x.xequeMate(tabuleiro, cor):
    t.mostrarTabuleiro(tabuleiro, letras)
    print(f'{e.estilos["VERMELHO"]}XEQUE-MATE!{e.estilos["REDEFINIR"]}\n{e.estilos["VERDE"]}{f.jogadorDaVez(jogador1, jogador2)} VENCEU A PARTIDA{e.estilos["REDEFINIR"]}')
    break
    
    
  
 
