"""
Módulo que agrupa todas las funcionalidades
que permiten solicitar introducir un dato numérico
"""


import sys #estamos llamando al sistema para interactuar con nuestro sistema. es para captura, corrección y optimizacion de errores
#XD ponlo cd vayas a interactuar muchas veces con la consola

MIN=0
MAX=100 #Esto hay que cambiarlo cuando te pide otro rango de numeros. este es un numero muy pequeño


def solicitar_introducir_numero(invite):
    #XD invite significa que todo lo que metamos ahí, nos lo convierte en cadena
    """
    Esta función verifica que tenemos un número
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end=": ")
        datoIntroducido = input()

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            print("Solo están autorizados los caracteres [0-9].", file=sys.stderr)
            #XD SI QUIERES CAMBIAR QUE VAYA DEL 0-9 LO CAMBIAS AHÍ EN EL TEXTO
        else:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido

def solicitar_introducir_numero_extremo(invite, minimum=MIN, maximum=MAX):
    """
    Esta función utiliza el anterior y añade una post-condición
    sobre los extremos del número a introducir
    """
    invite = "{} entre {} y {} incluídos".format(invite, minimum, maximum)
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        datoIntroducido = solicitar_introducir_numero(invite)

        if minimum <= datoIntroducido <= maximum:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido

