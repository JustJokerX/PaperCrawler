# -*- coding:utf-8 -*-

import sys


class ProgressBar:
    def __init__(self, count=0, total=0, width=50):
        self.count = count
        self.total = total
        self.width = width

    def update(self, step=1, index=0):
        if 0 == index:
            self.count += step
        else:
            self.count = index

    def log(self, s):
        sys.stdout.write(' ' * (self.width + 11) + '\r')
        sys.stdout.flush()
        print(s)
        progress = self.width * self.count / self.total
        sys.stdout.write('[{:.2%}]: '.format((self.count * 1.0 + 0.0001) /
                                             self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()

    def finish(self):
        self.log('finished')
