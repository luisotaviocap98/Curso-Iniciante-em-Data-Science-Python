import pandas 
import matplotlib.pyplot as plt
import numpy

tst = pandas.read_csv('athlete_events.csv')
# tst.hist(column='Age',bins=10) #column eh a coluna selecionada no dataset, bins quantidade de barras
# plt.show()

# ------------------------------------------------------

# tst.boxplot(column='Age')
# tst.boxplot(column=['Age','Weight']) # varios boxplot de varias colunas
# plt.show()

# -----------------------------------------------
# x=[1,2,3,4,5,6,7,8,9,10]
# y=[1,2,3,4,5,6,7,8,9,10]
# plt.scatter(x,y) #plotar x em relacao a y, como se fossem coordenadas
# plt.show()

# a=numpy.arange(0,100,1)
# plt.plot(a,a**2) #plotar funcoa matematica a²
# plt.show()

# homem = tst.loc[tst['Sex']=='M']
# plt.scatter(homem['Height'],homem['Weight']) #relacao altura e peso dos atletas masculinos
# plt.show() #a imagem resultante indica que quanto maior a altura maior o peso (+/-)

# --------------------------------------------------

teste = tst.dropna() #remover linhas contendo dados faltantes  / NaN de todo o dataset
teste2 = tst.isnull() #verifica dado por dado se ele eh NaN
teste3 = tst.isnull().sum() #soma em cada coluna a quantidade de dados true (faltantes)
# teste4 = tst['coluna'].fillna(opcao) #substitui na coluna as aparicoes de NaN pela opcao digitada, 
                                    # que pode ser uma string ou numero, 
                                    # em caso de numeros eh comum substituir pela media ou desvio padrao
teste4 = tst['coluna'].fillna(tst['coluna'].mean()) #substituindo NaN pela media
