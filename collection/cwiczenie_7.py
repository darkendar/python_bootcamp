napis = input("Napisz zdanie: ")
sam = 0
SAMOGLOSKI = ["a", "e", "i", "o", "u", "y"]

#for i in napis.lower():
#   for j in SAMOGLOSKI:
#       if i == j:
#           sam += 1

for i in napis.lower():
    if i in "aeiouy":
        sam += 1

print(f"W napisie jest {sam} samoglosek")