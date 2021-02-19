'''
List interaction using for loop.
'''
#ISR_TAX es una constante por lo que se pone en mayuscula. 
#Lo que haremos es calcular el ISR de cada uno de los importes del listado usando esa contsante.
ISR_TAX = 0.35 

salaries = [
    12000.00,
    10000.00,
    11000.00,
    10500.00,
    9000.00,
    11200.00
]

for s in salaries:
#Así calculamos el ISR de casa importe
    print(s*ISR_TAX)

#Podemos hacer una variable
salary_tax = s*ISR_TAX
print(salary_tax)

#Podemos usar variable y aparte F-STRING con unas cosas extra para que solo nos traega 
# los número flatantes redendeados.
salary_tax = s*ISR_TAX
Print(f'{salary_tax:.2f}')  

#Otra forma de redondear sería: (esto ni decimales dará)
salary_tax = round(salary_tax)
print(salary_tax)
