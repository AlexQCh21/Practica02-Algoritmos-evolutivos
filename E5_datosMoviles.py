import numpy as np

# Con un array de NumPy
paquete = np.array([1,2,5,10])
precio = np.array([5,9,20,35])

# calcular el costo por GB para cada paquete.
costo_por_gb = precio/paquete

print(f"El costo por GB es: ")
for p, c in zip(paquete, costo_por_gb):
    print(f"Paquete {p} tiene un costo por GB de {c}")
    
print(f"El paquete mas economico es {paquete[costo_por_gb.argmin()]} con un precio por GB de {costo_por_gb.min()}")