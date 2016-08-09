class Queue(object):
    def __init__(self):
        self.lst=[]


    def deco(self,func):
        def foo():
            print self.lst
            func()
            print self.lst
        return foo

    def empty(self):
        return self.lst==[]

    def enq(self,data):
        print 'Before',self.lst
        self.lst.append(data)
        print 'After:',self.lst
    
    def delq(self):
        print 'Before',self.lst
        if self.empty():
            return None
        else:
            self.lst.pop(0)
        print 'After:',self.lst

    def fontq(self):
        print self.lst
        if self.empty():
            return None
        else:
            print self.lst[0]

    def lengt(self):
        print self.lst
        return len(self.lst)
