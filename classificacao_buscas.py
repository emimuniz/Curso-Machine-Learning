#algoritmo precisa ter 3 fases:
#Treinar o algoritmo 80%
#Testar o algoritmo	 10%	
#Escolher o melhor entre eles e testar com os dados reais 10%

import pandas as pd #importando o panda
from collections import Counter

df = pd.read_csv('busca.csv') #lendo o arquivo dataframe

#Teste de Validação
#home, busca, logado
#home, logado
#home, busca
#busca, locado
#logado
#home
#busca
#7 testes de vaidação

X_df = df[['home', 'busca', 'logado']] #pegando as colunas do dataframe 
Y_df = df[['comprou']] #pegando as colunas do dataframe

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values #transformando em array os valores da colunas X
Y = Ydummies_df.values #transformando em array os valores da coluna Y

#fazendo a validação de dados reais
porcentagem_treino = 0.8
porcentagem_teste = 0.1

tamanho_treino = int(porcentagem_treino* len(Y)) 
tamanho_teste = int(porcentagem_teste * len(Y))

tamanho_de_treino = int(porcentagem_treino * len(Y)) #descobrir 90% de Y
tamanho_de_teste = len(Y) - tamanho_de_treino #descobrir oque falta

treino_dados = X[:tamanho_de_treino] #atribuindo a quantidade de dados
treino_marcacoes = Y[:tamanho_de_treino] #atribuindo a quantidade de marcacacoes

simplica_dados = tamanho_treino + tamanho_teste #fazendo a soma das colunas

teste_dados = X[tamanho_treino: simplica_dados] #atribuindo a quantidade que falta de dados
teste_marcacoes = Y[tamanho_treino: simplica_dados] #atribuindo a quantidade que falta de marcacao

Validação_do_FinalDados = X[simplica_teste:]
Validação_do_FinalMarcacoes = Y[simplica_teste:]

#funcao chamando os testes de algoritmo
def Segundo_Teste (nome, modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
	modelo.fit(treino_dados, treino_marcacoes)

	resultado = modelo.predict(teste_dados)

	diferencas = resultado - teste_marcacoes

	acertos = resultado == teste_marcacoes
	total_de_acertos = sum(acertos)
	total_de_elementos = len(teste_dados)

	taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

	novaMensagem = "Taxa de acertos do algoritmo {0}: {1}".format(nome, taxa_de_acerto)
	print(novaMensagem)
	
	return taxa_de_acerto

	
#importando AdaBoostClassifier procurando melhoras da classificação do algoritmo 
from sklearn.esemble import AdaBoostClassifier
	modeloAdaBoost = AdaBoostClassifier()#criando um modelo do AdaBoostClassifier
	resultadoAdaBoostClassifier = segundo_Teste("AdaBoostClassifier", modeloAdaBoost, treino_dados, treino_marcacoes, teste_dados, teste_marcacao)

	
#importantado pelo MultinomialNB forma mais simples de classificação do algoritmo	
from sklearn.naive_bayes import MultinomialNB

	modeloMultinomial = MultinomialNB() #criando um modelo do MultinomialNB
	resultadoMultinomial = segundo_Teste("MultinomialNB", modeloMultinomial, treino_dados, treino_marcacao, teste_dados, teste_marcacao)
	
	#testando algoritmo atraves do 0 e 1 
	acerto_base = max(Counter(teste_marcacoes).values())
	taxa_de_acerto = 100.0 * acerto_base / len(teste_marcacoes)
	print("Taxa de acerto base: %f" %taxa_de_acerto)	

	if resultadoMultinanomial > resultadoAdaBoost:
		vencedor = modeloMultinomial
	else:
		vencedor = modeloBoost
		
def teste_real(modelo, validacao_dados, validacao_marcacoes):
		resultado = modelo.predict(validacao_dados)
		
		acertos = resultado == validacao_marcacoes
		
		total_acertos = sum(acertos)
		total_elementos = len(validacao_marcacoes)
		
		taxa_acerto = 100.0 * total_acertos / total_elementos 
		
	
	#mostrando a quantidade de elementos do algoritmo 
	total_de_elementos = len(teste_dados)
	print(total_de_elementos)

