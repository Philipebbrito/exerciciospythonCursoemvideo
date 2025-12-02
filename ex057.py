
sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, favor informar o Sexo [M/F]: ')).strip().upper()[0]
 
print(f'Sexo {sexo} registrado com sucesso!')