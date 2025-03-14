def calcularValidade(diaFabr, mesFabr, anoFabr, validade):
    lista_mes31 = [1, 3, 5, 7, 8, 10, 12]
    lista_mes30 = [4, 6, 9, 11]

    if anoFabr % 4 == 0:
        ano_bissexto = True
    else:
        ano_bissexto = False

    if mesFabr > 12 or mesFabr < 0:
        return ("Erro! O mês deve estar entre 1 e 12")
    elif mesFabr in lista_mes31 and diaFabr > 31:
        return ("Erro! O mês escolhido tem apenas 31 dias")
    elif mesFabr in lista_mes30 and diaFabr > 30:
        return ("Erro! O mês escolhido tem apenas 30 dias")
    elif ano_bissexto and mesFabr == 2 and diaFabr > 29:
        return ("Erro! O mês escolhido tem apenas 29 dias")
    elif not ano_bissexto and mesFabr == 2 and diaFabr > 28:
        return ("Erro! O mês escolhido tem apenas 28 dias")

    dt_validade = diaFabr + validade

    if mesFabr == 2:
        if ano_bissexto == True:
            if dt_validade > 29:
                dt_validade -= 29
                mesFabr += 1
        else:
            if dt_validade > 28:
                dt_validade -= 28
                mesFabr += 1
    if mesFabr in lista_mes31:
        while dt_validade > 31:
            dt_validade -= 31
            mesFabr += 1
    if mesFabr in lista_mes30:
        while dt_validade > 30:
            dt_validade -= 30
            mesFabr += 1

    while mesFabr > 12:
        mesFabr -= 12
        anoFabr += 1

    return (f"{dt_validade}/ {mesFabr}/ {anoFabr}")