# programa para implementar los operadores aritmeticos 
print("--------------------------------")
print("---OPERADORES ARITMETICOS-----")
print("--------------------------------")

# input
x= int(input("digite el valor de x: "))
y=int(input("Digite el valor de y: "))

# procesing
s = x + y
r = x - y
m = x * y
d = x / y
mod = x % y
de = x // y
p = x ** y

print("--------------------------------")
print("-------RESULTADOS---------------")
print("--------------------------------")

print("suma: " + str(s))
print("resta: " + str(r))
print("multiplicacion: " + str(m))
print("division:" +str(d))
print("modulo: " + str(mod))
print("parte entera de la division: " + str(de))
print("potencia: " + str(p))
