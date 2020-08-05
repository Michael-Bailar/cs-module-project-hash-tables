# Your code here
import math
import random
import time
start_time = time.time()

# not in use
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

#fill the cache with the possible values
cache = {}
def populate_cache(x1, x2, y1, y2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            v = math.pow(x, y)
            v = math.factorial(v)
            v //= (x + y)
            v %= 982451653
            cache[f"{x}_{y}"] = v
#set the range
populate_cache(2, 14, 3, 6)


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    return cache[f"{x}_{y}"]
               



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

print("Script complete in %.2f seconds." % (time.time() - start_time))