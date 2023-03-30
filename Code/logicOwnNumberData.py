from logicConfigurations import logicConfigurations
import random
import time

class OwnNumberData:
# Ask for user set X
    z1 = logicConfigurations.z1
    z2 = logicConfigurations.z2
    z3 = logicConfigurations.z3
    z4 = logicConfigurations.z4
    z5 = logicConfigurations.z5
    z6 = logicConfigurations.z6
    z7 = logicConfigurations.z7
    x = logicConfigurations.x
    if x is None:
        x = int(input("Insira um valor inteiro para x: "))
        
# Array that makes numbers
    a = random.randint(1, x)
    b = random.randint(1, x)
    c = random.randint(1, x)
    d = random.randint(1, x)
    e = random.randint(1, x)
    f = random.randint(1, x)
# end of array

# Code
    debug = logicConfigurations.debug
    g = 10000+a+b+c+d+e+f
    sorry = random.randint(1, 1000)
    code = g+sorry
# Deez things
    y1 = random.randint(1, x)
    y2 = random.randint(1, x)
    y3 = random.randint(1, x)
    y4 = random.randint(1, x)
    y5 = random.randint(1, x)
    y6 = random.randint(1, x)
    supbro1 = x+1-y1
    supbro2 = x+1-y2
    supbro3 = x+1-y3
    supbro4 = x+1-y4
    supbro5 = x+1-y5
    supbro6 = x+1-y6

## LENG ##
    errorUN = f"An error ocourred."
    EN = logicConfigurations.EN
    PT_BR = logicConfigurations.PT_BR
    SPINNNNNNNNNNNNNNN = logicConfigurations.SPINNNNNNNNNNNNNNN
    lenguage = logicConfigurations.lenguage
## Português - Brasil (Brazilian Portuguese, yes i am Brazilian!)
    TID_PTBR_A_resultWrong = f"Boa tentativa! código:{a*2+code} para a letra A"
    TID_PTBR_B_resultWrong = f"Boa tentativa! código:{b*2+code} para a letra B"
    TID_PTBR_C_resultWrong = f"Boa tentativa! código:{c*2+code} para a letra C"
    TID_PTBR_D_resultWrong = f"Boa tentativa! código:{d*2+code} para a letra D"
    TID_PTBR_E_resultWrong = f"Boa tentativa! código:{e*2+code} para a letra E"
    TID_PTBR_F_resultWrong = f"Boa tentativa! código:{f*2+code} para a letra F"
# Certo (Right)
    TID_PTBR_F_resultRight = f"Você ganhou: R$ 5.000!!\nCódigo da vitória é: #{code+f*z2} para a letra F"
    TID_PTBR_A_resultRight = f"Você ganhou: R$ 5.000!!\nCódigo da vitória é: #{code+a*z1} para a letra A"
    TID_PTBR_B_resultRight = f"Você ganhou: R$ 5.000!!\nCódigo da vitória é: #{code+b*z2} para a letra B"
    TID_PTBR_C_resultRight = f"Você ganhou: R$ 5.000!!\nCódigo da vitória é: #{code+c*z2} para a letra C"
    TID_PTBR_D_resultRight = f"Você ganhou: R$ 5.000!!\nCódigo da vitória é: #{code+d*z2} para a letra D"
    TID_PTBR_E_resultRight = f"Você ganhou: R$ 5.000!!\nCódigo da vitória é: #{code+e*z2} para a letra E"
# Printer:
    TID_PTBR_Printer = f"\nos números gerados são:{a, b, c, d, e, f}\ncódigo: #{code+g*z7}\n{time.asctime()}"
# Debug:
    TID_PTBR_Debug = f"\nlíngua selecionada ==== {lenguage}\n4900000000000001 = PT_BR\n4900000000000002 = EN\nNúmeros corretos:\n{supbro1}\n{supbro2}\n{supbro3}\n{supbro4}\n{supbro5}\n{supbro6}"
    TID_PTBR_DebugIsDisabled = f"depuração está: Desativada ({debug})"
## English... some of them LOL :)
    TID_EN_A_resultWrong = f"nice try! code:{a*2+code} for A"
    TID_EN_B_resultWrong = f"nice try! code:{b*2+code} for B"
    TID_EN_C_resultWrong = f"nice try! code:{c*2+code} for C"
    TID_EN_D_resultWrong = f"nice try! code:{d*2+code} for D"
    TID_EN_E_resultWrong = f"nice try! code:{e*2+code} for E"
    TID_EN_F_resultWrong = f"nice try! code:{f*2+code} for F"
