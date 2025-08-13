class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class DoubleLinkedList {
    constructor() {
        this.head = null;
    }
    
    append(value) {
        let new_node = new Node(value);
        if (this.head === null) {
            this.head = new_node;
            return this;
        }
        let temp = this.head;
        while (temp.next) {
            temp = temp.next;
        }
        temp.next = new_node;
        new_node.prev = temp;
        return this;
    }
    delete(value){
        if (this.head == null){
            console.log("This list is empty, nothing to delete");
            return this
        }
        if (this.head.value == value){
            if (this.head.next == null){
                this.head = null
            }
            else{
                this.head = this.head.next
                this.head.prev = null
            }
            return this
        }
        let current = this.head
        
        while (current){
            if (current.value ==value) break
            current =current.next
        }
        if (current == null){
            console.log("Cannot find the element you want to delete");
            return this
        }
        if (current.prev){
            current.prev.next = current.next
        }
        if (current.next){
            current.next.prev= current.prev
        }
        return this
    }
    
    traversal_forward() {
        let temp = this.head;
        let result = "";
        while (temp !== null) {
            result += temp.value + " <--> ";
            temp = temp.next;
        }
        result += "null";
        console.log(result);
        return this;
    }
    traversal_backward() {
        if (this.head === null) {
            console.log("null");
            return this;
        }
        let temp = this.head;
        while (temp.next) {
            temp = temp.next;
        }
        let result = "";
        while (temp !== null) {
            result += temp.value + " <--> ";
            temp = temp.prev;
        }
        result += "null";
        console.log(result);
        return this;
    }
    insert_before(existing_value , new_value){
        if(this.head == null){
            console.log("List is empty");
            return this
        }
        if (this.head.value == existing_value) {
            let new_node = new Node(new_value)
            new_node.next = this.head
            this.head.prev = new_node
            this.head =new_node
            return this
        }
        let current  = this.head
        while (current) {
            if (current.value == existing_value) break
            current = current.next
        }
        if (current == null){
            console.log(`Node ${existing_value} not found`);
            return this
        }
        let new_node = new Node(new_value)
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next =new_node
        current.prev = new_node
        return this
    }      
}

let dll = new DoubleLinkedList();
dll.append(1).append(2).append(3).append(4).append(5).append(6);
dll.delete(3)
dll.insert_before(5,22)
dll.traversal_forward();
dll.traversal_backward();