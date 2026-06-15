import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"Time taken: {end-start} seconds")
        return result
    return wrapper
@timer
def countToMillion():
    for i in range(1_000_000):
        pass
countToMillion()