'''
GRUPO :
LAISA CAROLINE DA COSTA LUZ - 552531
MARIA LUIZA FELIPE CAROLINO - 552655
LUIZA ESTHER MARTINS PESSOA - 555516
'''

# Inicialmente, definimos as chaves -1 para as peças de cima, 0 para as casas vazias e 1 para as peças de baixo :

# Definimos um dicionário que indica se há tem capturas disponíveis :

possuiCapturasDisponiveis = {
                            -1: False, #-1 para pecas de cima
                            0: False, #0 para casas vazias
                            1: False, # 1 para pecas de baixo
                            } 

# Além disso, estabelecemos a pontuação inicial (0) de cada jogador :

pontuacaoJogadores = {
    -1: 0,
    1: 0,
}


def sinal(x):
    
    '''De acordo com a orientação, definimos que as peças de cima tem sinal -1, as casas vazias 0 e as peças de baixo 1 para definir o sentido de movimento em algumas operações, como
    no cálculo de coordenadas durante a execução de movimentos de peças'''
    
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# A classe Peca representa uma peça no jogo de damas, ela possui atributos e métodos que são utilizados para controlar o estado e o comportamento das peças durante o jogo :

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


    def movimentar_peca(self, movimento, tabuleiro): 

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
                    print("O novo placar é : Peças de Cima",pontuacaoJogadores[1],"vs Peças de Baixo",pontuacaoJogadores[-1])
                    capturouPeca = True
                    
                tabuleiro[i][ j] = Peca(i, j, 0)

            tabuleiro[movimento[0]][movimento[1]] = self
            self.y = movimento[0]
            self.x = movimento[1]
            
            self.virar_dama()

            return capturouPeca #Se capturou uma peca, deve jogar novamente
        
        else:
            print("Jogada inválida!")
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

        self.escolherOrientacaoInicial()
        self.tabuleiro = self.iniciarTabuleiro()

    def escolherOrientacaoInicial(self):

      '''Escolhendo se o usuário irá começar com as peças de cima ou com as peças de baixo'''
      
        orientacaoInicial = input("Insira qual lado deve começar, C para as peças de cima ou B para as peças de baixo : ")
        while orientacaoInicial != "B" and orientacaoInicial != "C":
            orientacaoInicial = input("Opção inválida, por favor escolha C para as peças de cima ou B para as peças de baixo : ")

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
        
        '''Tabuleiro de testes utilizado durante o jogo de damas para verificar comportamento das peças : 
        
        tabuleiro = [[Peca(y,x,0) for x in range(10)] for y in range(10)]
        tabuleiro[6][3] = Peca(6,3, -1)
        tabuleiro[5][2] = Peca(5,2, 1)
        #tabuleiro[3][2] = Peca(3,2,1)
        tabuleiro[6][5] = Peca(6,5,1)'''
        
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
        inputUsuario = input("Insira um movimento: ")

        posInicial = [int(inputUsuario[1]),ord(inputUsuario[0])-65]
        posFinal = [int(inputUsuario[5]),ord(inputUsuario[4])-65]

        if not self.estaDentroDoTabuleiro(posInicial):
            print("Posição da peça fora do tabuleiro")
            return True
        
        if not self.estaDentroDoTabuleiro(posFinal):
            print("Movimento indo para fora do tabuleiro")
            return True
        
        peca: Peca = self.tabuleiro[posInicial[0]] [posInicial[1]]

        if peca.orientacao != self.orientacao:
            print("Peça invalida, escolha outro movimento")
            return True
        
        peca.movimentos_possiveis(self.tabuleiro) 

        return peca.movimentar_peca(posFinal, self.tabuleiro) #retorna se deve jogar novamente ou não


    def iniciarJogo(self):

        '''Função responsável por executar o loop principal do jogo de damas. 
        Ela exibe o tabuleiro, verifica os movimentos possíveis para cada peça, determina se houve capturas disponíveis,
        verifica as condições de vitória e permite que os jogadores façam seus movimentos.'''
        
        while True:

            self.escreverTabuleiro()
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
                return
            
            if somaMovimentosCima == 0:
                print("Peças de Baixo ganharam!")
                return
        
            print("Turno das peças de " + (self.orientacao==1)*"Cima" + (self.orientacao==-1)*"Baixo")
            if(not self.jogarTurno()):
                self.orientacao = -self.orientacao


    def gameLoop(self):

        '''Função responsável por executar o loop principal do jogo em si, coordenando a interação entre os jogadores 
        e atualizando o estado do jogo até que ocorra uma condição de término. Essa função é chamada dentro do método iniciarJogo(self) 
        e é onde o jogo realmente acontece.'''

        self.iniciarJogo()
        recomecar = input("Deseja recomeçar?")
        if(recomecar == "S"):
            self.escolherOrientacaoInicial()
            self.tabuleiro = self.iniciarTabuleiro()
            self.iniciarJogo()
            return
        else:
            print("Até a próxima")


#def Damas():

    '''A função Damas() é responsável por iniciar o jogo de damas e gerenciar o fluxo do jogo. 
    Ela cria uma instância do objeto GerenciadorJogo, que é a classe responsável por controlar todo o jogo, 
    desde a inicialização até as condições de vitória.'''

    #gerenciador = GerenciadorJogo()
    #gerenciador.gameLoop()

#Damas()

        
