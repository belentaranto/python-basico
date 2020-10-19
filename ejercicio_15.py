subjects = {
    "Matemática" : 6,
    "Física" : 4,
    "Química" : 5
}

for i,k in subjects.items():
    print(f"{i} tiene {k} créditos")

print(f"El curso en total tiene {sum(subjects.values())} créditos")