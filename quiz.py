# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input

a = float(input("Ingrese la longitud del primer lado (a): "))
b = float(input("Ingrese la longitud del segundo lado (b): "))
c = float(input("Ingrese la longitud del tercer lado (c): "))

# processing

if a + b > c and a + c > b and b + c > a:
    es_triangulo = True
else:
    es_triangulo = False

# output

if es_triangulo:
    print("Los lados dados pueden formar un triángulo.")
else:
    print("Los lados dados no pueden formar un triángulo.")
