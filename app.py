try:
    arch = open('prueba.txt','rt')
    print(arch.readline())
except OSError as msj:
    print('Error:',msj)
finally:
    try:
        arch.close()
    except NameError:
        pass
