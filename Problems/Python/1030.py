n_casos = int(input())
casos = []

for i in range(n_casos):
    n_hombres, paso = map(int, input().split())

    circulo = []

    for i in range(n_hombres):
        circulo.append(i+1)

    index = 0 

    while len(circulo) != 1:


        for i in range(paso):

            if index >= len(circulo):
                index = 0

            if i == paso-1:
                circulo.pop(index)
                index -= 1
            
            index += 1

    casos.append(circulo[0])
            
for i in range(len(casos)):
    print("Case "+str(i+1)+ ":",casos[i])         



