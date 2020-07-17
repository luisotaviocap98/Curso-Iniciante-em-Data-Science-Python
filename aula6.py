import pandas as pd
import matplotlib

dadosENEM = pd.read_csv('microdados_enem2018/DADOS/MICRODADOS_ENEM_2018.csv',sep=';',encoding='ISO-8859-1',nrows=100) #lendo arquivo, dizendo o separador, tipo de codificacao, e quantidade de linhas
# dadosENEM.head()
# dadosENEM[0:100] #usar apenas 100 primeiras linhas
# print(dadosENEM.columns.values) #mostrar todos os nomes das colunas

colunas = ['NU_INSCRICAO', 'SG_UF_RESIDENCIA' ,'NU_IDADE','IN_GESTANTE', 'TP_SEXO' ,'TP_COR_RACA', 'TP_NACIONALIDADE',
 'TP_ESCOLA', 'TP_ENSINO' ,'CO_MUNICIPIO_PROVA' ,'NO_MUNICIPIO_PROVA' ,'CO_UF_PROVA', 'SG_UF_PROVA' ,'TP_PRESENCA_CN',
 'TP_PRESENCA_CH' ,'TP_PRESENCA_LC', 'TP_PRESENCA_MT' ,'CO_PROVA_CN' ,'CO_PROVA_CH' ,'CO_PROVA_LC' ,'CO_PROVA_MT' ,'NU_NOTA_CN',
 'NU_NOTA_CH' ,'NU_NOTA_LC' ,'NU_NOTA_MT' ,'TP_STATUS_REDACAO' ,'NU_NOTA_COMP1' ,'NU_NOTA_COMP2' ,'NU_NOTA_COMP3' ,'NU_NOTA_COMP4'
 'NU_NOTA_COMP5' ,'NU_NOTA_REDACAO','Q001','Q002'] #selecionando algumas colunas

dados_selecionados = dadosENEM.filter(items=colunas)
print(dados_selecionados.head())

city = dados_selecionados['NO_MUNICIPIO_PROVA'] #selecionar uma coluna especifica
print(city) 
print(city.value_counts().sort_index()) #mostrando a contagem de vezes que um valor aparece, e ordenando

print(dados_selecionados['NU_IDADE'].value_counts().sort_index()) #filtrando a quantidade de vezes que uma determinada idade aparece
# dados_selecionados['NU_IDADE'].hist(bins=50) #gerando histograma dos dados de idade, bins controla a quantidade de colunas no histograma

dados_selecionados['SG_UF_RESIDENCIA'].hist(bins=27)
# matplotlib.pyplot.show()

gravida = dados_selecionados['IN_GESTANTE'].value_counts()
print([100*x/gravida.sum() for x in gravida]) #mostrando porcentagem de mulheres gestantes e nao gestantes, porem nesses dados tambem estao inclusos homens

