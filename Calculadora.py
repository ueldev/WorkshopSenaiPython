def calculadora() :
    print("Bem vindo a calculadora em python!!")
    num1 = int(input("Digite um numero: "))
    operacao = input('''
    Selecinione um operador 
    + para somar 
    - para subtrair
    * para multiplicar 
    / para dividir 
    : ''')
    if operacao == "+" :
        print('{}+'.format(num1))
        num2 = int(input("Digite um numero: "))
        res =(num1+num2)
        print('{}+{}={}'.format(num1,num2,res))
    if operacao == "-" :
        print('{}-'.format(num1))
        num2 = int(input("Digite um numero: "))
        res =(num1-num2)
        print('{}-{}={}'.format(num1,num2,res))
    if operacao == "*" :
        print('{}-'.format(num1))
        num2 = int(input("Digite um numero: "))
        res =(num1*num2)
        print('{}*{}={}'.format(num1,num2,res))
    if operacao == "/" :
        print('{}/'.format(num1))
        num2 = int(input("Digite um numero: "))
        res =(num1/num2)
        if num2 == 0 :
            print('{}/0=0'.format(num1))
        
    reiniciar()


def reiniciar() :
    resetar = input('''
    Calcular novamente?
    1 - Para reiniciar 
    2 - para sair 
    :''')
    if resetar == "1" :
        calculadora()
    if resetar == "2" :
        print("Ate mais...")
    if resetar != "1" and resetar != "2" :
        reiniciar()
calculadora()
