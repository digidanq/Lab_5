import f_mat

x = 4
print(f"Kwadrat liczby {x}: {f_mat.kwadrat(x)}")

# Test funkcji szescian
x = 3
print(f"Sześcian liczby {x}: {f_mat.szescian(x)}")

# Test funkcji dodaj
a, b = 5, 7
print(f"Suma {a} i {b}: {f_mat.dodaj(a, b)}")



# Zdanie 9

print("Import całego modułu:")
print(f"Kwadrat liczby 10: {f_mat.kwadrat(10)}")
print(f"Sześcian liczby 3: {f_mat.szescian(3)}")
print(f"Suma liczb 10 i 5: {f_mat.dodaj(10, 5)}")

from f_mat import kwadrat, szescian, dodaj

print("\nImport wybranych funkcji:")
print(f"Kwadrat liczby 10: {kwadrat(10)}")
print(f"Sześcian liczby 3: {szescian(3)}")
print(f"Suma liczb 10 i 5: {dodaj(10, 5)}")
