# 5. Metaclasses: Create a metaclass that enforces a singleton pattern in classes.
# singleton_metaclass.py

import time

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Connecting to database")
        time.sleep(2)


def main():
    db1 = Database()
    db2 = Database()

    print(db1 is db2)   # True


if __name__ == "__main__":
    main()
