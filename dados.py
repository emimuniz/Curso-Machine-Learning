#chamando no cmd:
#from dados import carregar_acessos
#X, Y = carregar_acessos()

import csv #importando o arquivo csv

def carregar_acessos(): #função para carregar os acessos, abre o arquivo e ler.

    X = [] #pega os valores da esquerda 
    Y = [] #pega os valores da direita

    arquivo = open('acesso.csv', 'r') #abrir o arquivo e ler
    leitor = csv.reader(arquivo) #baseado no arquivo criar um leitor csv.reader, baseado no arquivo

    leitor.__next__() #pula linha(sem mostrar o nome da coluna)

    for acessou_home,acessou_como_funciona,acessou_contato, comprou in leitor: #ler cada coluna do arquivo

        X.append([int(acessou_home),int(acessou_como_funciona)
         ,int(acessou_contato)])#para cada coluna adici. no dados

        Y.append(int(comprou)) #adicionar a ultima coluna nas marcacoes

    return X, Y

def carregar_buscas():
    X = []
    Y = []

    arquivo = open('busca.csv', 'r')
    leitor = csv.reader(arquivo)

    leitor.__next__()

    for home,busca,logado,comprou in leitor:

        X.append([int(home),busca,int(logado)])

        Y.append(int(comprou))

    return X,Y
