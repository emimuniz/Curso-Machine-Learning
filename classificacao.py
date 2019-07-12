# [é gordinho?, tem perninha curta?, faz auau?]

porco1 = 	[1, 1, 0]
porco2 = 	[1, 1, 0]
porco3 = 	[1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]

marcacoes = [1, 1, 1, -1, -1, -1]


#importando do sklearn da parte do naive importar o MutinomialNB (algoritmo para ensinar o modelo) **
from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes) # Se encaixa a essas informacoes

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

testes = [misterioso1, misterioso2,misterioso3]

marcacoes_teste = [-1, 1, -1] # confirmacao da verificacao

resultado = modelo.predict(testes) #verifica a previsão
print(resultado)

diferenca = resultado - marcacoes_teste #verificando se o resultado bate com as marcaçoes
print(diferenca)

#fazendo if para comparar o iguais
acertos = [d for d in diferenca if d == 0]


total_de_acertos = len(acertos)
total_de_elementos = len(testes)
taxa_de_acertos = 100.0 * total_de_acertos / total_de_elementos # porcentagem de acertos

print(taxa_de_acertos)
