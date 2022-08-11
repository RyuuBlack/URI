numero = int(input())


salida = []

def operacion(expression):

    fraccion = []
    numerador = 0
    denominador = 0

    a, b, c , d = int(expression[0]) , int(expression[2]) , int(expression[4]) , int(expression[6])

    x = a / b
    y = c / d

    
    if (((x <= 1000) and (x > 0)) and ((y <= 1000) and (y > 0))):
        if expression[3] == "+":
            fraccion = [(a * d) + (c * b),b * d]
        elif expression[3] == "-":
            fraccion = [(a * d) - (c * b),b * d]
        elif expression[3] == "*":
            fraccion = [a * c,b * d]
        else:
            fraccion = [a * d,b * c]
    
    return fraccion

def MCD (fraccion):

    mcd = 1

    if fraccion[0] % fraccion[1] == 0:
        return fraccion[1]
    
    for i in range(int(fraccion[1]/2), 0, -1):
        if fraccion[0] % i == 0 and  fraccion[1] % i == 0:
            mcd = i
            break 
    
    return mcd

def simplify(fraccion,mcd):

    fra = str(fraccion[0]) + "/" + str(fraccion[1])
    fraccion[0] = int(fraccion[0] / mcd)
    fraccion[1] = int(fraccion[1] / mcd)
    simplified = str(fraccion[0]) + "/" + str(fraccion[1])
    salida = fra + " = " + simplified
    return salida

for i in range(numero):
    expression = str(input()).split(" ")
    fraccion = operacion(expression)
    mcd = MCD(fraccion)
    salida.append(simplify(fraccion,mcd)) 
    
for i in range(len(salida)):
    print(salida[i])

 
