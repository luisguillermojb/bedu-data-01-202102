'''
IF condition
'''
import time
# la variable "name" será igual a la respuesta que el usuario de a ese input.
name = input("Whats your name?")
# después de que el usuario nos dió el input nosotros mandaremos un mensaje con una interpolación de cadenas.
print(f"Hello {name}")
#Con esta variable definiremos la longitus (len) de la respuesta
magic_number = 6
time.sleep(2.0)
#Si la longitun (len) de la variable "name"
if len(name) > magic_number:
    print("Sorry, but you lost")
#Otro IF
elif len(name) == magic_number:
     print("Congrats, you got a special prize.") 
#Todos los otros resultados
else: 
    print("You Won! :)")
time.sleep(2.0)
print("Good bye!")


