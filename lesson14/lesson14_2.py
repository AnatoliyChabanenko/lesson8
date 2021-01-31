from functools import wraps
my_list1= ['pepsi', 'BMW']

def bed_world(my_list : list):
    def stop_words(func):
        @wraps(func)
        def do_samsing (*args, **kwargs):
            rezalt = func(*args, **kwargs)
            for i in my_list:
                rezalt = rezalt.replace(i,'*' )
            return rezalt

        return do_samsing

    return stop_words


@bed_world(my_list1)
def create_slogan(name) :
    return f" {name} drinks pepsi in his brand new BMW!"
print(create_slogan('sonya'))