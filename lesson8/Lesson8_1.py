def create_contact():
    return {
        'name': input('Name?'),
        'fullname': input('Full name?'),
        'state': input('Oblast?'),
        'phone': input('Phone?')
    }


def search_name(name, ):
    return [element for element in phone_book if element['name'] == name]


def serch_fullname(fullname):
    return [element for element in phone_book if element['fullname'] == fullname]


def serch_state(state):
    return [element for element in phone_book if element['state'] == state]


def serch_phone(phone):
    return [element for element in phone_book if element['phone'] == phone]


def print_contact(dat):
    for u in dat:
        for i in u:
            print(f'|{i}: {u[i]}|')


phone_book = [{
    'name': 'tolya',
    'fullname': 'Chabanenko',
    'state': 'Odesska onlast',
    'phone': '0972571036'
}, {
    'name': 'tolya',
    'fullname': 'pip',
    'state': 'niko',
    'phone': '0972571036'
}]

while True:
    a = input(f'c=create new\nsn=search by name\nsf=search by fullname\nss== search by state\nsp=search by phone\n: ')
    if a == 'c':
        new_contact = create_contact()
        phone_book.append(new_contact)
    elif a == 'sn':
        c = input('search by name? ')
        print_contact(search_name(c))
    elif a == 'sf':
        c = input('search by fullname? ')
        print_contact(serch_fullname(c))
    elif a == 'ss':
        c = input('search by state? ')
        print_contact(serch_state(c))
    elif a == 'sp':
        c = input('search by phone? ')
        print_contact(serch_phone(c))
    else:
        print(phone_book)
