brands = []

while True:
    print("enter brand number"+str(len(brands)+1)+"(or simply enter nothing to exit)")
    brand = input()
    if brand == '':
        break
    else:
        brands = brands+[brand]

print("The registered brands for this program are: ")

for name in brands:
    print(name)