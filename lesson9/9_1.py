def write_to (file_name, mydict):
    with open (file_name,'a') as file:
        file.write(mydict)

def read_file (file_name):
    with open(file_name) as file:
        print(file.read())
if __name__ == '__main__':
    write_to ('my_file.txt', 'dfdfs')
    read_file('my_file.txt')
