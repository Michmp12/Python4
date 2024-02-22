#Elaborar un programa en python que permita gestionar una tienda de videojuegos donde se prestan y se devuelven los mismos.
cons_existenciasInt = 5
var_cantidadInt = int(input('Ingrese la cantidad de videojuegos a prestar ->'))
if var_cantidadInt <= 0:
    print ('la cantidad de videojuegos debe ser mayor a 0')
else:
    if var_cantidadInt <= cons_existenciasInt:
     print ('Tu prestamo ha sido aprobado')
     print ('Existencias actuales: ', (cons_existenciasInt-var_cantidadInt))
     enter = input('Presione <Enter> para continuar')
    else:
        print ('No tenemos esa cantidad de videojuegos disponible')
    