from pythonds.basic.stack import Stack

# 问题: 十进制转换成二进制。如233^10，对应的二进制为11101001^2。
# 步骤: 重复除以2，将余数压到栈上，二进制的数需要将余数从栈中取出并进行拼接。
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(42))
