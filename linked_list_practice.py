class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()


    def append(self, data):
        new_node = node(data)
        current = self.head

        while current.next!=None:
            current = current.next
        current.next = new_node


    def length(self):
        sum_len = 0
        current = self.head



        while current.next!=None:
            sum_len += 1
            current = current.next

        return sum_len


    def display(self):
        current = self.head
        elements = []
        while current.next!=None:
            current = current.next
            elements.append(current.data)
            
        print(elements)


    def get(self, index):
       current = self.head

       i = 0

       while current.next != None:
           current = current.next

           if i==index:
             return current.data
          
           i += 1

    def erase(self, index):
        current = self.head

        current_index = 0

        while True:
            previous_node = current
            current = current.next
            
            if current_index == index:
               previous_node.next = current.next
               return None
            current_index += 1    

if __name__ == '__main__':
    my_list = linked_list()

    my_list.display()


    my_list.append(1)
    my_list.append(8)
    my_list.append(3)
    my_list.append(7)
    my_list.display()



    print("list index: ", my_list.get(2))


    my_list.erase(2)
    my_list.display()
