numA = int(input("Digite um número:"))
numB = int(input("Digite outro número:"))


for cont in range (0,11):
    multi = numA*numB
    print(f"{numA}x{numB}={multi}")
    numB+=1