#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        del self.items[:]

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[self.size()-1]


def revert_str(str):
    mystack = Stack()
    result = []
    for i in str:
        mystack.push(i)

    while mystack.size() > 0:
        result.append(mystack.pop())
    return ''.join(result)


if __name__ == '__main__':
    str = raw_input('you can input an unlimited str(split by blank):')
    str = str + ' '
    iter_str = iter(str)
    tmp_str = ''
    while True:
        try:
            tmp = iter_str.next()
            if not tmp.isspace():
                tmp_str += tmp
            else:
                print revert_str(tmp_str)
                tmp_str = ''
                continue
        except:
            break
    print '\nfinished'
