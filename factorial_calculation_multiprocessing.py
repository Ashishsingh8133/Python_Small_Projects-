###Real world use case of Multiprocessing
import multiprocessing
import sys
import math
import time

sys.set_int_max_str_digits(100000)

def factorial_number(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")


if __name__=="__main__":
    numbers=[5000,7000,600,8000]


    start_time=time.time()
    with multiprocessing.Pool() as pool:
        results=pool.map(factorial_number,numbers)

    end_time=time.time()

    print(f"The result is :{results}")
    print(f"The time taken {end_time-start_time} seconds ")

