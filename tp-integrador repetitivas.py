#TP integrador – Repetitivas- Condicionales y Secuenciales.


#Ejercicio 1— “Caja del Kiosco” ###########################

nombre_del_cliente = input("Ingrese su nombre: ")

while not nombre_del_cliente.isalpha():
    print("Error: solo se permiten letras.")
    nombre_del_cliente = input("ingrese su nombre: ")


cant_productos = input("Ingrese la cantidad de productos: ")

while not cant_productos.isdigit() or int(cant_productos) <= 0:
    print("Error: Ingrese un número entero mayor que 0.")
    cant_productos = input("ingrese la cantidad de productos: ")

cant_productos = int(cant_productos)

#variables antes del for para que conserven el valor acumulado cada vuelta
total_sin_descuentos = 0
total_con_descuentos = 0
ahorro_total = 0

for i in range(cant_productos):
    print("Producto", i+1)
    precio = input("Precio: ")

    while not precio.isdigit():
        print("Error: Ingrese un precio válido.")
        precio = input("Precio: ")

    precio = int(precio)

    total_sin_descuentos += precio

    descuento = input("¿Tiene descuento? (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: Ingrese S o N.")
        descuento = input("Descuento (S/N): ").lower()

    if descuento == "s":
       precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuentos += precio_con_descuento
    ahorro_total += precio - precio_con_descuento

promedio = float(total_con_descuentos / cant_productos)

print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#----------------------------------------------------------
#----------------------------------------------------------

# Ejercicio 2 — “Acceso al Campus y Menú Seguro” ##########

correct_user = "alumno"
correct_pw = "python123"

acceso_concedido = False
intentos = 0


# LOGIN

while not acceso_concedido and intentos < 3:

    intentos += 1

    print(f"Intento {intentos}/3")

    user = input("Usuario: ")
    pw = input("Clave: ")

    if user == correct_user and pw == correct_pw:

        acceso_concedido = True
        print("Acceso concedido")

    else:

        print("Error: credenciales inválidas.")


# CUENTA BLOQUEADA

if not acceso_concedido:

    print("Cuenta bloqueada")


# MENU

if acceso_concedido:

    opcion = 0

    while opcion != 4:

        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opción: ")

        # Validar que sea un número
        while not opcion.isdigit():

            print("Error: ingrese un número válido.")

            opcion = input("Opción: ")

        opcion = int(opcion)

        # Validar que esté entre 1 y 4
        while opcion < 1 or opcion > 4:

            print("Error: opción fuera de rango.")

            opcion = input("Opción: ")

            # Volver a validar que sea un número
            while not opcion.isdigit():

                print("Error: ingrese un número válido.")

                opcion = input("Opción: ")

            opcion = int(opcion)

        # ACCIONES DEL MENU

        match opcion:

            case 1:

                print("Inscripto")

            case 2:

                new_pw = input("Nueva clave: ")

                while len(new_pw) < 6:

                    print("Error: la clave debe contener un mínimo de 6 caracteres.")

                    new_pw = input("Nueva clave: ")

                confirmacion = input("Confirme su nueva clave: ")

                while new_pw != confirmacion:

                    print("Error: las claves no coinciden.")

                    confirmacion = input("Confirme nueva clave: ")

                correct_pw = new_pw

                print("Clave cambiada correctamente.")

            case 3:

                print("¡Vas por buen camino!")

            case 4:

                print("Saliendo...")

#----------------------------------------------------------
#----------------------------------------------------------

#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)"

#variables
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

nombre_operador = input("Ingresa nombre del operador: ")

while not nombre_operador.isalpha():
    print("ERROR: solo se permiten letras")
    nombre_operador = input("Ingrese nombre del operador: ")

# MENU

opcion = 0

