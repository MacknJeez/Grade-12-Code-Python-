stack = []
queue = []
listType = input("Enter type of list [STACK/QUEUE]:")
while True:
    def isEmpty():
        if stack == []:
            return True
        else:
            return False
        
    def isEmptyQ():
        if queue == []:
            return True
        else:
            return False

    def add():
        stack.append(input("Add to Stack:"))
        
    def view():
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
            
    def delete():
        print(stack.pop(), ' deleted!')

    def addQ():
        queue.append(input('Add to Queue:'))
        
    def viewQ():
        print('Elements:')
        for i in queue:
            print (queue)
            
    def deleteQ():
            print(queue.pop(0), ' deleted!')
            
    print('''Menu:
    1.Add
    2.View
    3.Delete
    4. End''')
    ask = input('')
    if ask != 'end':
        
        if listType == 'STACK':
            if ask == 'add':
                add()
            elif ask == 'view':
                view()
            elif ask == 'delete':
                if isEmpty() == False:
                    delete()
                else:
                    print('List Empty')
        elif listType == 'QUEUE':
            if ask == 'add':
                addQ()
            elif ask == 'view':
                viewQ()
            elif ask == 'delete':
                if isEmptyQ() == False:
                    deleteQ()
                else:
                    print('List Empty')
    else:
        break
    
