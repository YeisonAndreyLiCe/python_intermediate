#map filter reduce
from functools import reduce

l = [x for x in range(50) if x % 5 == 0]

ten_mul = list(map(lambda x: x * 10, l)) # map returns a list of the results of applying the given function to the items of the given iterable.

ten_multiples = list(filter(lambda x: x % 10 == 0, l)) # filter returns an iterable of elements for which the function returns True, 

mul = reduce(lambda x, y: x * y, l) # reduce returns a single value by combining the items of the iterable using the given function.



def main():
    print(l)
    print(ten_mul)
    print(ten_multiples)
    print(mul)

if __name__ == '__main__':
    main()