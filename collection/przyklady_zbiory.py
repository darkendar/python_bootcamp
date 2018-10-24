zbior_a = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}
zbior_a.add(1)
zbior_a.add(7)
print(zbior_a)

lista = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(set(lista))

a = {1, 2, 3, 4}
b = {4, 5, 6, 7}

print("Suma a+b", a | b)
print("Róznica a-b", a - b)
print("Róznica b-a", b - a)
print("Iloczyn a&b", a & b)
print("Różnica symetryczna", a ^ b)

x = {49, 81, 50, 20}
y = set(range(1, 100, 2))

print(x&y)