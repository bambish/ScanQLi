import sys
import time

class progressbar():
    def __init__(self, typestat, status, totalcount=1, count=1, text = None):
        self.typestat = typestat
        self.status = status
        self.total = 1
        self.value = 0
        self.totalcount = totalcount
        self.count = count
        self.text = text

    def delline(self, n=1):
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        for _ in range(n):
            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)
    
    def progress(self, addvalue = 0):
        bar_len = 60
        self.value += addvalue
        if self.typestat == "bar":
            filled_len = int(round(bar_len * self.value / float(self.total)))
            percents = round(100.0 * self.value / float(self.total), 1)
            bar = '#' * filled_len + '.' * (bar_len - filled_len)
            sys.stdout.write('%s [%s/%s][%s%s] [%s]      \r' % (self.status, self.count, self.totalcount, percents, '%', bar))
        elif self.typestat == "textbar":
            filled_len = int(round(bar_len * self.value / float(self.total)))
            percents = round(100.0 * self.value / float(self.total), 1)
            bar = '#' * filled_len + '.' * (bar_len - filled_len)
            sys.stdout.write('%s\n%s [%s/%s][%s%s] [%s]      \r' % (self.text, self.status, self.count, self.totalcount, percents, '%', bar))
        elif self.typestat == "count":
            sys.stdout.write('%s [%s]\r' % (self.status, self.value))
            

    def printabove(self, text):
        print("")
        self.delline()
        print(text)
        self.progress(0)

    def delbar(self, n = 1):
        print("")
        self.delline(n)