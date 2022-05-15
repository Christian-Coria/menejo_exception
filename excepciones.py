# bloque try exception
resultado = None   #DECIMOS QUE ESTA VARIABLE NO TIENE NINGUN VALOR ASIGNADO se define esta variable 
#fuera del bloque try except para poer reutilizarga fuera en el print

try:      # try = intenta
    a = int(input("Introduce el primer numero: "))
    b = int(input("Introduce el segundo numero: "))
    print("calculando division....")
    resultado = a/b
    #capturamos la exception en la clase padre de las exepciones y la renombramos "e"
except Exception as e:
    print(f"ocurrio un error: {e}")

#BLOQUE OPCIONAL: else solo se ejecita si no hubo exception
else:
    print("No hubo errores, felicidades")
#bloque finally: independientemente de error o no SIEMPRE SE EJECUTA
finally:
    print("termino la operacion!!!")
#si manejaramos errores de forma mas especificas se aplican otros exept de la misma manera dentro
#en ese caso la clase Exception va a final no al principio
print(f"el resultados es {resultado}") #utilizamos la variable
print("continuamos.....")

