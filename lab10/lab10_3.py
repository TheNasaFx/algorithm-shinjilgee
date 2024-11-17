def potential_function(D):
    return D ** 2  

def shifted_potential_function(D, D0):
    return potential_function(D) - potential_function(D0)

def unit_cost(D, D_prev):
    return potential_function(D) - potential_function(D_prev)

D0 = 0  
D_values = [0, 1, 2, 3, 4]  

for i in range(1, len(D_values)):
    D_prev = D_values[i - 1]
    D_curr = D_values[i]
    
    original_cost = unit_cost(D_curr, D_prev)
    shifted_cost = shifted_potential_function(D_curr, D0) - shifted_potential_function(D_prev, D0)
    
    print(f"Original unit cost for transition from D{D_prev} to D{D_curr}: {original_cost}")
    print(f"Shifted unit cost for transition from D{D_prev} to D{D_curr}: {shifted_cost}")
    print("Are the unit costs equal?", original_cost == shifted_cost)
    print()
