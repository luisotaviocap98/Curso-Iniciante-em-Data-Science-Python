import matplotlib.pyplot as plt 
import numpy

x = numpy.arange(-1000,1000,1)
'''
func1 = x**2
plt.subplot(1,2,1) #divide a regiao apresentada em linhas e colunas, e diz o indice da imagem
plt.plot(x,func1)

func2 = x
plt.subplot(2,2,2) 
plt.plot(x,func2)

func3 = x**3
plt.subplot(4,2,6) 
plt.plot(x,func3)

func4 = -x
plt.subplot(4,4,15) 
plt.plot(x,func4)

plt.show()'''

# ------------------------------------------------
figure = plt.figure(figsize=(10,10)) #para mudar o tamanho da janela
'''
figure.add_subplot(1,2,1)
plt.plot(x,x)
figure.add_subplot(2,2,2)
plt.plot(x,x**2)
figure.add_subplot(2,2,4)
plt.plot(x,x**3)
plt.show()
'''

func4 = -x
func3 = x**3
func2 = x
func1 = x**2
array_func = [func1,func2,func3,func4]

# for i in range(len(array_func)):
    # figure.add_subplot(2,2,i+1)
    # plt.plot(x,array_func[i])
# plt.show()

# --------------------------------------------------

from skimage.io import imread

# img = imread('pollen.jpg')
# plt.imshow(img)
# plt.show()

imgs = list()
path = 'dog/'

for i in range(4):
    imgs.append(imread(path+str(i+1)+'.jpg'))

for i in range(4):
    figure.add_subplot(2,2,i+1)
    plt.axis('off') #remover marcacao dos eixos
    plt.imshow(imgs[i])

plt.show()
