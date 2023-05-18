nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a media do aluno é {media}')
if 7 > media >= 5:
    print('Aluno esta em RECUPERAÇÃO! ')
elif media < 5:
    print('O Aluno esta REPROVADO! ')
elif media >= 5:
    print('O aluno esta APROVADO!')