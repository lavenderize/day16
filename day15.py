def isStackFull():
    global SIZE, stack, top
    if top >= SIZE - 1:
        return True
    else:
        return False


def isStackEmpty():
    global SIZE, stack, top
    if top == - 1:
        return True
    else:
        return False


def push(data):
    global SIZE, stack, top
    if isStackFull():
        print("Stack is FULL!")
        return
    top = top + 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print("Stack is EMPTY")
        return
    temp = stack[top]
    stack[top] = None
    top = top - 1
    return temp


def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print("Stack is EMPTY")
        return None
    return stack[top]


SIZE = int(input("Stack Size: "))
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    select = input("Insert(I)/Extract(E)/Verify(V)/eXit(X) ==> ")

    while select != 'X' and select != 'x':
        if select == 'I' or select == 'i':
            data = input("Input Data ==> ")
            push(data)
            print("Stack Status : ", stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print("Extracted Data ==> ", data)
            print("Stack Status : ", stack)
        elif select == 'V' or select == 'v':
            data = peek
            print("Check Data ==> ", data)
            print("Stack Status : ", stack)
        else:
            print("Input Mismatched!")

        select = input("nsert(I)/Extract(E)/Verify(V)/eXit(X) ==> ")

    print("End of Program")
