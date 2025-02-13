import time
import random

def decorator_1(func):
    def action(*argumentlarw, **event2):
        starting_time = time.time()  # Record the start time
        natijam1 = func(*argumentlarw, **event2)  # Call the original function
        ending_time = time.time()  # Record the end time
        execute_time = ending_time - starting_time  # Calculate execution time
        print(f"{func.__name__} call executed in {execute_time:.4f} sec")  # Print execution time
        return natijam1  # Return the result of the original function
    return action

@decorator_1
def func():
    print("How many plans do you have?")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)

@decorator_1
def funx(n=2, m=5):
    print("So now what to do?")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

