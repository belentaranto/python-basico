user = {}

name = input("Por favor ingrese su nombre: ")
age = input("Por favor ingrese su edad: ")
address = input("Por favor ingrese su dirección: ")
phone = input("Por favor ingrese su número de teléfono: ")

user.__setitem__("Nombre",name)
user.__setitem__("Edad",age)
user.__setitem__("Dirección",address)
user.__setitem__("Teléfono",phone)

print(user)