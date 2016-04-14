from Node import Node
import threading

class Message():
    #del = 0
    #insert = 1
    def __init__(self, _type, pos, char):
        self._type = _type
        self.pos = pos
        if self._type == 1:
            self.char = char
        self.vt = []

class CBCAST():
    def __init__(self, queue, node, ui):
        self.queue = queue
        self.node = node

    def delay(self, message):
        for i in range(0, len(node.get_peers())):
            if i == message.sender:
                if (node.vt[i] + 1) != message.vt[i]:
                    return True
            else:
                if message.vt[i] > node.vt[i]:
                    return True

        return False

    def recv_cbcast(self, message):
        if not self.delay(message):
            self.queue.put(message)
        else:
            self.deliver(message)

    def queue_batch_routine(self):
        index = self.queue.qsize() - 1
        while index >= 0:
            index -= 1
            message = self.queue.get_nowait()
            if not self.delay(message):
                self.deliver(message)
            else:
                self.queue.put(message)

    def deliver(self, msg):
        #update vt in msg
        if msg._type == 0:
            gui.
        pass



class CommunicationModule():
    def __init__(self, queue, _id):
        self.queue = queue
        self.vt = []
        self.cbcast = CBCAST(queue, self)
        self.ports = [10001, 10002, 10003]
        self._id = _id
        self.node = Node(self.ports[_id])

    def run(self):
        t = threading.Thread(target = self.node.mainloop,
                args = [])
        t.start()


