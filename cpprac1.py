# -----------------------------------
# Declaring local arrayList
# -----------------------------------
vec1 = [5, 1, 7, 4, 9]
vec2 = [6, 8, 2, 5, 4, 3, 1]

# -----------------------------------
# Declaring join functions
# -----------------------------------
def full_outer_join():
    salida = []
    # Getting unique elements from both vectors
    unique_elements = set(vec1) | set(vec2)
    for element in unique_elements:
        if element in vec1 and element in vec2:
            salida.append((element, element))  # Matching elements
        elif element in vec1:
            salida.append((element, None))  # vec1 element with no match in vec2
        else:
            salida.append((None, element))  # vec2 element with no match in vec1
    return salida

def right_join():
    salida = []
    # Iterate over elements in vec2
    for element in vec2:
        if element in vec1:
            salida.append((element, element))  # Matching elements
        else:
            salida.append((None, element))  # vec2 element with no match in vec1
    return salida

# -----------------------------------
# Executing join functions
# -----------------------------------
print("Full Outer Join:")
print(full_outer_join())
print('')

print("Right Join:")
print(right_join())
print()
