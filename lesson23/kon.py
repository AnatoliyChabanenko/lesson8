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


h = [[0 for j in range(8)] for i in range(8)]  # здесь создаю доску


def konyaka(x0, y0, x1, y1, h, hod=1):
    h[x0][y0] = 1
    h[x1][y1] = 2
    vozmohnur_hodu = []
    for i in getValidMoves(x0, y0):
        if i in get_empty_list(h):
            vozmohnur_hodu.append(i)
    if [x1 ,y1] in vozmohnur_hodu:
        vozmohnur_hodu.clear()
        vozmohnur_hodu.append([x1,y1])
    if vozmohnur_hodu == []:
        raise ValueError(f'этот раз неудача{pre_print(h)}')
    if h[x0][y0] == h[x1][y1]:
        return print(hod)
    if h[x0][y0] != h[x1][y1]:
        f = choice(vozmohnur_hodu)
        pre_print(h)
        return konyaka(f[0], f[1], x1, y1, h, hod + 1)


if __name__ == '__main__':
    print(konyaka(3, 4, 6, 6, h))
