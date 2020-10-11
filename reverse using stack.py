def createStack():
    stack = []
    return stack



def push(stack,item):
    stack.append(item)

def pop(stack):

        return stack.pop()

def reverse(string):
    n = len(string)
    stack = createStack()
    for i in range(0,n,1):
        push(stack,string[i])
    string = ''
    for i in range(0,n,1):
        string = string + pop(stack)
    return string


a = 'shahzaib'
b = reverse(a)
print(b)
