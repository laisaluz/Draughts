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
    


class Peca:

    ehDama = False
    possuiCaptura = False
    movimentosPossiveis = []

    def __init__(self, y, x, orientacao):
        
        '''Função responsável por definir e atribuir os valores iniciais dos atributos do objeto "Peca" '''
        
        self.x = x
        self.y = y
        self.orientacao = orientacao # -1 para pecas de baixo, 1 para pecas de cima e 0 para casas vazias  

    def movimentos_possiveis(self, tabuleiro):
        
        '''Função responsável por calcular os movimentos possíveis para uma determinada peça em um tabuleiro de damas. 
        Ela recebe o tabuleiro como parâmetro e atualiza o atributo movimentosPossiveis da peça com uma lista contendo 
        as coordenadas dos movimentos válidos'''
        
        self.movimentosPossiveis = []
        self.possuiCaptura = False
        if self.orientacao == 0:
            return
        
        #No caso em que a peça é uma dama : 
        #Percorre múltiplas posições na mesma direção até encontrar uma peça oponente, sem que tenha uma peça do mesmo tipo bloqueando o caminho 

        if not self.ehDama:
            
            direcoes = [[1,1], [1,-1], [-1,1], [-1,-1]]
            for direcao in direcoes:
                
                i = self.y + direcao[0]
                j = self.x + direcao[1]
                if 0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro):
                    podeCapturar = tabuleiro[i][j].orientacao == -self.orientacao
                    i += direcao[0]
                    j += direcao[1]
                
                    if podeCapturar and 0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro) and tabuleiro[i][j].orientacao == 0:
                        
                        self.movimentosPossiveis += [[i,j]]
                        self.possuiCaptura = True
                        possuiCapturasDisponiveis[self.orientacao] = True

            if(not self.possuiCaptura and not possuiCapturasDisponiveis[self.orientacao]):
                
                for direcao in direcoes:
                    if direcao[0] == self.orientacao:
                        i = self.y + direcao[0]
                        j = self.x + direcao[1]
                        if 0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro) and tabuleiro[i][j].orientacao == 0:
                            
                            self.movimentosPossiveis += [[i,j]]

                
        #No caso em que a peça não é uma dama : 
        #Percorre os movimentos nas diagonais (cima-direita, cima-esquerda, baixo-direita, baixo-esquerda).
        #Verifica se é possível capturar uma peça do oponente .
        #Se for possível e a próxima posição após a peça estiver vazia, esse movimento é adicionado à lista de movimentosPossiveis.
        #Caso não haja nenhuma captura possível, a função verifica os movimentos diagonais .

        else:
            
            direcoes = [[1,1], [1,-1], [-1,1], [-1,-1]]
            for direcao in direcoes:

                i = self.y + direcao[0]
                j = self.x + direcao[1]
                while(0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro)):
                    podeCapturar = tabuleiro[i][j].orientacao == -self.orientacao
                    i += direcao[0]
                    j += direcao[1]

                    if podeCapturar and 0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro):
                        while(0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro)):

                            if tabuleiro[i][j].orientacao == 0:
                                self.movimentosPossiveis += [[i,j]]
                            else:
                                break

                            i += direcao[0]
                            j += direcao[1]

                            self.possuiCaptura = True
                            possuiCapturasDisponiveis[self.orientacao] = True

                            #No final da função, o atributo possuiCaptura da peça é atualizado para indicar se a peça atual possui alguma captura possível. 
                            #Além disso, a função atualiza o dicionário possuiCapturasDisponiveis para refletir se há capturas disponíveis para o jogador atual.

                    if self.possuiCaptura:
                        break

            if(not self.possuiCaptura and not possuiCapturasDisponiveis[self.orientacao]):
                for direcao in direcoes:
                        i = self.y + direcao[0]
                        j = self.x + direcao[1]
                        while(0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro) and tabuleiro[i][j].orientacao == 0):
                            self.movimentosPossiveis += [[i,j]]
                            i += direcao[0]
                            j += direcao[1]

    def movimentar_peca(self, movimento, tabuleiro, indice): 

        '''Executa o movimento válido de uma peça no tabuleiro, atualiza o estado do dele e verifica se houve captura de peças durante o movimento.'''
        
        if movimento in self.movimentosPossiveis:
            
            y_range = range( self.y, movimento[0], sinal(movimento[0] - self.y))
            x_range = range( self.x, movimento[1], sinal(movimento[1] - self.x))

            #Como o movimento é diagonal, então len(y_range) = len(x_range)
            
            capturouPeca = False
            for k in range(len(y_range)):
                i = y_range[k]
                j = x_range[k]
                if(tabuleiro[i][j].orientacao == -self.orientacao):
                    pontuacaoJogadores[self.orientacao] += 1
                    capturouPeca = True
                    
                tabuleiro[i][ j] = Peca(i, j, 0)

            tabuleiro[movimento[0]][movimento[1]] = self
            self.y = movimento[0]
            self.x = movimento[1]
            
            self.virar_dama()

            return capturouPeca #Se capturou uma peca, deve jogar novamente
        
        else:
            print("Jogada invalida na linha" + str(indice))
            return True #Movimento inválido

    def virar_dama(self):

        '''Verifica se uma peça alcançou a última linha do tabuleiro adversário e, se sim, transforma essa peça em uma dama, atualizando seu tipo. '''

        if(self.orientacao == -1 and self.y == 0):
            self.ehDama = True

        if(self.orientacao == 1 and self.y == 9):
            self.ehDama = True

        return

    def __str__(self):

        '''Ao definir o método __str__ na classe Peca, podemos controlar como um objeto dessa classe (o/@,#, ) é representado como uma string.'''

        if(self.orientacao == 1):
            if(self.ehDama):
                return 'O'
            else:
                return 'o'
            
        elif(self.orientacao == -1):
            if(self.ehDama):
                return '&'
            else:
                return '@'

        else:
            if((self.x + self.y)%2):
                return ' '
            else:
                return '#'