while opcion != 5:
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("seleccione una opcion: ")

    while not opcion.isdigit():
        print("ERROR: debe ingresar un numero.")
        opcion = input("seleccione una opcion: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 5:
        print("ERROR: opcion invalida.")
        opcion = input("seleccione una opcion: ")

        while not opcion.isdigit():
            print("ERROR: debe ingresar un numero.")
            opcion = input("seleccione una opcion: ")

        opcion = int(opcion)

    if opcion == 1:
        dia = input("Ingrese el dia (1=lunes, 2=martes): ")

        while not dia.isdigit():
            print("ERROR: debe ingresar un numero")
            dia = input("ingrese el dia (1=lunes, 2=martes): ")

        dia = int(dia)

        while dia < 1 or dia > 2:
            print("ERROR: opcion invalida")
            dia = input("ingrese el dia 1=lunes, 2=martes): ")

            while not dia.isdigit():
                print("ERROR: debe ingresar un numero.")
                dia = input("ingrese el dia (1=lunes, 2=martes): ")

            dia =int(dia)

        nombre_paciente = input("ingrese nombre del paciente: ")

        while not nombre_paciente.isalpha():
            print("ERROR: solo se permiten letras.")
            nombre_paciente = input("ingrese nombre del paciente: ")

        if dia == 1:
            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                print("ERROR: el paciente ya tiene turno ese dia.")
            else:
                if lunes1 == "":
                    lunes1 = nombre_paciente
                    print("turno reservado correctamente.")

                elif lunes2 == "":
                    lunes2 = nombre_paciente
                    print("turno reservado correctamente")

                elif lunes3 == "":
                    lunes3 = nombre_paciente
                    print("turno reservado correctamente")

                elif lunes4 == "":
                    lunes4 = nombre_paciente
                    print("turno reservado correctamente")

                else:
                    print("no hay turnos disponibles para el lunes")

        elif dia == 2:
            if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                print("ERRROR: el paciente ya tiene turno ese dia")

            else:
                if martes1 == "":
                    martes1 = nombre_paciente
                    print("turno reservado correctamente")

                elif martes2 == "":
                    martes2 = nombre_paciente
                    print("turno reservado correctamente")

                elif martes3 == "":
                    martes3 = nombre_paciente
                    print("turno reservado correctamente")

                else:
                    print("no hay turnos disponibles para el martes.")

    elif opcion == 2 :
        dia = input("ingrese el dia (1=lunes, 2=martes): ")

        while not dia.isdigit():
            print("ERROR: debe ingresar un numero.")
            dia = input("ingrese el dia (1=lunes, 2=martes): ")

        dia = int(dia)

        while dia < 1 or dia > 2:
            print("ERROR: opcion invalida.")
            dia = input("ingrese el dia (1=lunes, 2=martes): ")

            while not dia.isdigit():
                print("ERROR: debe ingresar un numero.")
                dia = input("ingrese el dia (1=lunes, 2=martes): ")

            dia = int(dia)

        nombre_paciente = input("ingrese nombre del paciente: ")

        while not nombre_paciente.isalpha():
            print("ERROR: solo se permiten letras.")
            nombre_paciente = input("ingrese nombre del paciente: ")

        if dia == 1:
            if nombre_paciente == lunes1:
                lunes1 = ""
                print("turno cancelado correctamente.")

            elif nombre_paciente == lunes2:
                lunes2 = ""
                print("turno cancelado correctamente.")

            elif nombre_paciente == lunes3:
                lunes3 = ""
                print("turno cancelado correctamente.")

            elif nombre_paciente == lunes4:
                lunes4 = ""
                print("turno cancelado correctamente.")

            else:
                print("ERROR: el paciente no tiene turno ese dia.")

        elif dia ==2:
            if nombre_paciente == martes1:
                martes1 = ""
                print("turno cancelado correctamente.")

            elif nombre_paciente == martes2:
                martes2 = ""
                print("turno cancelado correctamente.")

            elif nombre_paciente == martes3:
                martes3 = ""
                print("turno cancelado correctamente.")

            else:
                print("ERROR: el paciente no tiene turno ese dia.")

    elif opcion == 3:
        dia = input("ingrese el dia (1=lunes, 2=martes): ")

        while not dia.isdigit():
            print("ERROR: debe ingresar un numero.")
            dia = input("ingrese el dia (1=lunes, 2=martes): ")

        dia = int(dia)

        while dia < 1 or dia > 2:
            print("ERROR: opcion invalida.")
            dia = input("ingrese el dia (1=lunes, 2=martes): ")

            while not dia.isdigit():
                print("ERROR: debe ingresar un numero.")
                dia = input("ingrese el dia (1=lunes, 2=martes): ")

        dia =int(dia)

        if dia == 1:
            if lunes1 == "":
                print("turno 1: (libre)")
            else:
                print("turno 1:", lunes1)

            if lunes2 == "":
                print("turno 2: (libre)")
            else:
                print("turno 2:", lunes2)

            if lunes3 == "":
                print("turno 3: (libre)")
            else:
                print("turno 3:", lunes3)

            if lunes4 == "":
                print("turno 4: (libre)")
            else:
                print("turno 4:", lunes4)

        elif dia == 2:
            if martes1 == "":
                print("turno 1: (libre)")
            else:
                print("turno 1:", martes1)

            if martes2 == "":
                print("turno 2: (libre)")
            else:
                print("turno 2:", martes2)

            if martes3 == "":
                print("turno 3: (libre)")
            else:
                print("turno 3:", martes3)

    elif opcion == 4:
        ocupados_lunes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        ocupados_martes = 0

        if martes1 != "":
            ocupados_martes += 1

        if martes2 != "":
            ocupados_martes += 1

        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes

        print("Lunes - ocupados:", ocupados_lunes)
        print("Lunes - disponibles:", disponibles_lunes)

        disponibles_martes = 3 - ocupados_martes

        print("Martes - ocupados:", ocupados_martes)
        print("Martes - disponibles:", disponibles_martes)

        if ocupados_lunes > ocupados_martes:
            print("El lunes tiene mas turnos ocupados.")

        elif ocupados_martes > ocupados_lunes:
            print("El martes tiene mas turnos ocupados.")

        else:
            print("Ambos dias tienen la misma cantidad de turnos ocupados.")

print("sistema cerrado.")

#----------------------------------------------------------
#----------------------------------------------------------

#Ejercicio 4 — “Escape Room: La Bóveda”

#variables
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

nombre_agente = input("ingrese el nombre del agente: ")

while not nombre_agente.isalpha():
    print("ERROR: solo se permiten letras.")
    nombre_agente = input("ingrese el nombre del agente: ")

forzar_seguido = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print("================================")
    print("        ESCAPE ROOM")
    print("================================")
    print("Agente:", nombre_agente)
    print("Energia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)

    #ACCIONES

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("seleccione una opcion: ")

    while not opcion.isdigit():
        print("ERROR: debe ingresar un numero.")
        opcion = input("seleccione una opcion: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("ERROR: opcion invalida.")
        opcion = input("seleccione una opcion: ")

        while not opcion.isdigit():
            print("ERROR: debe ingresar un numero.")
            opcion = input("seleccione una opcion: ")

        opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguido += 1

        if energia < 40:
            riesgo = input("elegi un numero del 1 al 3: ")

            while not riesgo.isdigit():
                print("ERROR: debe ingresar un numero.")
                riesgo = input("elegi un numero del 1 al 3: ")

            riesgo = int(riesgo)

            while riesgo < 1 or riesgo > 3:
                print("ERROR: opcion invalida.")
                riesgo = input("elegi un numero del 1 al 3: ")

                while not riesgo.isdigit():
                    print("ERROR: opcion invalida.")
                    riesgo = input("elegi un numero del 1 al 3: ")

                riesgo = int(riesgo)

            if riesgo == 3:
                alarma = True
                print("se activo la alarma")

        if forzar_seguido == 3:
            alarma = True
            print("la cerradura se trabo. Se activo la alarma :O!")
        if not alarma:
            cerraduras_abiertas += 1
            print("la cerradura se abrio correctamente")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_seguido = 0

        for paso in range(4):
            print("hackeando... paso", paso + 1)
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("hackeo exitoso. cerradura abierta.")

    elif opcion == 3:
        energia += 15
        tiempo -= 1
        forzar_seguido = 0

        if energia > 100:
            energia = 100
        if alarma:
            energia -= 10

if cerraduras_abiertas == 3:
    print("VICTORIA!")

elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("La alarma bloqueo la boveda")
    print("DERROTA.")

elif energia <= 0 or tiempo <= 0:
    print("DERROTA.")

# Ejercicio 5 — "Escape Room: La Arena del Gladiador"

# CONFIGURACION DEL PERSONAJE

nombre_gladiador = input("Nombre del Gladiador: ")

while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")


# VARIABLES INICIALES

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True


# INICIO DEL COMBATE

print("==============================")
print("     BIENVENIDO A LA ARENA")
print("==============================")


while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador:

        print()
        print("=== NUEVO TURNO ===")
        print(nombre_gladiador, "(HP:", vida_jugador, ")")
        print("Enemigo (HP:", vida_enemigo, ")")
        print("Pociones:", pociones)

        print()
        print("Elige accion:")
        print("1. Ataque Pesado")
        print("2. Rafaga Veloz")
        print("3. Curar")

        opcion = input("Opcion: ")

        while not opcion.isdigit():
            print("Error: Ingrese un numero valido.")
            opcion = input("Opcion: ")

        opcion = int(opcion)

        while opcion < 1 or opcion > 3:
            print("Error: Opcion invalida.")
            opcion = input("Opcion: ")

            while not opcion.isdigit():
                print("Error: Ingrese un numero valido.")
                opcion = input("Opcion: ")

            opcion = int(opcion)


        # ATAQUE PESADO

        if opcion == 1:

            if vida_enemigo < 20:
                danio_final = ataque_pesado * 1.5
                vida_enemigo -= danio_final

                print("¡Golpe Critico!")
                print("¡Atacaste al enemigo por", danio_final, "puntos de daño!")

            else:
                danio_final = ataque_pesado
                vida_enemigo -= danio_final

                print("¡Atacaste al enemigo por", danio_final, "puntos de daño!")


        # RAFAGA VELOZ

        elif opcion == 2:

            print(">> ¡Inicias una rafaga de golpes!")

            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")


        # CURAR

        elif opcion == 3:

            if pociones > 0:
                vida_jugador += 30
                pociones -= 1

                if vida_jugador > 100:
                    vida_jugador = 100

                print("¡Te curaste 30 puntos de vida!")

            else:
                print("¡No quedan pociones!")


        # VERIFICAR SI EL ENEMIGO SIGUE VIVO

        if vida_enemigo > 0:

            print(">> ¡El enemigo contraataca por 12 puntos!")

            vida_jugador -= danio_enemigo

            print("¡El enemigo te ataco por", danio_enemigo, "puntos de daño!")


# FIN DEL JUEGO

if vida_jugador > 0:
    print()
    print("¡VICTORIA!", nombre_gladiador, "ha ganado la batalla.")

else:
    print()
    print("DERROTA. Has caido en combate.")