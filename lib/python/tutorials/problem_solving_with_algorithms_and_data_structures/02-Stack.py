class Stack:
    """Docstring for Stack """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def push(self,item):

        self.items.append(item)

    def pop (self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def revstring(mystr):
    st = Stack()
    reverse = ""
    for letter in mystr:
        st.push(letter)
    while st.isEmpty() == False:
        reverse += st.pop()
    print (reverse)
#revstring("apple")


##Balanced Symbolys##
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)
def parChecker(symbolString):
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
                if not matches(top,symbol):
                    balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
#print(parChecker('((()))'))
#print(parChecker('(()'))


##Converting Decimal Numbers to Binary Numbers##
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binString = ""
    while not remstack.isEmpty():
        binString = binString + digits[remstack.pop()]

    return binString
#print(baseConverter(160,16))


##General Infix-to-Postfix Conversion##

