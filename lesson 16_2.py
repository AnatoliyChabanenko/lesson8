



def named_in_range (start , end  , step= 1):
    for i in range(start, end ,step ):
        yield i

v = named_in_range(10 , 100)

for i in v:
    print(i)