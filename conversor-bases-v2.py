finish = False
while not finish:
    print("-------------------Conversor de Bases--------------------\n")
    res = str.upper((input("Converter para:\n\n[B]inário\n[O]ctal\n[H]exadecimal\n\n[S]air\n\nR: ")))

    if res == "O" or res == "B" or res == "H":
        print("\n-------------------------Informe-------------------------\n")

        try:
            num = int(input("Digite o Número Decimal: "))
            finish = True

        except ValueError:
            print("\n--------------------------ERRO---------------------------\n")
            print("Digite um número!\n")

    elif res == "S":
        print("\nObrigado por usar este programa! c:")
        finish = True

    else:
        print("---------------------------------------------------------")
        print("\n\nERRO! Tente novamente! c:\n\n")


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


def base(b, a):
    resultados = []
    sair = False
    while not sair:
        inteiro = int(b / a)
        mult = a * inteiro
        resto = b - mult
        b = inteiro
        conversor = abcdef(resto)
        resultados.append(str(conversor))
        if inteiro == 0:
            sair = True
    resultados.reverse()
    return ''.join(resultados)


if res == "B":
    print("\n--------------RESULTADO--------------\n")
    print(f"Binário: {base(num, 2)}")

elif res == "O":
    print("\n--------------RESULTADO--------------\n")
    print(f"Octal: {base(num, 8)}")

elif res == "H":
    print("\n--------------RESULTADO--------------\n")
    print(f"Hexadecimal: {base(num, 16)}")
