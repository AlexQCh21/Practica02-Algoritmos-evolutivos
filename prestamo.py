import numpy
import pandas as pd

datos = {
    "Estudiantes":["Rosa","David","Elena","Mario","Paula"],
    "prestamo":[7,10,5,12,3]
}

df = pd.DataFrame(datos)

stats = df["prestamo"].describe()


#Calcular el promedio y el máximo de días de préstamo.
df_mayor_8 =  df[df['prestamo'] > 8]


prestamoPromedioDias = stats['mean']
prestamo_mayor_8 = df_mayor_8['Estudiantes'].tolist()


print(f"\nEl prestamo promedio por estudiante fue de S/ {prestamoPromedioDias:.2f}.")
print("Estudiantes que retuvieron el libro más de 8 días fueron:")
for alumno in prestamo_mayor_8: 
    print(f" - {alumno}")





#Filtrar quiénes retuvieron el libro más de 8 días.


