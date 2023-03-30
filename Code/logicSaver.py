from logicConfigurations import logicConfigurations


class logicSaver:
# Language:
    lenguage = input("Lenguage: from PT_BR to EN: ")
    PT_BR = 4900000000000001
    EN = 4900000000000002
    SPINNNNNNNNNNNNNNN = 4900000000000003
# explaining what is z's
    print('z1 -> z6 is 10 numbers and z7 is 15 or 20 numbers')
# z1 -> z6 = codes for numbers generated for wins
    z1 = input("Digite um número grande para z1[10 números]: ")
    z2 = input("Digite um número grande para z2[10 números]: ")
    z3 = input("Digite um número grande para z3[10 números]: ")
    z4 = input("Digite um número grande para z4[10 números]: ")
    z5 = input("Digite um número grande para z5[10 números]: ")
    z6 = input("Digite um número grande para z6[10 números]: ")
# Last Code
    z7 = input("Digite um número grande para z7 [15 ou 20 números]: ")
# X = number for randint
    x = input("Digite um número: ")
    debug = input("Digite uma float, entre True e False: ")
    with open('logicConfigurations.py', 'w') as file:
        file.write(f'#from logicLenguage import logicLenguage\nclass logicConfigurations:\n    EN = {EN}\n    PT_BR = {PT_BR}\n    SPINNNNNNNNNNNNNNN = {SPINNNNNNNNNNNNNNN}\n    lenguage = {lenguage}\n    z1 = {z1}\n    z2 = {z2}\n    z3 = {z3}\n    z4 = {z4}\n    z5 = {z5}\n    z6 = {z6}\n    z7 = {z7}\n    debug = {debug}\n    x = {x}\n')
