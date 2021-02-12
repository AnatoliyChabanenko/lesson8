from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    elif looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])


def is_palindrome_2(looking_str: str, index: int = 0) -> bool:
    index_looking = looking_str[index]
    if len(index_looking) <= 1:
        return True
    elif index_looking[0] != index_looking[-1]:
        return False
    return is_palindrome(index_looking[1:-1])

if __name__ == '__main__':
    print( is_palindrome('sassas'))