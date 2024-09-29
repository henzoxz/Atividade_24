# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.
media = 0
cont = 0

while True:
    n = int(input("Digite o Número:"))

    if n ==-1:
        break
    media += n

    cont += 1

    if cont>0:
        media = media/cont

    print(media)