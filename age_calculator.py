import datetime  #datetime proporciona clases para manipular fechas y horas de una manera sencilla y eficiente
    
def ageCalculator():
    y = int(input('Ingresa el año de nacimiento: '))
    m = int(input('Ingresa el mes de nacimiento: '))
    d = int(input('Ingresa el día de nacimiento: '))

    actually = datetime.datetime.now().date() # .now() devuelve la fecha y hora actual, .date() extrae solo la parte de la fecha     
    datauser = datetime.date(y, m, d) #datetime.date(y, m, d) crea un objeto con el año y, mes m y día d. Representa la fecha de nacimiento 
    
    age = actually.year - datauser.year  #Calcula la diferencia en años entre el año actual y el año de nacimiento
    if (actually.month, actually.day) < (datauser.month, datauser.day):#Si el día actual es menor que el día de nacimiento, se ajusta months restando 1, ya que aún no ha pasado el aniversario del cumpleaños en el mes actual.
        age -= 1
    
    if actually.month >= datauser.month:
        months = actually.month - datauser.month #Calcula los meses transcurridos entre el mes actual y el mes de nacimiento.
    else:
        months = 12 - (datauser.month - actually.month)
    
    # Ajustar los meses si el día actual es anterior al día de nacimiento
    if actually.day < datauser.day:
        months -= 1

    # Se manejan casos donde los meses podrían ser negativos o donde se necesite ajustar el cálculo debido a diferencias en los días.
    if months < 0:
        months += 12

    print(f'Usted tiene {age} años y {months} meses')

ageCalculator()