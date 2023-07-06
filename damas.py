# Função principal : responsável por executar o programa 

import sys
import offdamas
import uudamas

def Damas():

    ''' Função responsável por determinar o modo de jogo e executar o objeto "gerenciador" apropriado da classe "offdamas.GerenciadorJogo" ou "uudamas.GerenciadorJogo"'''

   # Se o número de argumentos na linha de comando for 2, ou seja, o arquivo de texto e a função principal, então o programa instancia o objeto "geranciador" da classe "uudamas.GerenciadorJogo" e começa o modo offline
  
    if len(sys.argv) == 2:
        gerenciador = offdamas.GerenciadorJogo()  

    # Se for igual a 1 (apenas a função principal), então começará a versão Usuário vs Usuário 
    
    elif len(sys.argv) == 1:
        gerenciador = uudamas.GerenciadorJogo() 

    # Se nenhum dos casos acima for feito, então a entrada será inválida
    
    else:
        print("Entrada invalida, é permitido até um arquivo")
    
    
    gerenciador.gameLoop()


Damas()
