#Laisa Caroline da Costa Luz 552531
#Luiza Esther Martins 555516
#Maria Luiza Felipe 552655

def tamanhoTabuleiro():
    return 10

def casaPreta():
    return ' '

def casaBranca():
    return '#'

def pecaBaixo():
    return 'o'

def pecaCima():
    return '@'

def rainhaBranca():
    return '&'

def rainhaPreta():
    return 'O'

def corOposta(cor):
    if cor == pecaCima():
        return pecaBaixo()
    else:
        return pecaCima()

def iniciarTabuleiro(n):
    return [[((i+j)%2 and i < n/2  - 1)*pecaBaixo() + 
          ((i+j)%2 and i > n/2)*pecaCima() + 
          (not (i+j)%2)*casaBranca() +
        ((i+j)%2 and (i == n/2  - 1 or i == n/2))*casaPreta() 
        for j in range(n)] for i in range(n)]

def renderMove(piecePosIn, piecePosAfter, tabuleiro, pieceColor):
    #print(piecePosIn, piecePosAfter)
    tabuleiro[piecePosIn[0]][ piecePosIn[1]] = casaPreta()
    if piecePosIn[0] - piecePosAfter[0] >= 2:
        tabuleiro[int((piecePosIn[0] + piecePosAfter[0])/2)][int((piecePosIn[1] + piecePosAfter[1])/2)] = casaPreta()
    tabuleiro[piecePosAfter[0]][ piecePosAfter[1]] = pieceColor

def possibleMoves(piecePos, pieceColor, n, tabuleiro):

    step = 2*(pieceColor == pecaBaixo()) - 1
    possible_moves = [] #x,y,haveCapture
    haveCaptureMove = False

    if(piecePos[1] - 1 >= 0 and piecePos[0] + step >= 0 and piecePos[0] + step < n):
        if(tabuleiro[piecePos[0] + step][piecePos[1] - 1] == casaPreta() and not haveCaptureMove):
            possible_moves.append([piecePos[0] + step,piecePos[1] - 1, False])
        
        if(tabuleiro[piecePos[0] + step][piecePos[1] - 1] == corOposta(pieceColor)):
            if(piecePos[1] - 2 >= 0 and piecePos[0] + 2*step >= 0 and piecePos[0] + 2*step < n  and 
                tabuleiro[piecePos[0] + 2*step][piecePos[1] - 2] == casaPreta()):
                possible_moves.append([piecePos[0] + 2*step,piecePos[1] - 2, True])
                haveCaptureMove = True


    if(piecePos[1] + 1 < n and piecePos[0] + step >= 0 and piecePos[0] + step < n):
        if(tabuleiro[piecePos[0] + step][piecePos[1] + 1] == casaPreta() and not haveCaptureMove):
            possible_moves.append([piecePos[0] + step,piecePos[1] + 1, False])
        
        if(tabuleiro[piecePos[0] + step][piecePos[1] + 1] == corOposta(pieceColor)):
            if(piecePos[1] + 2 < n and piecePos[0] + 2*step >= 0 and piecePos[0] + 2*step < n  and 
                tabuleiro[piecePos[0] + 2*step][piecePos[1] + 2] == casaPreta()):
                possible_moves.append([piecePos[0] + 2*step,piecePos[1] + 2, True])
                haveCaptureMove = True
    
    if(piecePos[1] - 1 >= 0 and piecePos[0] - step >= 0 and piecePos[0] - step < n):

        if(tabuleiro[piecePos[0] - step][piecePos[1] - 1] == corOposta(pieceColor)):
            if(piecePos[1] - 2 >= 0 and piecePos[0] - 2*step >= 0 and piecePos[0] - 2*step < n  and 
                tabuleiro[piecePos[0] - 2*step][piecePos[1] - 2] == casaPreta()):
                possible_moves.append([piecePos[0] - 2*step,piecePos[1] - 2, True])
                haveCaptureMove = True

    if(piecePos[1] + 1 < n and piecePos[0] - step >= 0 and piecePos[0] - step < n):
        
        if(tabuleiro[piecePos[0] - step][piecePos[1] + 1] == corOposta(pieceColor)):
            if(piecePos[1] + 2 < n and piecePos[0] - 2*step >= 0 and piecePos[0] + 2*step < n  and 
                tabuleiro[piecePos[0] - 2*step][piecePos[1] + 2] == casaPreta()):
                possible_moves.append([piecePos[0] - 2*step,piecePos[1] + 2, True])
                haveCaptureMove = True

    for move in possible_moves:
        if(haveCaptureMove and move[2] == False):
            possible_moves.remove(move)

    return possible_moves

