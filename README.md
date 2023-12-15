#### orderData

**Descripción:**
`orderData` es una herramienta sencilla y eficaz desarrollada en Python para procesar y organizar datos de usuarios desde cadenas de texto desestructuradas. Esta utilidad es especialmente útil cuando se tienen datos heterogéneos y se desea almacenarlos de manera ordenada y acumulativa.

**Funcionalidad:**
La herramienta permite al usuario ingresar cadenas de datos que contienen información sobre usuarios, como nombres, identidades, números de teléfono, direcciones, correos electrónicos y afiliaciones. Utilizando expresiones regulares, `orderData` extrae y organiza estos datos en un formato estructurado.

Si algunos datos están ausentes en la cadena de entrada, `orderData` rellena esos campos con "N/A" para mantener la consistencia en el conjunto de datos. Además, la herramienta acumula los datos procesados y los guarda en un archivo Excel (`datos_registro.xlsx`), actuando como una base de datos rudimentaria.

**Utilidad:**
- **Ordenación de Datos:** Facilita la organización de datos desestructurados en un formato tabular, lo que mejora la legibilidad y facilita su uso.
- **Base de Datos Acumulativa:** Permite acumular datos con el tiempo, manteniendo un registro histórico que persiste entre ejecuciones del script.
- **Adaptabilidad:** La herramienta se adapta a diferentes formatos de entrada y maneja la falta de datos de manera elegante.
- **Facilidad de Uso:** Proporciona una interfaz interactiva que permite al usuario ingresar datos de manera intuitiva.

**Instrucciones de Uso:**
1. Ejecuta el script en un entorno de Python.
2. Ingresa las cadenas de datos cuando se solicite, o escribe 'salir' para finalizar.
3. Los datos procesados se acumulan y se guardan en el archivo Excel (`datos_registro.xlsx`).
4. Al volver a ejecutar el script, los datos existentes se cargan, permitiendo una acumulación continua.

`orderData` simplifica el proceso de organización y acumulación de datos, proporcionando una solución práctica para la gestión de información variada y desestructurada.
