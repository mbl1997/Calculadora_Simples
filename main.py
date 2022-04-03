num1 = input('Informe o primeiro numero:')
num2 = input('Informe o segundo numero:')
operacao = input ('Informe a operação (+-*/)')

if operacao == '+':
    resultado = float(num1) + float(num2)
    print(resultado)

elif operacao == '-':
    resultado = float(num1) - float(num2)
    print(resultado)
    
elif operacao == '*':
    resultado = float(num1) * float(num2)
    print(resultado)

elif operacao == '/':
    resultado = float(num1) / float(num2)
    print(resultado)

else:
    print('Operação Invalida... Tente Novamente!')

print('Fim da Operação!')
