'''Нет нет на входе число.
Тебе надо например с двигать вправо.
 Значит крайнее надо отрезать и поставить в начало.
 Как числу 59 в начало поставить 2?  Прибавить 200'''
import math

n = 10203


def dlina_chisla(chislo, skolko_raz=0, _flag = 0):
    if skolko_raz == 0:
        return chislo
    else:
        if _flag == 0:
            if chislo % 10 != 0:
                return dlina_chisla(chislo // 10 + (chislo % 10 * (10 ** int(math.log10(chislo)))), skolko_raz - 1)

            elif chislo % 10 == 0:
                return dlina_chisla(chislo // 10 + (chislo % 10) * (10 ** int(math.log10(chislo))), skolko_raz - 1,+1)
        if _flag >= 0:
            return dlina_chisla(chislo // 10 + (chislo % 10) * (10 ** int(math.log10(chislo)+1)), skolko_raz - 1)



if __name__ == '__main__':
    print(dlina_chisla(n,5))
