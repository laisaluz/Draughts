# Função principal 

import sys
import offdamas
import uudamas

def Damas():
    print(sys.argv)

  #2 e 1, pois a função principal também conta como argumento
  
    if len(sys.argv) == 2:
        gerenciador = offdamas.GerenciadorJogo()  #ativa o modo Offline 

    elif len(sys.argv) == 1:
        gerenciador = uudamas.GerenciadorJogo() #ativa o modo Usuários vs Usuário

    else:
        print("Entrada invalida, é permitido até um arquivo")
    
    
    gerenciador.gameLoop()


Damas()
