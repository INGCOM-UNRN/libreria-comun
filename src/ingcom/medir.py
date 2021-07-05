################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import time


def timeit(funcion):
    """
     Formalmente, un decorador es una funcion que recibe la funcion a envolver y devuelve esta
     combinacion de envoltorio con funcion original, se utiliza para agregar caracteristicas sin
     modificar la funcion original, tratando a lo decorado como una "caja negra".
    """
    def timed(*args, **kwargs):
        inicio = time.time()
        result = funcion(*args, **kwargs)
        fin = time.time()
        transcurrido = (fin - inicio) * 1000
        print(f"'{funcion.__name__}' {transcurrido:.2f} ms")
        return result
        
    return timed
    

def prueba():
    @timeit
    def lento():
        time.sleep(1)
    print("Al usar sleep(1), deberia de dar 1000ms")
    lento()


if __name__ == '__main__':
    prueba()
