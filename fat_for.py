num = int(input("Digite um numero:"))
fat = 1
for cont in range (1, num+1, 1):
    fat = fat*cont
print("O fatorial de", num,"e:", fat)