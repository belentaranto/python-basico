user = {}
answer = "si"

while answer.lower() == "si":
    key = input("Qué dato quiere ingresar? ").capitalize()
    value = input(f"{key}: ").capitalize()
    user.__setitem__(key,value)
    print(user)
    answer = input("Quiere ingresar algo más? ")
