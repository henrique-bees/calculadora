# calculadora em python
print('''Para calcular escreva a operação separando os termos com espaço
exemplo: 5 * 5
use o sinal padrão para cada operação matemática simples
digite "sair" para parar o programa
''')
while True:
    c = input('calcule: ')
    nt = c.split(' ')
    lista = [str(x) for x in nt]
    print(lista)

    if lista[0] == 'sair':
        print('desligando')
        quit()
    elif lista[1] == '*':
        m = float(lista[0]) * float(lista[2])
        print(m)
    elif lista[1] == '+':
        m = float(lista[0]) + float(lista[2])
        print(m)
    elif lista[1] == '-':
        m = float(lista[0]) - float(lista[2])
        print(m)
    elif lista[1] == '/':
        m = float(lista[0]) / float(lista[2])
        print(m)
    else:
        print('houve um erro')
print()
