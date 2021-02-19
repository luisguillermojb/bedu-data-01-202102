
'''
How the dictionaries work in Python
'''

Student_1 = {
    "name": "Galileo",
    "age": 5,
    "city": "Puerto Escondido",
    "Sate": "Oaxaca"
}

Student_2 = {
     "name": "Sofia",
    "age": 4,
    "city": "Zapopan",
    "Sate": "Jalisco"
}

print(Student_1)
#Nos dirá es qes class dict
print(type(Student_1))
#Para acceder a un datio en específico del diccionario podemos buscarlo
print(Student_1["name"])
#Podemos hacer un F-STRING para que nos diga "Galileo is 5 years old"
print(f'{Student_1["name"]} is {Student_1["age"]} years old.')
#Podemos formatear variables para que estas que haggar upper case
galileo = "galileo"
print(galileo.upper())
