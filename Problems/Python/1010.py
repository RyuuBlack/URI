producto_uno = str(input()).split(" ")
producto_dos = str(input()).split(" ")

b_uno, c_uno =  int(producto_uno[1]), float(producto_uno[2]) 
b_dos, c_dos = int(producto_dos[1]), float(producto_dos[2]) 

total_pagar = (b_uno * c_uno) + (b_dos * c_dos)

print("VALOR A PAGAR: R$ "+str("{0:.2f}".format(total_pagar)))