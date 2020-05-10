#Calculadora de operaciones basicas 
primernumero = 2
segundonumero = 4
suma = int(primernumero) + int(segundonumero)
resta = int(primernumero) - (segundonumero)
dividir = int(primernumero) / int(segundonumero)
multiplicacion = int(primernumero) * int(segundonumero)
modulo = int(primernumero) % int(segundonumero)
divisionentera = int(primernumero) // int(segundonumero)
igual = int(primernumero) == int(segundonumero)
exponente = int(primernumero) ** int(segundonumero)
mayorque = int(primernumero) > int(segundonumero)
menorque = int(primernumero) < int(segundonumero)

print("la suma es, " + str(suma))
print("la resta es, " + str(resta))
print("la division es, " + str(dividir))
print("la multiplicacion es, " + str(multiplicacion))
print("el residuo es, " + str(modulo))
print("el primer numero es igual que el compareciente, " + str(igual))
print("el exponente es, " + str(exponente))
print("el  primer numero es mayor que el segundo numero, "+ str(mayorque))
print("el primer numero es menor que el segundo numero, " + str(menorque))
