import re
import pandas as pd

def procesar_cadena(cadena):
    # Definir el patrón regex para extraer la información
    patron = re.compile(r'(.+)? (\d+)? (\d+)? (.+)? ([\w.-]+@\w+\.\w+)? AFILIACIÓN \$([\d,]+)?')

    # Buscar coincidencias en la cadena
    coincidencia = patron.match(cadena)

    if coincidencia:
        # Extraer cada grupo de la coincidencia
        nombre_apellido = coincidencia.group(1) or "N/A"
        identidad = coincidencia.group(2) or "N/A"
        celular = coincidencia.group(3) or "N/A"
        direccion = coincidencia.group(4) or "N/A"
        correo = coincidencia.group(5) or "N/A"
        afiliacion = coincidencia.group(6) or "N/A"
        # Ajuste por medida numérica
        afiliacion = afiliacion + ".000"

        # Crear el DataFrame con los datos organizados
        datos_df = pd.DataFrame([[nombre_apellido, identidad, celular, direccion, correo, afiliacion]],
                                columns=['Nombre y Apellido', 'Identidad', 'Celular', 'Dirección', 'Correo Electrónico', 'Afiliación'])

        return datos_df
    else:
        return None

# Cargar los datos existentes del archivo Excel
try:
    datos_acumulados = pd.read_excel('datos_registro.xlsx')
    print("Datos existentes cargados.")
except FileNotFoundError:
    datos_acumulados = pd.DataFrame(columns=['Nombre y Apellido', 'Identidad', 'Celular', 'Dirección', 'Correo Electrónico', 'Afiliación'])
    print("Archivo de datos no encontrado. Se creará uno nuevo.")

# Solicitar entrada al usuario y procesar la cadena
while True:
    cadena_datos = input("Ingrese la cadena de datos a procesar (o 'salir' para terminar): ")

    if cadena_datos.lower() == 'salir':
        break

    resultado = procesar_cadena(cadena_datos)

    if resultado is not None:
        # Concatenar el resultado al DataFrame acumulado
        datos_acumulados = pd.concat([datos_acumulados, resultado], ignore_index=True)
        print("Datos procesados y agregados al registro.")
    else:
        print("No se pudo procesar la cadena.")

# Guardar el DataFrame acumulado en un archivo Excel
datos_acumulados.to_excel('datos_registro.xlsx', index=False)
print("Registro guardado en 'datos_registro.xlsx'")