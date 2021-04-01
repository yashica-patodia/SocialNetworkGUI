def multiply(*args):
    prod = 1
    for n in args:
        prod *= n
    print(prod)

if __name__=='__main__':
    multiply(3,4)
    multiply(3,4,5)
    multiply(3,4,5,6)
