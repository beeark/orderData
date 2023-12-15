import re
import pandas as pd
import pyfiglet

def generar_ascii_art():
    ascii_art = pyfiglet.figlet_format("orderData", font="slant")
    print(ascii_art)
    print("              By Porix")
    print("")

def procesar_cadena(cadena):
    # Definir el patrón regex para extraer la información
    patron = re.compile(r'(.+)? (\d+)? (\d+)? (.+)? ([\w.-]+@\w+\.\w+)? (\w+) \$([\d,]+)?')

    # Buscar coincidencias en la cadena
    coincidencia = patron.match(cadena)

    if coincidencia:
        # Extraer cada grupo de la coincidencia
        nombre_apellido = coincidencia.group(1) or "N/A"
        identidad = coincidencia.group(2) or "N/A"
        celular = coincidencia.group(3) or "N/A"
        direccion = coincidencia.group(4) or "N/A"
        correo = coincidencia.group(5) or "N/A"
        tipo_servicio = coincidencia.group(6) or "N/A"
        costo = coincidencia.group(7) or "N/A"

        # Ajuste por medida numérica solo si el costo está presente
        if costo != "N/A":
            costo = costo + ".000"

        # Si falta el número de identidad, asignar "N/A"
        if identidad == "N/A" and celular != "N/A":
            identidad = "N/A"

        # Crear el DataFrame con los datos organizados
        datos_df = pd.DataFrame([[nombre_apellido, identidad, celular, direccion, correo, tipo_servicio, costo]],
                                columns=['Nombre y Apellido', 'Identidad', 'Celular', 'Dirección', 'Correo Electrónico', 'Tipo de Servicio', 'Costo'])

        return datos_df
    else:
        return None

# Cargar los datos existentes del archivo Excel
try:
    datos_acumulados = pd.read_excel('datos_registro.xlsx')
    print("Datos existentes cargados.")
except FileNotFoundError:
    datos_acumulados = pd.DataFrame(columns=['Nombre y Apellido', 'Identidad', 'Celular', 'Dirección', 'Correo Electrónico', 'Tipo de Servicio', 'Costo'])
    print("Archivo de datos no encontrado. Se creará uno nuevo.")

# Mostrar la interfaz de ventana interna
generar_ascii_art()

# Solicitar entrada al usuario y procesar la cadena
while True:
    cadena_datos = input("Ingrese datos a procesar (o 's' para terminar) > ")

    if cadena_datos.lower() == 's':
        break

    resultado = procesar_cadena(cadena_datos)

    if resultado is not None:
        # Concatenar el resultado al DataFrame acumulado
        datos_acumulados = pd.concat([datos_acumulados, resultado], ignore_index=True)
        print("")
        print("Datos procesados y agregados al registro.")
        print("")
    else:
        print("No se pudo procesar la cadena. Asegúrate de incluir al menos el nombre y uno de los siguientes: identidad, celular, dirección, correo, tipo de servicio o costo.")

# Guardar el DataFrame acumulado en un archivo Excel
datos_acumulados.to_excel('datos_registro.xlsx', index=False)
print("Registro guardado en 'datos_registro.xlsx'")
