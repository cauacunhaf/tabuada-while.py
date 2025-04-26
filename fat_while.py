#contador = num

num = int(input("Digite um numero:"))
fat = 1
cont = num
while cont >=1:
    fat = fat * cont
    cont = cont - 1
print("O fatorial de", num,"e:", fat)

"""
contador = 1

num = int(input("Digite um numero:"))
fat = 1
cont = 1
while cont <=num:
    fat = fat*cont
    cont = cont + 1 #(ou cont +=1)
print("O fatorial de", num,"e:", fat)

"""
