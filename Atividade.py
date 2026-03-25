def calculadora():
    while True:
        print("\n menu da calculadora")
        print("1. soma")
        print("2. subtraçao")
        print("3. multiplicaçao")
        print("4. divisao")
        print("5. sair")
        
        opçao = input("\n escolhe uma opçao ai (1-5): ")

        if opçao == '5':
            print("adeus, vlw")
            break 

        if opçao in ['1', '2', '3', '4']:
            
            n1 = float(input("digite o primeiro valor: "))
            n2 = float(input("digite o segundo valor: "))

            if opçao == '1':
                res = n1 + n2
                print("o resultado deu:", res)
            
            elif opçao == '2':
                res = n1 - n2
                print("o resultado deu:", res)
            
            elif opçao == '3':
                res = n1 * n2
                print("o resultado deu:", res)
            
            elif opçao == '4':
                if n2 != 0:
                    res = n1 / n2
                    print("o resultado deu:", res)
                else:
                    print("erro: um da pra dividir por zero!")
        else:
            print("opçao errada! tenta de novo.")

calculadora()