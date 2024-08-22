class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.prev = previous


class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head, None)
        if self.head:
            self.head.prev = node
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            if itr.prev is None:
                llstr += "None " + "<-- |" + str(itr.data) + "| -->"
            else:
                llstr += "<-- |" + str(itr.data) + "| -->"

            if itr.next is None:
                llstr += " None"

            itr = itr.next

        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(data, None, itr)
        itr.next = node

    def insert_values(self, data):
        for i in data:
            self.insert_at_end(i)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_start(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break
            count += 1
            itr = itr.next


# Example usage
dll = Doubly_Linked_List()
dll.insert_at_start(23)
dll.insert_at_start(24)
dll.insert_at_start(25)
dll.insert_at_start(26)
dll.insert_at_end(22)
dll.insert_values([45, 7, 12, 567, 99])
dll.insert_at(1, 100)
dll.remove_at(0)

dll.print()
print(dll.get_length())
