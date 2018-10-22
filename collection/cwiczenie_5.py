x = list(range(10))
y = list(range(10))
print("   ", end="")
for k in range(10):
    print(f"{k:3}", end="")

print()
print()

for i in x:
    print("\n")
    for j in y:
        mnozenie = x[i]*y[j]
        print(f"{mnozenie}\t", end = "")




