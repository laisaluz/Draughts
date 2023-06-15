#Variaveis Globais
possuiCapturasDisponiveis = {
                            -1: False, #-1 para pecas de cima
                            0: False, #0 para casas vazias
                            1: False, # 1 para pecas de baixo
                            } 

pontuacaoJogadores = {
    -1: 0,
    1: 0,
}


#Funcoes auxiliares
def sinal(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

#Classes
class Peca:

    ehDama = False
    possuiCaptura = False
    movimentosPossiveis = []


    def __init__(self, y, x, orientacao):
        self.x = x
        self.y = y
        self.orientacao = orientacao # -1 para pecas de baixo, 1 para pecas de cima e 0 para casas vazias

    def movimentos_possiveis(self, tabuleiro):
        self.movimentosPossiveis = []
        if self.orientacao == 0:
            return
        
        if not self.ehDama:
            #Tem peça inimiga na casa
            #Se não tiver peça inimiga, verificar se não há peca ou limites obstruindo
            #Só assim, podemos fazer o movimento
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
            #Tem peça inimiga na casa
            #Se não tiver peça inimiga, verificar se não há peca ou limites obstruindo
            #Só assim, podemos fazer o movimento
            direcoes = [[1,1], [1,-1], [-1,1], [-1,-1]]
            for direcao in direcoes:
                bloqueado = False
                i = self.y + direcao[0]
                j = self.x + direcao[1]
                while(0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro) and not bloqueado):
                    podeCapturar = tabuleiro[i][j].orientacao == -self.orientacao
                    i += direcao[0]
                    j += direcao[1]

                    if podeCapturar and 0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro) and tabuleiro[i][j].orientacao == 0:
                        while(0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro) and not bloqueado):
                            softBlock = False
                            if tabuleiro[i][j].orientacao == -self.orientacao:
                                self.movimentosPossiveis += [[i,j]]
                            elif tabuleiro[i][j].orientacao == self.orientacao:
                                break
                            else:
                                softBlock = True

                            i += direcao[0]
                            j += direcao[1]

                            if tabuleiro[i][j].orientacao != 0 and softBlock:
                                bloqueado = True

                            
                        self.possuiCaptura = True
                        possuiCapturasDisponiveis[self.orientacao] = True
                    
                    else:
                        bloqueado = True

            if(not self.possuiCaptura and not possuiCapturasDisponiveis[self.orientacao]):
                for direcao in direcoes:
                        i = self.y + direcao[0]
                        j = self.x + direcao[1]
                        while(0 <= i and i < len(tabuleiro) and 0 <= j and j < len(tabuleiro) and tabuleiro[i][j].orientacao == 0):
                            self.movimentosPossiveis += [[i,j]]
                            i += direcao[0]
                            j += direcao[1]



    def movimentar_peca(self, movimento, tabuleiro): 
        '''Faz alterações no tabuleiro e retorna se o jogador deve jogar novamente ou não'''
        if movimento in self.movimentosPossiveis:
            
            y_range = range( self.y, movimento[0], sinal(movimento[0] - self.y))
            x_range = range( self.x, movimento[1], sinal(movimento[1] - self.x))
            #Como o movimento é diagonal, então len(y_range) = len(x_range)
            capturouPeca = False
            for k in range(len(y_range)):
                i = y_range[k]
                j = x_range[k]
                if(tabuleiro[i][ j].orientacao == -self.orientacao):
                    pontuacaoJogadores[self.orientacao] += 1
                    capturouPeca = True
                    
                tabuleiro[i][ j] = Peca(i, j, 0)

            tabuleiro[movimento[0]][movimento[1]] = self
            self.y = movimento[0]
            self.x = movimento[1]
            self.virar_dama()

            return capturouPeca #Se capturou uma peca, deve jogar novamente
        
        else:
            print("Movimento inválido")
            return True #Movimento inválido

                

    def virar_dama(self):
        if(self.orientacao == -1 and self.y == 0):
            self.ehDama = True

        if(self.orientacao == 1 and self.y == 9):
            self.ehDama = True

        return
    
    def __str__(self):
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

    orientacao = 0

    def __init__(self) -> None:

        self.escolherOrientacaoInicial()
        self.tabuleiro = self.iniciarTabuleiro()

    def escolherOrientacaoInicial(self):
        orientacaoInicial = input("Insira qual lado deve começar, C para as peças de cima ou B para as peças de baixo ")
        while orientacaoInicial != "B" and orientacaoInicial != "C":
            orientacaoInicial = input("Opção inválida, por favor escolha C para as peças de cima ou B para as peças de baixo ")

        if orientacaoInicial == 'C':
            self.orientacao = 1
        else:
            self.orientacao = -1

    def iniciarTabuleiro(self):
        tabuleiro = [[Peca(y,x,0) for x in range(10)] for y in range(10)]
        for i in range(10):
            for j in range(10):
                if((i+j)%2 and i < 3):
                    tabuleiro[i][j] = Peca(i,j,1)
                elif ((i+j)%2 and i > 6):
                    tabuleiro[i][j] = Peca(i,j,-1)

        return tabuleiro


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

    def jogarTurno(self):
        inputUsuario = input("Insira um movimento")

        try:

            posInicial = [int(inputUsuario[1]),ord(inputUsuario[0])-65]
            posFinal = [int(inputUsuario[5]),ord(inputUsuario[4])-65]
            peca: Peca = self.tabuleiro[posInicial[0]] [posInicial[1]]

        except Exception:
            print("Movimento inválido, peça fora do tabuleiro, escolha outro movimento")
            self.jogarTurno()
            return

        if peca.orientacao != self.orientacao:
            print("Peça invalida, escolha outro movimento")
            self.jogarTurno()
            return
        
        peca.movimentos_possiveis(self.tabuleiro) #Reconferir os movimentos possiveis da peca, pois é possivel que seja adicionados movimentos invalidos em IniciarTurno(self, tabuleiro) 
        #pois nem todas as pecas podem ter sido verificadas antes de se adicionar os movimentos

        print(peca.movimentosPossiveis)

        if(peca.movimentar_peca(posFinal, self.tabuleiro)):
            self.jogarTurno()
            return


    def iniciarJogo(self):
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

            if somaMovimentosBaixo == 0:
                print("Peças de Cima ganharam!")
                return
            
            if somaMovimentosCima == 0:
                print("Peças de Baixo ganharam!")
                return
        
            print("Turno das peças de " + (self.orientacao==1)*"Cima" + (self.orientacao==-1)*"Baixo")
            self.jogarTurno()
            self.orientacao = -self.orientacao

        
    def gameLoop(self):
        self.iniciarJogo()
        recomecar = input("Deseja recomeçar?")
        if(recomecar == "S"):
            self.escolherOrientacaoInicial()
            self.tabuleiro = self.iniciarTabuleiro()
            self.iniciarJogo()
            return
        else:
            print("Até a próxima")


def Damas():
    gerenciador = GerenciadorJogo()
    gerenciador.gameLoop()

Damas()



        
