from concurrent.futures.process import ProcessPoolExecutor
import time
from concurrent.futures.thread import ThreadPoolExecutor

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  ]


def is_prime (number):
    if number % 2 == 0:
        return number == 2
    div = 3
    while div * div <= number and number % div != 0 :
        div += 2
    return div * div > number

def process_execution():
    start = time.time()
    with ProcessPoolExecutor(max_workers=5) as executor:
        results  = executor.map(is_prime, NUMBERS)
    for result in  results:
        print(result)
    print('start : {}  Time taken : {}'.format(start, time.time()-start) )

def tread_execution():
    start = time.time()
    with ThreadPoolExecutor (max_workers=5) as executor:
        results  = executor.map(is_prime, NUMBERS)
    for result in  results:
        print(result)
    print('start : {}  Time taken : {}'.format(start, time.time()-start) )


if __name__ == '__main__':
    process_execution()
    tread_execution()