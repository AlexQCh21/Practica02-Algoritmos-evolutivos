import pandas as pd

datos = {
    "dias" : ["Lunes","Martes","Miercoles","Jueves","Viernes"],
    "gastos": [4.0, 3.5, 5.0, 4.2, 3.8] 
}


# Objetivo:
# 1. Pasar esa lista a un DataFrame con columna Gasto.
df = pd.DataFrame(datos)
stats = df["gastos"].describe()

# 2. Calcular el gasto total y el gasto medio de la semana.
gastoTotal = df["gastos"].sum()
gastoMedio = df["gastos"].mean()
# 3. Identificar los días en que gastó más que el promedio.
df_gasto_mayor_al_promedio = df[df["gastos"]>gastoMedio]
gasto_mayor_de_la_media= df_gasto_mayor_al_promedio["dias"].tolist()

print("=======================RESULTADOS=======================")
print(f"El gato total en la semana es de : ${gastoTotal:.2f} y el gasto medio es: ${gastoMedio:.2f}")
print("Los días en los que se gastó mas de la media son: ")
for dia in gasto_mayor_de_la_media: 
    print(f" - {dia}")
