'''
                        |        Linked list       |      Array
-----------------------------------------------------------------                                
Indexing                |          O(1)            |        O(n)
insert/del at start     |          O(n)            |        O(1)
Insert/del at end       |          O(n)+O(1)       |        O(n)
Insert/del at middle    |          O(n)            |        O(n) 

'''
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    def beg(self,data):
        node = Node(data, self.head)
        self.head = node

    def end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
                
    def print(self):
        if self.head is None:
            print('linked list empty')
            return
        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
            
        print(llstr)




if __name__ == '__main__':
    ll = LinkedList()
    #ll.end(5)
    #ll.beg(14)
    #ll.end(10)
    ll.print()
