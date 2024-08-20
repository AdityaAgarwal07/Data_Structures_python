class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->" if itr.next else str(itr.data)
            itr = itr.next

        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self,data):
        for i in data:
            self.insert_at_end(i)

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_start(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next


    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count  += 1
            itr = itr.next



ll = LinkedList()
ll.insert_at_start(10)
ll.insert_at_start(11)
ll.insert_at_start(12)
ll.insert_at_start(13)
ll.insert_at_start(14)
ll.insert_values([45,7,12,567,99])
ll.insert_at(1,123)
ll.remove_at(1)
ll.print()
print(ll.get_length())






