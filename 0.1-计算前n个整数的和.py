import time
# 问题：计算前n个整数的和，并计算耗费时间
# 1 方法1：迭代方法
def sumOfN1(n):
    start = time.time()

    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i

    end = time.time()

    return theSum, end - start

for n1 in range(5):
    print("Sum is %d required %.7f seconds " % (sumOfN1(1000000)))

# 2 方法2：封闭方程 执行时间和n无关
def sumOfN2(n):
    start = time.time()
    theSum = 0
    sumResult = (n*(n+1))/2
    end = time.time()
    return sumResult, end - start

for n2 in range(5):
    print("Sum is %d required %.7f seconds " % (sumOfN2(1000000000)))

