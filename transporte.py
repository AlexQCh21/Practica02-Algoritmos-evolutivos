#Quezada Chorres Cesar Alexander

import numpy as np

#Copisteria bus = 0.10  -  combi = 0.12  -  tren = 0.08
precios = np.array([2.5,3,1.8])

presupuesto = 15


def maxCantidad(max_viajes):
    return max_viajes.max()


max_viajes = np.floor(presupuesto/precios)
cantidad_max = int(max_viajes.max())
indice_max = int(max_viajes.argmax())

#Determinar precio más bajo
precio_min = precios.min()
indice_precio_min = int(precios.argmin())

#Mapeo de copisteria
nombres = ["A", "B", "C"]

#imperimir resultados

print("##############Resultado##############")
for i, nombre in enumerate(nombres):
    print(f"Transporte{nombre}:precio$/{precios[i]:.2f}->puede realizar {int(max_viajes[i])} viajes")


print(f"\nCon S/ {presupuesto:.2f} obtienes la mayor cantidad de copviajes ({cantidad_max}) en {nombres[indice_max]}.")
print(f"El precio más bajo es S/ {precio_min:.2f} en {nombres[indice_precio_min]}.")