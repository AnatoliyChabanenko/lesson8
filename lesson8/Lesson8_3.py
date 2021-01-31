try:
    x = int(input('число :'))
    y = int(input('число 2:'))
    print((x ** 2) / y)
except ValueError:
    print('davai chisla')
except ZeroDivisionError:
    print('ne dili na 0 ')
except:
    print('tu cho ydymal')
