import math
import random
import numpy

def sort_random():
    generated_numbers = []
    sorted_numbers = []

    for i in range(50):
        num = random.randint(0, 100)
        generated_numbers.append(num)
    print("Random numbers:\n",generated_numbers)

    sort_func = sorted(generated_numbers, reverse=True)
    print("To verify the results:\n",sort_func)

    for j in range(50):
        sorted_numbers.append(max(generated_numbers))
        generated_numbers.remove(max(generated_numbers))
    print("My function:\n",sorted_numbers)

    if sorted_numbers==sort_func:
        print("Numbers are the same - OK")

sort_random()