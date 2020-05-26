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

def main():
    a = int(input("请输入乘数:"))
    b = int(input("请输入模数:"))

    if b < 0:
        m = abs(b)
    else:
        m = b
    gcd, x, y = extgcd(a, b)

    # 判断最大公约数是否为1，若不是则没有逆元
    if gcd == 1:

        x0 = x % m
        return x0
    else:
        print("不存在逆元!")
        return False

if __name__ == "__main__":

    inverseNum = main()
    if inverseNum:
        print("乘法逆元为:{}".format(inverseNum))