'''Create a separate asynchronous code to calculate Fibonacci, factorial,
squares and cubic for an input number.
Schedule the execution of this code using asyncio.gather
for a list of integers from 1 to 10.
You need to get four lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same
results but using a multiprocessing library. Time the execution of both
realizations, explore the results, what realization is more effective,
why did you get a result like this.'''
import asyncio

async def squares(n):
    d = (n*n)
    print(f'от числа {n} вот квадрат {d}')

async def cubic (n):
    d =(n*n*n)
    print(f'от числа {n} вот куб {d}')

async def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    print(f'фибаначи {a}')


async def factorial( number):
    f = 1
    for i in range(2, number + 1):
        await asyncio.sleep(1)
        f *= i
    print(f": факториал ({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        *[factorial(i) for i in range(10)],
        *[cubic(i) for i in range(10)],
        *[squares(i) for i in range(10)],
        *[fib(i) for i in range(10)]
    )


if __name__ == '__main__':
    asyncio.run(main())