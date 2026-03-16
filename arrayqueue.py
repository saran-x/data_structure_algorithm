# Arrayqueue

class array_queue:

    # creating a queue and size
    def __init__(self):
        self.queue = []
        self.size = 10
        self.rear = -1
        self.front = -1

    # inserting a queue
    def enqueue(self,data):

        # inserting a first value
        if self.front == -1 and self.rear == -1:
            print(f"Inserting a first value : {data}")
            self.queue.append(int(data))
            self.front += 1
            self.rear += 1
        
        else:
            print(f"Inserting a value : {data}")
            self.queue.append(data)
            self.rear +=1
    
        print(f"Queue value : {self.queue}")

    # dequeue array
    def dequeue(self):

        # whether check queue is empty
        if self.front == -1 and self.rear == -1:
            print("Queue is empty!")
            return
        
        # whether front and rear point with first value
        if self.front == self.rear:
            print(f"Delete the value : {self.queue[self.front]}")
            self.queue.pop(self.front)
            self.front -= 1
            self.rear -= 1
            return
        
        # delete the first element
        print(f"Delete the value : {self.queue[self.front]}")
        self.queue.pop(self.front)
        self.rear -= 1
            

args = array_queue()
# Inserting a value
args.enqueue(10)
args.enqueue(20)
args.enqueue(30)
args.enqueue(40)

# delete the first value
args.dequeue()