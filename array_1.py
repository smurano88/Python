meses =[ "¡Hasta pronto!", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes = 0
while mes != -1:
    mes = int(input(("Dime el número del mes (entre el 1 y el 12) y te daré su nombre. -1 si quieres salir ")))
    if mes >= 1 and mes <= 12:
            print (meses[mes])
    elif mes == -1:
        print (meses[0])
        break
    else:
        print("ERROR")
        continue

