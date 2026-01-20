def add(num1, num2):
    wynik =[]
    if num1 > num2:
        i =0
        while num1 > 0:
            wynik.append(str((num1 % 10 + num2 % 10)))
            num1 //= 10; num2 //= 10
            i += 1
    else:
        i = 0
        while num2 > 0:
            wynik.append(str((num1 % 10 + num2 % 10)))
            num1 //= 10; num2 //= 10
            i += 1
    tekst = ''.join(wynik[::-1])
    return int(tekst) if tekst else 0
