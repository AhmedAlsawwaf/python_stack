class SLNode:
    def __init__(self,val):
        self.value = val
        self.next = None
class SList: 
    def __init__(self):
        self.head = None
    def add_to_front(self,val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def add_to_back(self,val):
        if self.head is None:
            self.add_to_front(val)
            return self
        
        new_node = SLNode(val)
        runner = self.head
        while(runner.next is not None):
            runner =runner.next
        runner.next = new_node
        return self
    def print_values(self):
        runner = self.head
        while(runner is not None):
            print(runner.value)
            runner = runner.next
        return self
    def remove_from_front(self):
        if self.head is None:
            raise Exception("Cannot remove from empty list")

        removed_value = self.head.value
        print(f"Removed value is {removed_value}")
        self.head = self.head.next
        return self
    def remove_from_back(self):
        if self.head is None:
            raise Exception("Cannot remove from empty list")
        
        if self.head.next is None:
            removed_value = self.head.value
            print(f"Removed value is {removed_value}")
            self.head = None
            return self
        
        runner = self.head
        while runner.next.next is not None:
            runner = runner.next
        
        removed_value = runner.next.value
        print(f"Removed value is {removed_value}")
        runner.next = None
        return self
    def remove_val(self, val):
        if self.head is None:
            raise Exception("Cannot remove from empty list")
        
        if self.head.value == val:
            self.head = self.head.next
            return self
        
        runner = self.head
        while runner.next is not None:
            if runner.next.value == val:
                runner.next = runner.next.next
                return self
            runner = runner.next
        
        raise Exception(f"Value {val} not found in list")
    def insert_at(self, val, n):
        if n < 0:
            raise Exception("Position cannot be negative")
            
        if n == 0:
            self.add_to_front(val)
            return self
        
        new_node = SLNode(val)
        runner = self.head
        current_pos = 0
        
        while runner is not None and current_pos < n - 1:
            runner = runner.next
            current_pos += 1
        
        if runner is None:
            raise Exception("Position exceeds list length")
        
        new_node.next = runner.next
        runner.next = new_node
        return self
my_list = SList()
try:
    my_list.add_to_front("Yousef").add_to_front("Ahmed").add_to_back("Ibrahim").add_to_back("Alsawwaf").remove_from_front().remove_from_back().remove_val("Ibrahim").insert_at("Eng",1).print_values()
except Exception as e:
    print(f"error : {e}")
