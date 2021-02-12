

def reverse(input_str: str) -> str:
    if input_str == '':
        return input_str
    else:
        return reverse(input_str[1:]) + input_str[0]










if __name__ == '__main__':
    print(reverse('hello'))