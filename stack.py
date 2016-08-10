class Stack(object):
    def __init__(self):
        self.lst=[]

    def isEmpty(self):
        return len(self.lst)==0

    def push(self,item):
        print 'before:',self.lst
        self.lst.append(item)
        print 'after:',self.lst

    def pop(self):
        print 'before:',self.lst
        self.lst.pop()
        print 'after:',self.lst

    def peek(self):
        if not self.isEmpty():
            return self.lst[len(self.lst)-1]

    def size(self):
        print self.lst
        return len(self.lst)
