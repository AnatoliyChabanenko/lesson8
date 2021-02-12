def sum_of_digits(digit_string: str) -> int:
    if digit_string == '' :
        return 0
    if digit_string != '':
        return int(digit_string[0])+ int(sum_of_digits(digit_string[1:]))
    else:
        raise ValueError












if __name__ == '__main__':
    print(sum_of_digits('4332'))
    print(sum_of_digits('3938'))
