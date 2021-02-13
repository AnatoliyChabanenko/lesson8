import math

n = 102003


def dlina_chisla(chislo, skolko_raz=0, _flag = 0):
    if skolko_raz == 0:
        return chislo
    else:
        if chislo% 10 != 0:
            if _flag == 0:
                return dlina_chisla(chislo // 10 + (chislo % 10 * (10 ** int(math.log10(chislo)))), skolko_raz-1 )
            else:
                return dlina_chisla(chislo // 10 + (chislo % 10) * (10 ** int(math.log10(chislo) +_flag)), skolko_raz-1,  _flag =0)

        elif chislo%10 == 0:
            if _flag == 0:
                return dlina_chisla(chislo // 10 + (chislo % 10) * (10 ** int(math.log10(chislo))), skolko_raz -1, +1)
            else:
                return dlina_chisla(chislo // 10 + (chislo % 10) * (10 ** int(math.log10(chislo) +_flag)), skolko_raz-1, _flag+ 1)



if __name__ == '__main__':
    print(dlina_chisla(n,10))
