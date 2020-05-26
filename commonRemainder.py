#solve function : ax = b (mod m)
#extend euclid method

def extgcd(b, n):
    '''
    :param a:integer
    :param b:integer
    calculate ax + by = gcd(a,b)
    :return: x0 :coefficient, r0: gcd(a,b)
    '''
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return b, x0, y0

def linearEquation(a, b, n):

    solutionList = []
    gcd, x ,y = extgcd(a, n)
    # print(x, r)
    if b % gcd != 0:
        return False
    else:
        for i in range(gcd):
            x = b // gcd * x + n // gcd * i
            x = x % n
            if x < 0:
                x += n
            solutionList.append(x)

        return solutionList

def main():
    a = int(input("请输入a:"))
    b = int(input("请输入b:"))
    n = int(input("请输入n:"))
    result = linearEquation(a, b, n)
    if result != False:
        print('结果为:{}'.format(result))
    else:
        print("无解!")

if __name__ == "__main__":
    main()