# dicio = {
    # 'nome':'',
    # 'idade':22,
    # 'sexo':'sempre',
    # 'dinheiro':10500
# }

# lo = dict(dicio)
# lo['nome'] = 'luis'
# bia = dict(dicio)
# bia['nome']='beatriz'

# print(bia,lo)
# print(lo.values())

# ------------------------------------------------

# func1 = lambda a,b : a + (a*b)

# print(func1(b=2,a=3))

# def teste(i):
    # print(i)
    # return lambda a : a * (i+a)

# op1 = teste(2) #op1 esta recebendo a funcao lambda
# op2 = op1(3)
# print(op2,type(op1))

# -------------------------------------------------

x = [1,2,3,4,5]
y = [6,7,8,9,10]

soma = lambda a,b : a+b

print(map(soma,x,y))

res = [a+b for a,b in zip(x,y)]

print(res)

ascii = [chr(ord(i)+1) for i in 'LuisOtavio']
# ord pega o valor ascii, e chr de ascii para char
print(ascii)
