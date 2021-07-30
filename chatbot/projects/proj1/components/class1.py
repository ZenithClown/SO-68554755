from ....utils.abc import hello as a
from ..utils.data_process import hello as b

def super_hello():
    print(f"Executed: {a()}")
    print(f"Executed: {b()}")
    return "I'm from class1.py"