# Right
    TID_EN_A_resultRight = f"You win U$1,000!!\ncode for win is: #{code+a*z1} for a"
    TID_EN_B_resultRight = f"You win U$1,000!!\ncode for win is: #{code+b*z2} for b"
    TID_EN_C_resultRight = f"You win U$1,000!!\ncode for win is: #{code+c*z3} for c"
    TID_EN_D_resultRight = f"You win U$1,000!!\ncode for win is: #{code+d*z4} for d"
    TID_EN_E_resultRight = f"You win U$1,000!!\ncode for win is: #{code+e*z5} for e"
    TID_EN_F_resultRight = f"You win U$1,000!!\ncode for win is: #{code+f*z6} for f"
# Printer:
    TID_EN_Printer = f"\nthe generated numbers are:{a, b, c, d, e, f}\ncode: #{code+g*z7}\n{time.asctime()}"
# Debug:
    TID_EN_Debug = f"\nlenguage ==== {lenguage}\n4900000000000001 = PT_BR\n4900000000000002 = EN\nNumbers that needs to be correct:\n{supbro1}\n{supbro2}\n{supbro3}\n{supbro4}\n{supbro5}\n{supbro6}"
    TID_EN_DebugIsDisabled = f"debug is: {debug}"
# SPINNNNNNNNNNNNNNN
    TID_SPINNNNNNNNNNNNNNN_Printer = f"SPINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN :{a, b, c, d, e, f}"
    
# Winner and loser!
# a
    if not a == supbro1:
        if lenguage == PT_BR:
            print(TID_PTBR_A_resultWrong)            
        if lenguage == EN:
            print(TID_EN_A_resultWrong)
    else:
        if lenguage == PT_BR:
            print(TID_PTBR_A_resultRight)
        if lenguage == EN:
            print(TID_PTBR_A_resultRight)
# b
    if not b == supbro2:
        if lenguage == PT_BR:
            print(TID_PTBR_B_resultWrong)
        if lenguage == EN:
            print(TID_EN_B_resultWrong)
    else:
        if lenguage == PT_BR:
            print(TID_PTBR_B_resultRight)
        if lenguage == EN:
            print(TID_EN_B_resultRight)
# c
    if not c == supbro3:
        if lenguage == PT_BR:
            print(TID_PTBR_C_resultWrong)
        if lenguage == EN:
            print(TID_EN_C_resultWrong)
    else:
        if lenguage == PT_BR:
            print(TID_PTBR_C_resultRight)
        if lenguage == EN:
            print(TID_EN_C_resultRight)
# d
    if not d == supbro4:
        if lenguage == PT_BR:
            print(TID_PTBR_D_resultWrong)
        if lenguage == EN:
            print(TID_EN_D_resultWrong)
    else:
        if lenguage == PT_BR:
            print(TID_PTBR_D_resultRight)
        if lenguage == EN:
            print(TID_EN_D_resultRight)
# e
    if not e == supbro5:
        if lenguage == PT_BR:
            print(TID_PTBR_E_resultWrong)
        if lenguage == EN:
            print(TID_EN_E_resultWrong)
    else:
        if lenguage == PT_BR:
            print(TID_PTBR_E_resultRight)
        if lenguage == EN:
            print(TID_EN_E_resultRight)
# f
    if not f == supbro6:
        if lenguage == PT_BR:
            print(TID_PTBR_F_resultWrong)
        if lenguage == EN:
            print(TID_EN_F_resultWrong)
    else:
        if lenguage == PT_BR:
            print(TID_PTBR_F_resultRight)
        if lenguage == EN:
            print(TID_EN_F_resultRight)
# Printer
    if lenguage == PT_BR:
        print(TID_PTBR_Printer)
    if lenguage == EN:
        print(TID_EN_Printer)
    if lenguage == SPINNNNNNNNNNNNNNN:
        print(TID_SPINNNNNNNNNNNNNNN_Printer)
# Debug:
    if lenguage == PT_BR:
        if debug == True:
            print(TID_PTBR_Debug)
        else:
            print(TID_PTBR_DebugIsDisabled)
    if lenguage == EN:
        if debug == True:
            print(TID_EN_Debug)
        else:
            print(TID_EN_DebugIsDisabled)
# END
    time.sleep(9999999)
# ABSOLUTE END

