from UIModule import start_ui
import threading
import queue

def main():
    q = queue.Queue(maxsize=100)
    ui_thread = threading.Thread(target = start_ui,
            args = [q])
    ui_thread.start()


if __name__ == "__main__":
    main()
