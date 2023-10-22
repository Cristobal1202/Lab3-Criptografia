# Nombre del archivo de entrada y salida
archivo_entrada = "rockyou.txt"
archivo_salida = "rockyou_mod.dic"

# Abre el archivo de entrada en modo lectura y el archivo de salida en modo escritura
with open(archivo_entrada, "r", encoding="latin-1") as entrada, open(archivo_salida, "w") as salida:
    contraseñas_modificadas = 0  # Contador para contraseñas modificadas

    # Recorre cada línea en el archivo de entrada
    for linea in entrada:
        # Elimina espacios en blanco al principio y al final de la línea
        linea = linea.strip()

        # Verifica si la línea comienza con una letra
        if linea and linea[0].isalpha():
            # Reemplaza la primera letra por su versión en mayúscula y agrega "0" al final
            contraseña_modificada = linea[0].upper() + linea[1:] + "0"

            # Escribe la contraseña modificada en el archivo de salida
            salida.write(contraseña_modificada + "\n")

            # Incrementa el contador de contraseñas modificadas
            contraseñas_modificadas += 1

# Imprime la cantidad de contraseñas en el archivo modificado
print(f"Se han modificado {contraseñas_modificadas} contraseñas.")

# Cierra los archivos
entrada.close()
salida.close()
