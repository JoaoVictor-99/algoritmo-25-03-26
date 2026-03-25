def resumo(notas):
    soma = 0

    for n in notas:
        soma = soma + n

    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)

    print("soma:", soma)
    print("media:", media)
    print("maior:", maior)
    print("menor:", menor)

lista = [7, 8, 6, 9, 10]
resumo(lista)