# import numpy 

# a = numpy.array([1,2,3])
# a.max() #maior elemento da matriz
# a.min() #menor elemento da matirz
# a.sum() #soma dos elementos da matriz
# a.mean() #media da soma dos elementos da matriz
# a.std() #desvio padrao dos elementos da matriz
# print(a)

# --------------------------------------------

import pandas 

# teste = pandas.read_excel('Planilha data science.xlsx')
# tst = pandas.read_csv('Planilha data science - Página1.csv')

# print(tst.head()) #primeiras X (padrao 5) linhas

data = pandas.DataFrame({'nome':['luis','joao','paula','mario'],
                        'idade':[12,14,15,10],
                        'sexo':['m','m','f','m']}) #interno tem um dicionario
# print(data)
# print(data.shape) #retorna qnt linhas e colunas 
# print(data.describe()) #traz operacoes matematicas e estatisticas
# print(data['nome']) #filtrar coluna nome
# print(data.loc[[0,2]]) #filtrando linha zero e dois
# print(data.loc[0:2]) #filtrando da linha zero ate a dois
# print(data.loc[data['nome']=='luis']) #query filtrando a linha onde na coluna nome corresponde a 'luis'
# print(data['nome'].loc[2]) #trazendo apenas a linha 2 da coluna nome
# print(data.size) #retorna quantidade de elementos
# print(data.loc[data['idade']>=12]) #retorna as linhas onde a idade eh maior ou igual a 12
data = data.rename(columns={'nome':'Nome','idade':'age'}) #mudando nomes das colunas
print(data)
print(data['age'].value_counts()) #contabilizando repeticoes de um valor em uma coluna
data.drop('nome',axis=1) #excluindo a coluna nome, axis 0 eh linha axis 1 eh coluna
