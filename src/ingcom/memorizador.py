################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def memorizador(funcion):
    """
     Esto funciona guardando para un valor del argumento (n) el resultado de la funcion
     El decorador funciona para cualquier funcion que reciba un solo argumento.
     
     Formalmente, un decorador es una funcion que recibe la funcion a envolver y devuelve esta
     combinacion de envoltorio con funcion original, se utiliza para agregar caracteristicas sin
     modificar la funcion original, tratando a lo decorado como una "caja negra".
    """
    memoria = {}
    def ayudante(argumento):
        if argumento not in memoria:            
            memoria[argumento] = funcion(argumento)
        return memoria[argumento]
    return ayudante
