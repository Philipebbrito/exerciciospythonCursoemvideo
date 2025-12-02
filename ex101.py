def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f'Com {idade} anos, ainda não pode votar!'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} anos, o voto é opcional!'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos, o voto é obrigatório!'
    else:
        return f'Com {idade} anos, o voto é opcional!'


nasc = int(input('Ano de Nascimento: '))
print(voto(nasc))
