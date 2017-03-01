# coding:utf-8
# __author__ = 'guyu'
class MyDict(dict):   #有序字典实现

    def __init__(self):
        self.li = []
        super(MyDict,self).__init__()

    def __setitem__(self, key,value):
        self.li.append(key)
        super(MyDict,self).__setitem__(key,value)

    def __str__(self):
        temp_list = []
        for key in self.li:
            value = self.get(key)
            temp_list.append("'%s':%s" %(key,value,))
        temp_str = '{' + ','.join(temp_list) + '}'
        return temp_str
obj = MyDict()
obj['k1'] = 123
obj['k2'] = 456
print(obj)