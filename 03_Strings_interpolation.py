'''
Sample code of how the string interpolation works in python 
'''
name = "Guillermo"
last_name = "Bojorquez"

#Union de cadenas
print(name + " " + last_name)
# Usamos llaves para unir cadenas con un F-STRING
print(f"{name} {last_name}")
#Variables con F-STRING
full_name_f = f"{name} {last_name}"
print (full_name_f)
#String formatting (igual nos dará el nomre completo pero no se usa mucho por qué nos equivocamos al usarlo)
full_name_formatting = "{} {}".format(name,last_name)