def printTabuleiro(tabuleiro):
    letras = 'ABCDEFGHIJ'
    linhaEntreCasas = '  +-+-+-+-+-+-+-+-+-+-+'
    print("   ",end="")
    for l in letras:
        print(l, end=" ")

    print(" ")
    for i in range(len(tabuleiro)):
        print(linhaEntreCasas)
        print(str(i), end=' |')
        for j in range(len(tabuleiro)):
            print(tabuleiro[i][j],end='|')
        print(i)

    print(linhaEntreCasas)
    print("   ",end="")
    for l in letras:
        print(l, end=" ")
    
    print(" ")
    

def temCaptura(cor, n , tabuleiro):
    temCaptura = False
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] == cor:
                for move in possibleMoves([i,j], cor, n, tabuleiro):
                    if(move[2]):
                        temCaptura = True
    
    return temCaptura

def turnoUsuario(cor, n, tabuleiro, capturaObrigatoria = False, pecaObrigatoria = [0,0]):
    printTabuleiro(tabuleiro)
    if(not capturaObrigatoria):
        piecePos = [int(e) for e in input("Insira a peça que deseja mover ").split()]
    else:
        print("Você deve usar a peça na posição" + str(pecaObrigatoria))
        piecePos = pecaObrigatoria

    if tabuleiro[piecePos[0]][piecePos[1]] != cor:
        print('Casa invalida')
        turnoUsuario(cor, n, tabuleiro)
        return
    
    possible_moves = possibleMoves(piecePos, cor, n, tabuleiro)

    if temCaptura(cor, n, tabuleiro):
        pecaValida = True
        for move in possible_moves:
            if not move[2]:
                pecaValida = False

        if not pecaValida:
            print("Você tem uma captura obrigatória, você não pode escolher esta peça!")
            turnoUsuario(cor, n, tabuleiro)
        

    print(possible_moves)
    if(len(possible_moves) == 4):
        comando = input("Insira 1, 2, 3 ou 4 para escolher o movimento ou insira qualquer outra tecla para escolher outra peça\n")
    if(len(possible_moves) == 3):
        comando = input("Insira 1, 2 ou 3 para escolher o movimento ou insira qualquer outra tecla para escolher outra peça\n")
    if(len(possible_moves) == 2):
        comando = input("Insira 1 ou 2 para escolher o movimento ou insira qualquer outra tecla para escolher outra peça\n")
    elif(len(possible_moves) == 1):
        comando = input("Insira 1 para movimentar ou insira qualquer outra tecla para escolher outra peça\n")
    else:
        print("Escolha outra peça")
        turnoUsuario(cor, n, tabuleiro)
        return
    
    if comando == '1':
        move = possible_moves[0]
    elif comando == '2' and len(possible_moves) >= 2:
        move = possible_moves[1]
    elif comando == '3' and len(possible_moves) >= 3:
        move = possible_moves[2]
    elif comando == '4' and len(possible_moves) == 4:
        move = possible_moves[3]
    else:
        turnoUsuario(cor, n , tabuleiro)
        return

    renderMove(piecePos, move[:2], tabuleiro, cor)

    if(move[2]):
        possible_future_moves = possibleMoves(move[:2], cor, n, tabuleiro)
        playAgain = False
        for future_moves in possible_future_moves:
            if(future_moves[2]):
                playAgain = True
        if(playAgain):
            turnoUsuario(cor, n ,tabuleiro, True, move[:2])

    return

