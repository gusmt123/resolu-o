def fibonnaci(num):
    fibonnaci = []
    num1, num2 = 0 , 1
    for x in range(num):
        fibonnaci.append(num1)
        num1, num2 = num2 , num1 + num2
    print(fibonnaci)
    if num in fibonnaci:
        print(f'O número {num} está na sequência')
    else:
        print(f'O número {num} não está na sequência')

fibonnaci(20)