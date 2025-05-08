#Quezada Chorres Cesar Alexander

import numpy as np

#Copisteria A = 0.10  -  B = 0.12  -  C = 0.08
precios = np.array([0.10,0.12,0.08])

presupuesto = 8


def maxCantidad(max_copias):
    return max_copias.max()


max_copias = np.floor(presupuesto/precios)
cantidad_max = int(max_copias.max())
indice_max = int(max_copias.argmax())

#Determinar precio más bajo
precio_min = precios.min()
indice_precio_min = int(precios.argmin())

#Mapeo de copisteria
nombres = ["A", "B", "C"]

#imperimir resultados

print("##############Resultado##############")
for i, nombre in enumerate(nombres):
    print(f"Copisteria{nombre}:precio$/{precios[i]:.2f}->puede comprar {int(max_copias[i])} copias")


print(f"\nCon S/ {presupuesto:.2f} obtienes la mayor cantidad de copia ({cantidad_max}) en la copisteria {nombres[indice_max]}.")
print(f"El precio más bajo es S/ {precio_min:.2f} en la copisteria{nombres[indice_precio_min]}.")