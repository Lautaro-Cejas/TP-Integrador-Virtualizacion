#!/usr/bin/env python3
# Empezamos definiendo una función para calcular el porcentaje de notas.

def porcentaje(notas):
    # Sumamos las notas
    total = sum(notas)
    
    promedio = total / len(notas)  # Calculamos el promedio
    
    porcentaje = (promedio / 10) * 100  # Convertimos el promedio a porcentaje
    
    return porcentaje

# Creamos una lista vacía para almacenar las notas
notas = []

# Solicitamos al usuario que ingrese las notas
for i in range(4):  # Definimos la cantidad de notas que el usuario puede ingresar
    nota = int(input(f'Ingrese la nota {i+1}: '))
    if nota <= 10:
        notas.append(nota)
    else:
        print('Nota no válida')

porcentaje_final = porcentaje(notas)

# Usamos una estructura condicional para interpretar el porcentaje
if porcentaje_final >= 70:
    mensaje = 'Aprobado'
elif porcentaje_final >= 40:
    mensaje = 'Debe Mejorar'
else:
    mensaje = 'Reprobado'

# Mostramos los resultados por consola
print(f'Notas Ingresadas: {notas}')
print(f'Porcentaje Final: {porcentaje_final} %')
print(f'Estado: {mensaje}')