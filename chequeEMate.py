import funcs_auxiliares as f


# Variáveis utilizadas em todas as funções de movimento
quadrados = ['p_quadrado', 'b_quadrado']
pecasPretas = ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre', 'p_peao']
pecasBrancas = ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre', 'b_peao']


def cheque(tabuleiro,posicao,cor):
    linha = f.linha(posicao)
    coluna = f.coluna(posicao)
    resultado = False
    contLinha= linha
    contColuna= coluna
    if cor == 'branca':
    #CASAS DIAGONAIS
    #Casas superiores direita
        while True:
            if contColuna>= 7 or contLinha<=0:
                break
            else:
                if tabuleiro[contLinha][contColuna] in pecasBrancas and not 'b_rei':
                    break
                if tabuleiro[contLinha][contColuna] in pecasPretas and (tabuleiro[contLinha][contColuna]=='p_bispo' or tabuleiro[contLinha][contColuna] == 'p_rainha'):
                    resultado=True
                
                contLinha-=1
                contColuna+=1
        contLinha= linha
        contColuna= coluna
        
    return resultado

