import numpy as np

m = np.arange(729).reshape(9,9,9)

#Obtener las posiciones del numero inicial del bloque dado por:
# xBloque = (num%9)%3
# yBloque = (num%9)/3
# zBloque = num/9
# Cada una de estas posiciones la multiplicamos por 3 para hallar la posicion exacta

def getPosBloque(num):
    return [(int)((num%9)%3)*3, (int)(np.floor((num%9)/3))*3,(int)(np.floor(num/9))*3]

#El intercambio se hace por un simple swap con una variable temporal
#teniendo en cuenta que la variable temporal tenemos que añadirle *1 para asi no 
#tener guardado la referencia del bloque sino el valor

def intercambio(num1, num2):
    posNum1 = getPosBloque(num1)
    posNum2 = getPosBloque(num2)
    temp = m[posNum1[2]:posNum1[2]+3,posNum1[1]:posNum1[1]+3,posNum1[0]:posNum1[0]+3] * 1
    m[posNum1[2]:posNum1[2]+3,posNum1[1]:posNum1[1]+3,posNum1[0]:posNum1[0]+3] = m[posNum2[2]:posNum2[2]+3,posNum2[1]:posNum2[1]+3,posNum2[0]:posNum2[0]+3]
    m[posNum2[2]:posNum2[2]+3,posNum2[1]:posNum2[1]+3,posNum2[0]:posNum2[0]+3] = temp

intercambio(0,3)

print(m)