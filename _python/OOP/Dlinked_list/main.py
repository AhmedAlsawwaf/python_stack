class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev =temp
        return self
    
    def delete(self,data):
        if self.head is None :
            print("This list is empty, nothing to delete")
            return self
        
        if self.head.data == data:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return self
        current =self.head
        
        while current:
            if current.data ==data:
                break
            current =current.next
        if current is None:
            print("Cannot find the element you want to delete")
            return self
        if current.prev :
            current.prev.next = current.next
        if current.next:
            current.next.prev= current.prev
        return self
    
    def insert_before(self, existing_data, new_data):
        if self.head is None:
            print("List is empty")
            return self
            
        if self.head.data == existing_data:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node   
            return self
            
        current = self.head
        while current:
            if current.data == existing_data:
                break
            current = current.next
            
        if current is None:
            print(f"Node {existing_data} not found")
            return self
            
        new_node = Node(new_data)
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        
        return self
    
    def traversal_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end="<-->")
            temp=temp.next
        print("None")
        return self
    
    def traversal_backward(self):
        temp =self.head
        if not temp:
            print("This list is empty")
            return self
        while temp.next :
            temp =temp.next
        while temp:
            print(temp.data, end="<-->")
            temp=temp.prev
        print("None")
        return self

dll = DoublyLinkedList()
dll.append(1).append(2).append(3).append(4).append(5).append(6)
dll.delete(3)
dll.insert_before(1,"ahmed")
dll.traversal_forward()
dll.traversal_backward()