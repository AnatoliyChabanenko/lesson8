key = 'abcdefghijklmnopqrstuvwxyz., '

def caesar (kod, slovo):
    result =''
    if kod > 0 :
        for i in slovo.lower():
            shifr_indeks = (key.index(i) + kod) % 26 # если будут выходить за рамки
            result += key[shifr_indeks]
    else:
        for i in slovo.lower():
            shifr_indeks = abs(key.index(i) - kod ) % 26
            result += key[shifr_indeks]

    return result



if __name__ == '__main__':
    d = caesar(-25 , 'hello')
