from random import choice


def pre_print(mas):  # просто принт
    print('-' * 10)
    for i in mas:
        print(*i)
    print('-' * 10)


def getValidMoves(x0, y0):  # возможние варианти хода
    deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    validPositions = []
    for (x, y) in deltas:
        xcandidate = x0 + x
        ycandidate = y0 + y
        if 0 < xcandidate < 8 and 0 < ycandidate < 8:
            validPositions.append([xcandidate, ycandidate])

    return validPositions


def get_empty_list(mas):  # проверка на где на одске ище 0
    svobodnue_kletki = []
    for i in range(8):
        for j in range(8):
            if mas[i][j] != 1:
                svobodnue_kletki.append([i, j])
    return svobodnue_kletki


def menshe_chislo(x0, y0, x1, y1, skolko_raz):

    def konyaka(x0, y0, x1, y1, hod=1, x2= x0 ,y2=y0):
        h[x1][y1] = 2
        vozmohnur_hodu = []
        for i in getValidMoves(x0, y0):
            if h [i[0]] [i[1]] == 0 :
                vozmohnur_hodu.append(i)
            if h[i[0]][i[1]] == 2:
                return hod

        if hod > 6 :
            return konyaka(x2, y2, x1, y1, hod=1)

        if h[x0][y0] != h[x1][y1]:
            f = choice(vozmohnur_hodu)
            return konyaka(f[0], f[1], x1, y1, hod + 1)

    res = []
    for i in range(skolko_raz):
        h = [[0 for j in range(8)] for i in range(8)]
        h[x0][y0] = 1
        res.append(konyaka(x0, y0, x1, y1))

    return res


if __name__ == '__main__':
    print(menshe_chislo(1, 1, 7, 7, 10))
