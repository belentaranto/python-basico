subjects = {
    "Matemática" : 7,
    "Física" : 3,
    "Química" : 8
}

for i,k in subjects.items():
    print(f"{i} tiene {k} créditos")

print(f"El curso en total tiene {sum(subjects.values())} créditos")