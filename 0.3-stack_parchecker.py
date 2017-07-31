from pythonds.basic.stack import Stack

# 问题1: 简单括号"()"匹配。
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


# 问题2: 符号匹配"([{"。
def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

def parchecker_pro(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parchecker_pro('{{([][])}()}'))
print(parchecker_pro('[{()]'))
