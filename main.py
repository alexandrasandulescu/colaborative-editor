from UIModule import start_ui
from CommunicationModule import CommunicationModule
import threading
import queue
import sys

def main():
    if len(sys.argv) < 2:
        print('Fail! specify node id')
        return 1

    _id = int(sys.argv[1])
    if _id < 0 or _id > 2:
        print('Wrong id! Choose in [0, 2]')
        return 1


    q = queue.Queue(maxsize=100)
    ui_thread = threading.Thread(target = start_ui,
            args = [q])
    ui_thread.start()

    cm = CommunicationModule(q, _id)
    cm.run()

if __name__ == "__main__":
    main()
