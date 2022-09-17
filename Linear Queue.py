#linear queue 有口有屁眼 头出尾进
class queue:
    def __init__(self):
        self.Headpointer = 0
        self.Freepointer = 0
        self.Tailpointer = 0
        self.array = [None, None, None, None, None]

#从左加
    def leftenqueue(self, data):#添加queue要判断是不是满的
        #是空队列
        if self.Freepointer == self.Headpointer and self.Headpointer == 0 and self.Headpointer == self.Tailpointer:
            self.array[self.Freepointer] = data
            self.Freepointer = self.Freepointer + 1
        else:
        #不是空队列
            if self.Freepointer == self.Tailpointer:
                return ("It's full, cannot put in")
            else:
                self.array[self.Freepointer] = data
                self.Freepointer = self.Freepointer + 1
                if self.Tailpointer != len(self.array):
                    self.Tailpointer = self.Tailpointer + 1

#从右加
    def rightenqueue(self, data):#添加queue要判断是不是满的
        if self.Freepointer == self.Tailpointer:
            return ("It's full, cannot put in")
        else:
            self.array[self.Freepointer] = data
            self.Freepointer = self.Freepointer - 1
            self.Tailpointer = self.Tailpointer - 1



#从左边丢
    #头固定死, 整体从5位变成4位, 所以要补位
    def lockleftdequeue(self):#删除queue要判断是不是空
        #是空队列
        if self.Freepointer == self.Headpointer:
            return ("queue is empty")
        else:
            #不是空，但是是满的
            if self.Tailpointer == len(self.array):
                self.Headpointer.pop(0)
                self.Tailpointer = self.Tailpointer -1
                self.array.append(None)
            else:
            #不是空，但是也不是满的
                self.Headpointer.pop(0)
                self.Tailpointer = self.Tailpointer - 1
                self.Freepointer = self.Freepointer - 1
                self.array.append(None)

    #头不固定死，当把头pop出去后，将Headpointer赋给下一个
    def unlockleftdequeue(self):#删除queue要判断是不是空
        # 是空队列
        if self.Freepointer == self.Headpointer:
            return ("queue is empty")
        else:
            self.array[self.Headpointer] = None
            self.Headpointer = self.Headpointer + 1

#从右边丢
    #从右边丢是以右边为头，删除要变Headpointer
    def rightdequeue(self):#删除queue要判断是不是空
        # 是空队列
        if self.Freepointer == self.Headpointer:
            return ("queue is empty")
        else:
            self.Tailpointer.pop()
            self.array.append(None)
            self.Headpointer = self.Headpointer - 1