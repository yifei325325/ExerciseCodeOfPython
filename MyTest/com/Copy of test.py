# -*- coding: utf-8 -*-
import threading

class MyThread(object):
    def __init__(self, thread_num):
        self.thread_num = thread_num        # 线程个数
        self.outLock = threading.Lock()     # 控制台输出锁
        self.threads = []                   # 线程列表
        self.interruptEvent = threading.Event() # 键盘中断事件
    
    def beginTask(self):
        # 将线程加入线程列表
        for i in range(self.thread_num):
            t_name = str(i + 1)
            thread = threading.Thread(target=self.doSomething, kwargs={"t_name": t_name})
            self.threads.append(thread)

        # 启动线程
        for thread in self.threads:
            thread.start()
        self.interruptEvent.clear()             # clear
        # 用 isAlive 循环判断代替线程的 join 方法
        
        while True:
            try:
                alive = False
                for thread in self.threads:
                    alive = alive or thread.isAlive()
                if not alive:
                    break
            except KeyboardInterrupt:
                self.interruptEvent.set()           # set
    
    def doSomething(self, t_name):
        self.outLock.acquire()
        print u"线程 %s 已启动" % t_name
        self.outLock.release()
        while True:
            try:
                if self.interruptEvent.isSet():     # isSet
                    raise KeyboardInterrupt
                ########################
                # doSomething 函数代码 #
                ########################
            except KeyboardInterrupt:
                ##################
                # 处理最后的工作 #
                ##################
                self.outLock.acquire()
                print u"用户强制中止主线程，线程 %s 已中止" % t_name
                self.outLock.release()                
                break
        self.outLock.acquire()
        print u"线程 %s 已停止" % t_name
        self.outLock.release()
        
                        
if __name__ == "__main__":
    t = MyThread(5)
    t.beginTask()