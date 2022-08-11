nombre = str(input())
salary = float(input())
ventas = float(input())

bonus = (15 * ventas) / 100
salary += bonus

print("TOTAL = R$ "+str("{0:.2f}".format(salary)))