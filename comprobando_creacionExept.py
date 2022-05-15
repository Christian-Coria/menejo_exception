from creando_except import numeros_identicos
#importamos la clase creada

resultado = None   

try:   
    a = int(input("Introduce el primer numero: "))
    b = int(input("Introduce el segundo numero: "))
    print("calculando division....")
    resultado = a/b
    if a == b:  # raise es una palabra reservada para ñuego llamar a la clase creada y 
                #opcional es el mensaje
                #asi "raise puede manejar cualquier tipo de except"
        raise numeros_identicos("error numeros identicos")
    
except Exception as e:
    print(f"ocurrio un error: {e}")

else:
    print("No hubo errores, felicidades")

finally:
    print("termino la operacion!!!")

print(f"el resultados es {resultado}") 
print("continuamos.....")

