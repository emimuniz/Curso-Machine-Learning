#minha abordagem inicial foi
# Separar 90% para treino e 10% para teste

from dados import carregar_acessos

X, Y = carregar_acessos()

#separando para treino
treino_dados = X[:90] #pegando os primeiros 
treino_marcacoes = Y[:90]

#separando para teste
teste_dados= X[-9:] #pegando os ultimos 9
teste_marcacoes = Y[-9:]

from sklearn.naive_bayes import MultinomialNB
 
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)

resultado = modelo.predict(teste_dados)

diferenca = resultado - teste_marcacoes

acertos = [d for d in diferenca if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)
print(total_de_elementos)