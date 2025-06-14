def imprimirArchivo():
    try:
        arch = open('prueba.txt','rt') 
    except OSError as msj:
        print('Error:',msj)
    else:
        print(arch.readlines())
    finally:
        try:
            arch.close()
        except NameError:
            pass

imprimirArchivo()