#Criando arquivo para modo offline
import sys 

if len(sys.argv) > 1:
    nome_arquivo = sys.argv[1]
    with open(nome_arquivo, 'r+') as arquivo: #abrindo arquivo para escrever e ler 
        confirm = 'S'
        linha1 = input('Qual posição você quer começar? Digite C para cima ou B para baixo: ')

        while confirm != 'enter':
            linha = input('Insira uma jogada: ')
            arquivo.writelines(linha + '\n')
            confirm = input('Digite enter se não tiver mais jogadas')

    with open(nome_arquivo, 'r') as arquivo:
        jogadas = arquivo.readlines()

    print(jogadas)
