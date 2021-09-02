print("------------------Conversor de Bases------------------\n")

res = str(input("Converter para:\n\n[B]inário\n[O]ctal\n[H]exadecimal\n\nR: "))
print("\n-------------------------Informe-------------------------")
num = int(input("\nDigite o Número Decimal: "))


def abcdef(x):
    if x == 10:
        x = "a"
    elif x == 11:
        x = "b"
    elif x == 12:
        x = "c"
    elif x == 13:
        x = "d"
    elif x == 14:
        x = "e"
    elif x == 15:
        x = "f"
    return x


if res == "H":
    resultadosHex = []
    sairHex = False
    while not sairHex:
        inteiroHex = int(num / 16)
        multHex = 16 * inteiroHex
        resto16 = num - multHex
        num = inteiroHex
        conversor = abcdef(resto16)
        resultadosHex.append(conversor)
        if inteiroHex == 0:
            sairHex = True
    resultadosHex.reverse()
    print("\n------------------------Resultado------------------------\n")
    print(f"Hexadecimal: {resultadosHex}")

elif res == "B":
    resultadosBin = []
    sairBin = False
    while not sairBin:
        inteiroBin = int(num / 2)
        multBin = 2 * inteiroBin
        resto2 = num - multBin
        num = inteiroBin
        resultadosBin.append(resto2)
        if inteiroBin == 0:
            sairBin = True
    resultadosBin.reverse()
    print("\n------------------------Resultado------------------------\n")
    print(f"Binário: {resultadosBin}")

elif res == "O":
    resultadosOct = []
    sairOct = False
    while not sairOct:
        inteiroOct = int(num / 8)
        multOct = 8 * inteiroOct
        resto8 = num - multOct
        num = inteiroOct
        resultadosOct.append(resto8)
        if inteiroOct == 0:
            sairOct = True
    resultadosOct.reverse()
    print("\n------------------------Resultado------------------------\n")
    print(f"Octal: {resultadosOct}")
