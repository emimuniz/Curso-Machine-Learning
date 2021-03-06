import pandas as pd
from collections import Counter
import numpy as np
from sklearn.model_selection import cross_val_score



classificacoes = pd.read_csv('emails.csv') #lendo o arquivo email
textosPuros = classificacoes['email'] #Pega a coluna email
#Ler em string e transforma em minuscula
#Ler em string e separa com espaço
textosQuebrados = textosPuros.str.lower().str.split(' ') 

#Guarda as palavras no conjunto
#Não pode repetir palavras
dicionario = set()


#Roda a lista e guarda as palavras no dicionario
for lista in textosQuebrados: 
	dicionario.update(lista)

#quantidade de palavras
totaldePalavras = len(dicionario)

#print(totaldePalavras) -> mostra na tela a quantidade de palavras

#zip junta as palavras com os numeros
#range cria um intervalo de 0 até o totaldePalavras
tuplas = zip(dicionario, range(totaldePalavras))

#Cria um dicionario
#Que roda e guarda a Palavra e o indice
tradutor = {palavra:indice for palavra, indice in tuplas}

#Cria um vetor com a quantidade de palavras
#Cria um for que roda todas as palavras dessa frase
#Se a palavra existe no tradutor
#Posicao = tradutor[palavra]
#vetor[palavra] += 1

def vetorizar_texto(texto, tradutor):
	vetor = [0] * len(tradutor)

	for palavra in texto:
		if palavra in tradutor:
			posicao = tradutor[palavra]
			vetor[posicao] += 1

	return vetor

#print(textosQuebrados[0]) -> mostrando a primeira frase
texto = textosQuebrados[0]

#Passa por todas as frases usando a funcao vetorizar_texto
vetoresDeTexto = [vetorizar_texto(texto,tradutor) for texto in textosQuebrados]

#Pegando a ultima coluna
marcas = classificacoes['classificacao']

# X = para comparar
# Y = treino

X = np.array(vetoresDeTexto)
Y = marcas.tolist()

porcentagem_de_treino = 0.8

tamanho_do_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_validacao = len(Y) - tamanho_do_treino #oque sobra


treino_dados = X[0:tamanho_do_treino]
treino_marcacoes = Y[0:tamanho_do_treino]

validacao_dados = X[tamanho_do_treino:]
validacao_marcacoes = Y[tamanho_do_treino:]

def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes):
    k = 10
    scores = cross_val_score(modelo, treino_dados, treino_marcacoes, cv = k)
    taxa_de_acerto = np.mean(scores)

    msg = "Taxa de acerto do {0}: {1}".format(nome,taxa_de_acerto)
    print(msg)
    return taxa_de_acerto

def teste_real(modelo, validacao_dados, validacao_marcacoes):
    resultado = modelo.predict(validacao_dados)

    acertos = resultado == validacao_marcacoes

    total_de_acertos = sum(acertos)
    total_de_elementos = len(validacao_marcacoes)

    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

    msg = "Taxa de acerto do vencedor entre os dois algoritmos no mundo real: {0}".format(taxa_de_acerto)
    print(msg)

resultados = {}

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

modeloOneVsRest = OneVsRestClassifier(LinearSVC(random_state=0))
resultadoOneVsRest = fit_and_predict("OneVsRest", modeloOneVsRest, treino_dados, treino_marcacoes)
resultados[resultadoOneVsRest] = modeloOneVsRest


from sklearn.multiclass import OneVsOneClassifier

modeloOneVsOne = OneVsOneClassifier(LinearSVC(random_state=0))
resultadoOneVsOne = fit_and_predict("OneVsOne", modeloOneVsOne, treino_dados, treino_marcacoes)
resultados[resultadoOneVsOne] = modeloOneVsOne

from sklearn.naive_bayes import MultinomialNB

modeloMultinomial = MultinomialNB()
resultadoMultinomial = fit_and_predict("MultinomialNB", modeloMultinomial, treino_dados, treino_marcacoes)
resultados[resultadoMultinomial] = modeloMultinomial

from sklearn.ensemble import AdaBoostClassifier

modeloAdaBoost = AdaBoostClassifier(random_state=0)
resultadoAdaBoost = fit_and_predict("AdaBoostClassifier", modeloAdaBoost, treino_dados, treino_marcacoes)
resultados[resultadoAdaBoost] = modeloAdaBoost


print(resultados)

maximo = max(resultados)
vencedor = resultados[maximo]

print("Vencerdor: ")
print(vencedor)

vencedor.fit(treino_dados, treino_marcacoes)

teste_real(vencedor, validacao_dados, validacao_marcacoes)

acerto_base = max(Counter(validacao_marcacoes).values())
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)

total_de_elementos = len(validacao_dados)
print("Total de teste: %d" % total_de_elementos)