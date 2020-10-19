divisas = {
    "Euro" : "€",
    "Dolar" : "$",
    "Yen" : "¥"
    }

answer = input("Por favor ingrese un tipo de divisa: ")
answer = answer.capitalize()

if answer in divisas:
    print(f"El símbolo del {answer} es {divisas[answer]}")
else:
    print("La divisa no fue encontrada")

"""
Mi idea original fue plantearlo así pero al recorrer el diccionario se fija en todas las claves y me devuelve
la búsqueda en cada uno, no supe cómo hacer para que sólo me devuelva el valor correcto

for i,k in divisas.items():
    if answer == i:
        print(f"El símbolo del {i} es {k}")
    else:
        print("La divisa no ha sido encontrada")
"""