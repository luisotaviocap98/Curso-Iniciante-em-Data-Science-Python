import pandas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier #arvore de decisao
data = pandas.read_csv('/home/luisotavio/Downloads/datasets_16721_22034_wine_dataset.csv')

data['style'] = data['style'].replace('red',0)
data['style'] = data['style'].replace('white',1)

y=data['style'] #gabarito
x=data.drop('style',axis=1) #recebe o dataset todo exceto a coluna style, essa vai ser testada 

x_train, x_teste, y_train, y_teste = train_test_split(x,y,test_size=0.3)

modelo = ExtraTreesClassifier()
modelo.fit(x_train,y_train) #treina o algoritmo, aprende a reconhecer e confere no gabarito
resultado = modelo.score(x_teste,y_teste) #testa o algoritmo, usando a parte de teste e confere com o gabarito
print(resultado) #porcentagem de acerto

# modelo.predict(x_teste[100:150]) #previsao dos dados de teste da linha 100 a 150, pode usar essa funcao para novos dados 