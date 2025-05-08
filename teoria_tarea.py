import numpy as np

def simplex():
    
    tableau = np.array([
        [ 2,   3,  1,  85],   
        [-50, -80, 0,   0]    
    ], dtype=float)

    num_vars = 2 

    while True:
        z_row = tableau[-1, :-1]
        if all(z_row >= 0):
            break  

        col_pivot = np.argmin(z_row)
        rhs = tableau[:-1, -1]
        column = tableau[:-1, col_pivot]

        ratios = np.array([rhs[i] / column[i] if column[i] > 0 else np.inf
                           for i in range(len(rhs))])
        row_pivot = np.argmin(ratios)
        pivot = tableau[row_pivot, col_pivot]

        
        tableau[row_pivot] /= pivot

        
        for i in range(len(tableau)):
            if i != row_pivot:
                factor = tableau[i, col_pivot]
                tableau[i] -= factor * tableau[row_pivot]

    
    print("Tabla final:")
    print(tableau)

    
    x_vals = np.zeros(num_vars)
    for var_index in range(num_vars):
        column = tableau[:-1, var_index]
        if (column == 1).sum() == 1 and (column == 0).sum() == len(column) - 1:
            row = np.where(column == 1)[0][0]
            x_vals[var_index] = tableau[row, -1]

    # x = x1 + 10, y = x2 + 5
    x = x_vals[0] + 10
    y = x_vals[1] + 5
    z = tableau[-1, -1] + 900

    print(f"\nProducción óptima:")
    print(f"Artesanía A (x): {x:.2f} unidades")
    print(f"Artesanía B (y): {y:.2f} unidades")
    print(f"Ganancia total: S/. {z:.2f}")

simplex()
