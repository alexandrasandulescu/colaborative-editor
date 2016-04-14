import socket
import traceback

class Node():
    def __init__(self, port):
        self.shutdown = False
        self.socket = socket.socket(socket.AF_INET,
                socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,
                socket.SO_REUSEADDR, 1)
        self.socket.bind(('', port))
        self.socket.listen(2)

    def __debug(self, msg):
        print('[DEBUG]' + msg)

    def __handlepeer(self, clientsock):
        self.__debug( 'New child ' + str(threading.currentThread().getName()) )
        self.__debug( 'Connected ' + str(clientsock.getpeername()) )

        host, port = clientsock.getpeername()
        # receive data
        # update pq
        self.__debug(clientsock.recv(100))

    #def __handlesend(self, clientsock):
    #    pass

    #def connectandsend(self, clientsock, msg):
    #    self.sendsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #    self.sendsock.connect(clientsock.getpeername())
    #    sd = self.sendsock.makefile('rw', 0)
    #    sd.write(msg)
    #    sd.flush()
    #    self.sendsock.close()
    #    sd = None

    def mainloop(self):
        while not self.shutdown:
            try:
                self.__debug( 'Listening for connections...' )
                clientsock, clientaddr = self.socket.accept()
                clientsock.settimeout(None)

                #start listening thread
                t = threading.Thread( target = self.__handlepeer,
                                      args = [ clientsock ] )
                t.start()

            except KeyboardInterrupt:
                print('KeyboardInterrupt: stopping mainloop')
                self.shutdown = True
                continue
            except:
                traceback.print_exc()
                continue

        # end while loop
        self.__debug( 'Main loop exiting' )
