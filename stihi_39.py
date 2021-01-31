
def one_stih(faile_neme = ''):
    with open (faile_neme) as f:
        for line in f:
            yield line



def stihi (*args):
    all_itrerator = []
    for fn in args:
        all_itrerator.append(one_stih(fn))
    ok = True
    while ok:
            for one in all_itrerator:
                try:
                    ret = next(one)
                except:
                    pass
                yield ret





if __name__ == '__main__':

    for line in stihi('stihi_1.txt', 'stihi.txt'):
        print(line)