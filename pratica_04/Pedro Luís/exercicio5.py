import os
os.system("clear" if os.name != "nt" else "cls")

frutas = ["maçã", "banana", "uva", "pera"]
piton = "Python"

for i in frutas:
    print(f"Eu gosto de {i}.")

print(f"{len(frutas)} foram percorridas.\n")

for i in piton:
    print(i)