def turnoAdversario(cor, n, tabuleiro, capturaObrigatoria = False, pecaObrigatoria = [0,0] ):
    printTabuleiro(tabuleiro)

    if(not capturaObrigatoria):
        piecePos = [int(e) for e in input("HEHEHEHE EU SOU O ADVERSARIO, mas não sei decidir :(\nInsira a peça que deseja mover\n").split()]
    else:
        print("HUHAUHA, Você deve usar a peça na posição" + str(pecaObrigatoria))
        piecePos = pecaObrigatoria
    
    if tabuleiro[piecePos[0]][piecePos[1]] != cor:
        print('Casa invalida')
        turnoUsuario(cor, n, tabuleiro)
        return
    
    
    possible_moves = possibleMoves(piecePos, cor, n, tabuleiro)

    if temCaptura(cor, n, tabuleiro):
        pecaValida = True
        for move in possible_moves:
            if not move[2]:
                pecaValida = False

        if not pecaValida:
            print("Você tem uma captura obrigatória, você não pode escolher esta peça!")
            turnoAdversario(cor, n, tabuleiro)

    print(possible_moves)
    if(len(possible_moves) == 4):
        comando = input("HEHEHEHEH, Insira 1, 2, 3 ou 4 para escolher o movimento ou insira qualquer outra tecla para escolher outra peça\n")
    if(len(possible_moves) == 3):
        comando = input("HEHEHEHHE, Insira 1, 2 ou 3 para escolher o movimento ou insira qualquer outra tecla para escolher outra peça\n")
    if(len(possible_moves) == 2):
        comando = input("HUHAUHAUHA, Insira 1 ou 2 para escolher o movimento ou insira qualquer outra tecla para escolher outra peça\n")
    elif(len(possible_moves) == 1):
        comando = input("HUAHUAHUHAUH, Insira 1 para movimentar ou insira qualquer outra tecla para escolher outra peça\n")
    else:
        print("HEHEHEHE EU SOU O ADVERSARIO, mas não sei decidir :(\n Escolha outra peça\n")
        turnoAdversario(cor, n, tabuleiro)
        return
    
    if comando == '1':
        move = possible_moves[0]
    elif comando == '2' and len(possible_moves) >= 2:
        move = possible_moves[1]
    elif comando == '3' and len(possible_moves) >= 3:
        move = possible_moves[2]
    elif comando == '4' and len(possible_moves) == 4:
        move = possible_moves[3]
    else:
        turnoAdversario(cor, n , tabuleiro)
        return

    renderMove(piecePos, move[:2], tabuleiro, cor)

    if(move[2]):
        possible_future_moves = possibleMoves(move[:2], cor, n, tabuleiro)
        playAgain = False
        for future_moves in possible_future_moves:
            if(future_moves[2]):
                playAgain = True
        if(playAgain):
            turnoAdversario(cor, n ,tabuleiro, True, move[:2])

    return

def vitoriasPretas(n, tabuleiro):
    vitoria = True
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] == pecaCima():
                if(len(possibleMoves([i,j],pecaCima(), n, tabuleiro)) > 0):
                    vitoria = False

    return vitoria

def vitoriasBrancas(n, tabuleiro):
    vitoria = True
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] == pecaBaixo():
                if(len(possibleMoves([i,j],pecaBaixo(), n, tabuleiro)) > 0):
                    vitoria = False

    return vitoria
    

def alguemGanhou(n, tabuleiro):
    if(vitoriasBrancas(n, tabuleiro)):
        print("Brancas venceram!!!")
        return True
    
    if(vitoriasPretas(n, tabuleiro)):
        print("Pretas venceram!!!")
        return True
    
    return False

    

def gerenciadorTurnos(corUsuario, n, tabuleiro):
    cor = pecaCima()
    while not alguemGanhou(n, tabuleiro):
        if(corUsuario == cor):
            turnoUsuario(corUsuario, n, tabuleiro)
        else:
            turnoAdversario(cor, n, tabuleiro)

        cor = corOposta(cor)  

            
def escolherCor():

    print("Bem vindo ao Jogo de Damas! Antes de começarmos, escolha com que peças você quer jogar :")
    corUsuario = input("Insira C para jogar com as peças de cima (o) e B para jogar com as peças de baixo (@)\n")
    if corUsuario == "C":
        cor = pecaCima()
    elif corUsuario == "B":
        cor = pecaBaixo()
    else:
        print("Escolha uma cor válida")
        return escolherCor()
        
    return cor


def Damas():
    
    cor = escolherCor()
    n = tamanhoTabuleiro()
    tab = iniciarTabuleiro(n)
    gerenciadorTurnos(cor, n, tab)


Damas()

    
