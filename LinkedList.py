class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self,val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def pop(self):
        if self.head is None:
            raise Exception("No Value")

        if self.head.next is None:
            print("Case 1")
            val = self.head.val
            self.head = None
            return val

        print("Case 2")
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next

        val = temp.val
        prev.next = None
        return val

    def remove(self,val):
        temp = self.head

        if temp == None:
            raise Exception("List is Empty")

        if temp.val == val:
            # Case 1

            self.head = temp.next
            temp = None
            return

        while temp is not None:
            if temp.val == val:
                break

            prev = temp
            temp = temp.next


        #Case 2

        prev.next = temp.next
    
    def len(self):
        temp = self.head
        counter = 0
        while temp is not None:
            counter+=1
            temp = temp.next

        return counter

    def get(self,index):
        counter = 0
        temp = self.head

        if index == 0:
            return temp.val

        while temp.next is not None:
            counter += 1
            prev = temp
            temp = temp.next

            if counter == index:
                return temp.val

            if temp.next == None:
                raise IndexError("List index out of range")

    def __str__(self):
        r_str = '['
        temp = self.head
        while temp is not None:
            r_str += str(temp.val) + ','
            temp = temp.next

        r_str = r_str.strip(',')
        r_str += ']'
        return r_str

    def reverse_list(self):
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev

if __name__ == '__main__': 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    l.push(3)

    print(l)

    l.reverse_list() 
    print(l)