class GerenciadorJogo:

    '''A classe GerenciadorJogo é responsável por gerenciar todo o fluxo do jogo de damas, 
    desde a inicialização até o controle dos turnos e das condições de vitória.'''

    orientacao = 0

    def __init__(self) -> None:

        self.jogadas = self.lerJogadas()
        self.indice = 1
        self.escolherOrientacaoInicial()
        self.tabuleiro = self.iniciarTabuleiro()
        

    
    
    def lerJogadas(self):

        nome_arquivo = sys.argv[1]

        with open(nome_arquivo, 'r') as arquivo:
            jogadas = arquivo.readlines()

        print(jogadas)
        return jogadas


# Escolhendo se o usuário irá começar com as peças de cima ou com as peças de baixo :

    def escolherOrientacaoInicial(self):  #Lê a primeira linha para indicar quem começa o jogo 
        orientacaoInicial = self.jogadas[0]

        if orientacaoInicial == 'C':
            self.orientacao = 1
        else:
            self.orientacao = -1

# Iniciando o tabuleiro :

    def iniciarTabuleiro(self):
        #Tabuleiro oficial das damas
        tabuleiro = [[Peca(y,x,0) for x in range(10)] for y in range(10)]
        for i in range(10):
            for j in range(10):
                if((i+j)%2 and i < 3):
                    tabuleiro[i][j] = Peca(i,j,1)
                elif ((i+j)%2 and i > 6):
                    tabuleiro[i][j] = Peca(i,j,-1)
        return tabuleiro

# Construindo o tabuleiro conforme o formato especificado :

    def estaDentroDoTabuleiro(self, pos):
        return 0 <= pos[0] and pos[0] < len(self.tabuleiro) and 0 <= pos[1] and pos[1] < len(self.tabuleiro)
    
    def escreverTabuleiro(self):
        letras = 'ABCDEFGHIJ'
        linhaEntreCasas = '  +-+-+-+-+-+-+-+-+-+-+'
        print("   ",end="")
        for l in letras:
            print(l, end=" ")

        print(" ")
        for i in range(len(self.tabuleiro)):
            print(linhaEntreCasas)
            print(str(i), end=' |')
            for j in range(len(self.tabuleiro)):
                print(self.tabuleiro[i][j],end='|')
            print(i)

        print(linhaEntreCasas)
        print("   ",end="")
        for l in letras:
            print(l, end=" ")
        
        print(" ")

# Recebendo um movimento do usuário e mudando a posição da peça escolhida :

    def jogarTurno(self):
        inputUsuario = self.jogadas[self.indice]
        self.indice += 1
        

        posInicial = [int(inputUsuario[1]),ord(inputUsuario[0])-65]
        posFinal = [int(inputUsuario[5]),ord(inputUsuario[4])-65]

        if not self.estaDentroDoTabuleiro(posInicial) or not self.estaDentroDoTabuleiro(posFinal):
            print("Jogada invalida na linha " + str(self.indice))
            return True
        
        peca: Peca = self.tabuleiro[posInicial[0]] [posInicial[1]]

        if peca.orientacao != self.orientacao:
            print("Jogada invalida na linha " + str(self.indice))
            return True
        
        peca.movimentos_possiveis(self.tabuleiro) 


        
        
        #Reconferir os movimentos possiveis da peca, pois é possivel que seja adicionados movimentos invalidos em IniciarTurno(self, tabuleiro) 
        #pois nem todas as pecas podem ter sido verificadas antes de se adicionar os movimentos

        return peca.movimentar_peca(posFinal, self.tabuleiro, self.indice) #retorna se deve jogar novamente ou não


    def iniciarJogo(self):
        
        '''Função responsável por executar o loop principal do jogo de damas. 
        Ela exibe o tabuleiro, verifica os movimentos possíveis para cada peça, determina se houve capturas disponíveis,
        verifica as condições de vitória e permite que os jogadores façam seus movimentos.'''
        
        while len(self.jogadas) > self.indice:

            possuiCapturasDisponiveis[-1] = False
            possuiCapturasDisponiveis[1] = False

            somaMovimentosCima = 0
            somaMovimentosBaixo = 0

            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro)):
                    peca:Peca = self.tabuleiro[i][j]
                    peca.movimentos_possiveis(self.tabuleiro)
                    
                    if peca.orientacao == -1:
                        somaMovimentosCima += len(peca.movimentosPossiveis) > 0

                    if peca.orientacao == 1:
                        somaMovimentosBaixo += len(peca.movimentosPossiveis) > 0

            #Condição de vitória das peças de baixo e das peças de cima :

            if somaMovimentosBaixo == 0:
                print("Peças de Cima ganharam!")
                break
            
            if somaMovimentosCima == 0:
                print("Peças de Baixo ganharam!")
                break
        
            if(not self.jogarTurno()):
                self.orientacao = -self.orientacao

        self.escreverTabuleiro()  # Mostra a situação final do tabuleiro
        print("O Placar é : Peças de Cima", pontuacaoJogadores[1],"vs Peças de Baixo", pontuacaoJogadores[-1])

    

    def gameLoop(self):

        '''Função responsável por executar o loop principal do jogo em si, coordenando a interação entre os jogadores 
        e atualizando o estado do jogo até que ocorra uma condição de término. Essa função é chamada dentro do método iniciarJogo(self) 
        e é onde o jogo realmente acontece.'''

        self.iniciarJogo()

