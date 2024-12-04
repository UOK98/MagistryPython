ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}
idsuniq = []
for key in ids.keys():
    for element in ids[key]:
        if element not in idsuniq: 
            idsuniq.append(element)

idsuniq = str(idsuniq)
idsuniq = idsuniq.replace('[', '{')
idsuniq = idsuniq.replace(']', '}')
print(idsuniq)