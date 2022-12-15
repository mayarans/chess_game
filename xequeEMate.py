import funcs_auxiliares as f


# Variáveis utilizadas em todas as funções de movimento
quadrados = ['p_quadrado', 'b_quadrado']
pecasPretas = ['p_torre', 'p_cavalo', 'p_bispo', 'p_rainha', 'p_rei', 'p_bispo', 'p_cavalo', 'p_torre', 'p_peao']
pecasBrancas = ['b_torre', 'b_cavalo', 'b_bispo', 'b_rainha', 'b_rei', 'b_bispo', 'b_cavalo', 'b_torre', 'b_peao']


def xeque(tabuleiro,posicao,cor):
    linha = f.linha(posicao)
    coluna = f.coluna(posicao)
    resultado = False
    contLinha= linha
    contColuna= coluna
    if cor == 'branca':
        #CASAS DIAGONAIS (Para verificar se está ameaçado por bispos, rainha ou peões)
        #Casas superiores direita (bispo rainha e peão)  
        while True:
            if contColuna>= 7 or contLinha<=0:
                break
            else:
                #Verificação se há um peão na diagonal imediata antes de verificar as demais casas
                if not tabuleiro[linha+1][coluna+1]=='p_peao': 
                    if tabuleiro[contLinha][contColuna] in pecasBrancas and not 'b_rei' or (tabuleiro[contLinha][contColuna] in pecasPretas and tabuleiro[contLinha][contColuna]!= 'p_bispo' and tabuleiro[contLinha][contColuna]!='p_rainha'):
                        break
                    if tabuleiro[contLinha][contColuna] in pecasPretas and (tabuleiro[contLinha][contColuna]=='p_bispo' or tabuleiro[contLinha][contColuna] == 'p_rainha'):
                        resultado=True
                else:
                    resultado=True  
                contLinha-=1
                contColuna+=1
        contLinha= linha
        contColuna= coluna
        #Casas superiores esquerda (bispo, rainha e peão)
        while True:
            if contColuna<= 0 or contLinha<=0:
                break
            else:
                #Verificação se há um peão na diagonal imediata antes de verificar as demais casas
                if not tabuleiro[linha-1][coluna-1]=='p_peao': 
                    if tabuleiro[contLinha][contColuna] in pecasBrancas and not 'b_rei' or (tabuleiro[contLinha][contColuna] in pecasPretas and tabuleiro[contLinha][contColuna]!= 'p_bispo' and tabuleiro[contLinha][contColuna]!='p_rainha'):
                        break
                    if tabuleiro[contLinha][contColuna] in pecasPretas and (tabuleiro[contLinha][contColuna]=='p_bispo' or tabuleiro[contLinha][contColuna] == 'p_rainha'):
                        resultado=True
                else:
                    resultado=True  
                contLinha-=1
                contColuna+=1
        contLinha= linha
        contColuna= coluna
        #Casas inferior direita (Bispo e rainha)
        while True:
            if contColuna >=7 or contLinha>=7:
                break
            else:
                if tabuleiro[contLinha][contColuna] in pecasBrancas and not 'b_rei' or (tabuleiro[contLinha][contColuna] in pecasPretas and tabuleiro[contLinha][contColuna]!= 'p_bispo' and tabuleiro[contLinha][contColuna]!='p_rainha'):
                    break
                if tabuleiro[contLinha][contColuna] in pecasPretas and (tabuleiro[contLinha][contColuna]=='p_bispo' or tabuleiro[contLinha][contColuna] == 'p_rainha'):
                    resultado=True
                
                contLinha+=1
                contColuna+=1
        contLinha= linha
        contColuna= coluna
        #Casas inferior esquerda (Bispo e rainha)
        while True:
            if contColuna <=0 or contLinha>=7:
                break
            else:
                if tabuleiro[contLinha][contColuna] in pecasBrancas and not 'b_rei' or (tabuleiro[contLinha][contColuna] in pecasPretas and tabuleiro[contLinha][contColuna]!= 'p_bispo' and tabuleiro[contLinha][contColuna]!='p_rainha'):
                    break
                if tabuleiro[contLinha][contColuna] in pecasPretas and (tabuleiro[contLinha][contColuna]=='p_bispo' or tabuleiro[contLinha][contColuna] == 'p_rainha'):
                    resultado=True
                
                contLinha+=1
                contColuna-=1
        contLinha= linha
        contColuna= coluna
        #VERIFICAÇÃO DAS CASAS EM "L" (Movimento do cavalo)
        #para cima
        if linha > 1:
            if coluna < 7:
                if  tabuleiro[linha - 2][coluna + 1]== 'p_cavalo':
                    resultado = True
            if coluna > 0:
                if tabuleiro[linha - 2][coluna - 1] == 'p_cavalo':
                    resultado = True
        #para baixo
        if linha < 6:
            if coluna < 7:
                if  tabuleiro[linha + 2][coluna + 1]== 'p_cavalo':
                    resultado = True
            if coluna > 0:
                if tabuleiro[linha + 2][coluna - 1] == 'p_cavalo':
                    resultado = True
        #para direita
        if linha < 6:
            if coluna < 7:
                if  tabuleiro[linha + 1][coluna + 2]== 'p_cavalo':
                    resultado = True
            if coluna > 0:
                if tabuleiro[linha - 1][coluna + 2] == 'p_cavalo':
                    resultado = True
        #para esquerda
        if linha > 1:
            if coluna > 0:
                if  tabuleiro[linha + 1][coluna - 2]== 'p_cavalo':
                    resultado = True
            if coluna > 0:
                if tabuleiro[linha - 1][coluna - 2] == 'p_cavalo':
                    resultado = True
        #VERIFICAÇÃO DAS CASAS HORIZINTAIS (Movimento da torre e da rainha)
        #Para cima
        if linha > 0:
            for i in range(linha, 0, -1):
                if tabuleiro[i][coluna] in pecasBrancas and not 'b_rei':
                    break
                elif tabuleiro[i][coluna] in pecasPretas and not 'p_torre' and not 'p_rainha':
                    break
                elif tabuleiro[i][coluna] == 'p_torre' or tabuleiro[i][coluna] == 'p_rainha':
                    resultado = True
        #Para baixo
        if linha < 7:
            for i in range(linha, 8):
                if tabuleiro[i][coluna] in pecasBrancas and not 'b_rei':
                    break
                elif tabuleiro[i][coluna] in pecasPretas and not 'p_torre' and not 'p_rainha':
                    break
                elif tabuleiro[i][coluna] == 'p_torre' or tabuleiro[i][coluna] == 'p_rainha':
                    resultado = True
        #Para direita
        if coluna < 7:
            for i in range(coluna, 8):
                if tabuleiro[i][linha] in pecasBrancas and not 'b_rei':
                    break
                elif tabuleiro[i][linha] in pecasPretas and not 'p_torre' and not 'p_rainha':
                    break
                elif tabuleiro[i][linha] == 'p_torre' or tabuleiro[i][linha] == 'p_rainha':
                    resultado = True
        #Para esquerda
        if coluna > 0:
            for i in range(coluna,0,-1):
                if tabuleiro[i][linha] in pecasBrancas and not 'b_rei':
                    break
                elif tabuleiro[i][linha] in pecasPretas and not 'p_torre' and not 'p_rainha':
                    break
                elif tabuleiro[i][linha] == 'p_torre' or tabuleiro[i][linha] == 'p_rainha':
                    resultado = True
    return resultado

