'''
How while loop works in python
'''
import time
#Tenemos que hacer que este contador suba su valor en cada vuelta de que de 1 que es con lo que empezamos
#a número n
counter = 1
while counter <= 10:
    time.sleep(1.5)
    print(counter)
    counter += 1
#Como mestamos sumando 1  nos dará 1, 2, 3, etc. y al final el print de Good Bye
print("Good Bye")