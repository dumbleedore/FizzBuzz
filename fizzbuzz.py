def fizzbuzz(colecao):
    fizz = 0
    buzz = 0
    fizzbuzzcont = 0
    for numero in colecao:
        if numero % 5 == 0 and numero % 3 == 0:  # Caso o número seja divisível por ambos, retorna "FizzBuzz"
            fizzbuzzcont = fizzbuzzcont + 1
            print('fizzbuzz')
        elif numero % 3 == 0:  # Para múltiplos de 3, retorna "Fizz"
            fizz = fizz + 1
            print('fizz')
        elif numero % 5 == 0:  # Para múltiplos de 5, retorna "Buzz"
            buzz = buzz + 1
            print('buzz')

        else:
            print(numero)
    print("." * 30)
    print(f'resumo\n{fizz} fizz\n{buzz} buzz\n{fizzbuzzcont} fizzbuzz')
    print("." * 30)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Coleção
# Utilização da função
fizzbuzz(lista)
