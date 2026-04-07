# 3. Decorators: Create a decorator that logs the execution time of a function and use it to decorate a function of your choice.

import time

# Decorator
def log_execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start:.7f} seconds")
    return wrapper


# Function using decorator
@log_execution_time
def my_function():
    time.sleep(2)
    print("Function is running")


def main():
    my_function()

if __name__=="__main__":
    main()