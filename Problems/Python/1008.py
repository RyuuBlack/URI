n_empleado = int(input())
n_horas_trabajadas = int(input())
monto_horas = float(input())

salary = n_horas_trabajadas * monto_horas

print("NUMBER =",n_empleado)
print("SALARY = U$ "+str("{0:.2f}".format(salary)))

