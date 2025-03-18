purchases = {}

with open('purchase_log.txt', 'r') as file:
    for line in file: 
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2: 
            key, value = parts
            purchases[key] = value


for key, value in purchases.items():
    print(f"{key} '{value}'")
