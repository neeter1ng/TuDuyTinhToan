"""
Custom module
"""
# Tệp: fibonacci.py (Hoàn chỉnh)
def fib(n):ZZ
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
if __name__ == "__main__":
    print(fib(10)) 