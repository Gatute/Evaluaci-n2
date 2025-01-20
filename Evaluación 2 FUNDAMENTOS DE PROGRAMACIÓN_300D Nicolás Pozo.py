cambio = 40000
DescuentoAcumulado = 0
DescuentosOtorgados = 0
MontoIngresado = 0
MontoTotal = 0
codigo = 0
Ganancia = 0




while True:
    
    while True:
        try:
            
            print("===LISTADO DE ESTACIONAMIENTOS===")
            print("1)Auto: $2.000")
            print("2)Camioneta: $3.000")
            print("3)Camión: $4.000")
            print("4)Motocicleta: $890")
            print("================")
            vehiculo = int(input("Eliga un vehiculo"))
            if vehiculo == 1:
                PrecioFinal = 2000
            elif vehiculo == 2:
                PrecioFinal = 3000
            elif vehiculo == 3:
                PrecioFinal = 4000
            elif vehiculo == 4:
                PrecioFinal = 890
            else:
                print("Error, opción invalida, por favor comience de nuevo")
                break
            MontoIngresado = int(input("Ingrese un monto que quiera añadir entre 1 y 10000 pesos chilenos"))
            if MontoIngresado < 1 and MontoIngresado > 10000:
                print("Error, monto ingresado no valido, por favor comience de nuevo")
                break
            correo = str(input("Ingrese un correo electronico entre 8 y 30 caracteres"))
            if len(correo) < 8:
                print("Error, correo con menos de 8 caracteres, por favor comience de nuevo")
                break
            elif len(correo) > 30:
                print("Error, correo con mas de 30 caracteres, por favor comience de nuevo")
                break
            for i in correo:
                if i == "@":
                    break
                elif i == "a":
                    DescuentoAcumulado = DescuentoAcumulado + 1
                elif i == "z":
                    DescuentoAcumulado = DescuentoAcumulado + 0.3
                elif i == "l":
                    DescuentoAcumulado = DescuentoAcumulado + -0.2
                elif i == "b":
                    DescuentoAcumulado = DescuentoAcumulado + 0.7
                elif i == "m":
                    DescuentoAcumulado = DescuentoAcumulado + 1.3
                elif i == "o":
                    DescuentoAcumulado = DescuentoAcumulado + -0.2
                elif i == "e":
                    DescuentoAcumulado = DescuentoAcumulado + -1
                elif i == "u":
                    DescuentoAcumulado = DescuentoAcumulado + 0.5
                elif i == ".":
                    DescuentoAcumulado = DescuentoAcumulado + -1
                elif i == "x":
                    DescuentoAcumulado = DescuentoAcumulado + 2
                elif i == "y":
                    DescuentoAcumulado = DescuentoAcumulado + 2.1
                elif i == "i":
                    DescuentoAcumulado = DescuentoAcumulado + 6
            ##Monto a pagar con descuento
            PrecioTotal = PrecioFinal - (PrecioFinal * DescuentoAcumulado / 100)

            if DescuentoAcumulado > 0 and DescuentoAcumulado < 90:
                print("Se le ha aplicado un descuento de ", DescuentoAcumulado, "%")
                print("Su cuota a pagar es de $",PrecioTotal)
                DescuentosOtorgados = DescuentosOtorgados + 1
            elif DescuentoAcumulado < 0:
                print("Su cuota a pagar es de $",PrecioFinal)
            elif DescuentoAcumulado > 90:
                print("Tiene un descuento de mayor a 90% por lo cual su estacionamiento es gratis")

                break
            opc = str(input("Desea pagar la cuota?s/n"))
            if opc == "s":    
                if PrecioTotal > MontoIngresado:
                    print("Error, no tiene suficiente dinero para pagar, comience de nuevo")
                elif cambio < 0:
                    opc = str(input("Esta maquina no tiene cambio actualmente, ¿Desea continuar?s/n"))
                    if opc == "s":
                        print("Se ha pagado su cuota")
                        cambio = cambio - (MontoIngresado - PrecioTotal)       
                        Ganancia = Ganancia + PrecioTotal
                        break
                    else:
                        break
                elif MontoIngresado > PrecioTotal:
                    print("Se ha pagado su cuota y le han quedado $", round(MontoIngresado - PrecioTotal,1))
                    cambio = cambio - round(MontoIngresado - PrecioTotal,1)       
                    Ganancia = Ganancia + PrecioTotal
                    break
            else:
                break
        except ValueError:
            print("Valor incorrecto, intente de nuevo")    
    codigo = int(input("Ingrese codigo para apagar la maquina"))
    if codigo != 3312:
        continue
    else:
        break
##

print("Ganancias Finales")
print("Dinero ganado;",Ganancia)
print("Cantidad de descuentos usados:", DescuentosOtorgados)
print("Cambio de la maquina restante",cambio)
