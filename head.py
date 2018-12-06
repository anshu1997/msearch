class Node(object):
    def __init__(self, data,typ):
        self.data = data
        self.typ = typ
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.data['title'])+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret