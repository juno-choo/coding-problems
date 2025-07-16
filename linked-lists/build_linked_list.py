class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, val):
        node = Node(val, self.head)
        self.head = node

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.val) + ' --> '
            itr = itr.next
            if itr is None:
                llstr += 'None'

        print(llstr)

    def insert_at_end(self, val):
        if self.head is None:
            self.head = Node(val, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(val, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def find_middle(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val




if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_values(["banana", "mango", "orange", "apple", "figs", "strawberry"])
    linked_list.print_list()
    linked_list.remove_at(2)
    linked_list.print_list()
    print("Length of linked list: ", linked_list.get_length())
    print("Middle of linked list: ", linked_list.find_middle())
    
    