'''count_lines(name) function that reads an input file and counts the number
of lines in it (hint: file.readlines() does most of the work for you, and `len` does the rest)

count_chars(name) function that reads an input file and counts the
 number of characters in it (hint: file.read() returns a single string)

test(name) function that calls both counting functions with a given input file­name.
 Such a filename generally might be passed-in, hard-coded, input with raw_input, or pulled from a
  command-line via the sys.argv list; for now, assume it’s a passed-in function argument.'''

import sys



def count_lines(name):
    count = len(open(name, 'r').readlines(  ))
    return count

def count_chars (name):
    count_1 = len(open(name, 'r').read(  ))
    return count_1

def test (name_fail):
    return count_chars(name_fail), count_lines(name_fail)

if __name__ == '__main__':
    print(sys.argv)
    print(test(sys.argv[1]))

