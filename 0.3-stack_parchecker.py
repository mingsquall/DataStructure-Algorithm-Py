from pythonds.basic.stack import Stack
def parchecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1
    # 当所有符号被处理后，栈应该是空的
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parchecker('((()))'))
print(parchecker('(()'))
