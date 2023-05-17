baddata = True
while baddata :
    try:
         a = int(input('Введите число: '))
         baddata = False
         secret_number.write(a)
    except ValueError:
        print('Не удалось получить данные!!!')