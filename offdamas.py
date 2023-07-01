import sys
# Inicialmente, definimos que não existem capturas disponíveis para nenhum tipo de peça :
possuiCapturasDisponiveis = {
                            -1: False, #-1 para pecas de cima
                            0: False, #0 para casas vazias
                            1: False, # 1 para pecas de baixo
                            } 

# Além disso, definimos a pontuação inicial (0) de cada jogador :
pontuacaoJogadores = {
    -1: 0,
    1: 0,
}

def sinal(x):
    
    '''De acordo com a orientação, definimos que as peças de cima tem sinal -1, as casas vazias 0 e as peças de baixo 1'''
    
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
    

    #Por isto aqui embaixo dentro de gerenciador jogo




def ler_jogadas():

    nome_arquivo = sys.argv[1]

    with open(nome_arquivo, 'r') as arquivo:
        jogadas = arquivo.readlines()

    return jogadas


class GerenciadorJogo():
    def __init__(self) -> None:
        self.jogadas = ler_jogadas()

    def gameLoop(self):
        for i in range(len(self.jogadas)):
            print(self.jogadas[i])


    def jogada_valida(self):
        self.jogadas
        '''Lógica de validação de uma jogada
        Retorna True se for válida e False caso contrário'''

        return True

    def executar_jogada(self,tabuleiro):
        self.jogadas

        '''Função responsável por processar a jogada 
        do usuário e modificar o tabuleiro '''


        


