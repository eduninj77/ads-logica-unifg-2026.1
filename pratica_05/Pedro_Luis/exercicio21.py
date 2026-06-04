import os
os.system("clear" if os.name != "nt" else "cls")

presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

presente = 0
faltoso = 0

for i in presencas:
    for v in i:
        if v == "P":
            presente += 1
        else:
            faltoso += 1
print(f"Hoje {presente} pessoas estão presentes.")
print(f"Hoje {faltoso} pessoas faltaram.")