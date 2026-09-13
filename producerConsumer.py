import threading
import time

buffer = []
MAX_SIZE = 3

condition = threading.Condition()


def producer():
    for i in range(1, 6):
        with condition:
            while len(buffer) == MAX_SIZE:
                condition.wait()

            buffer.append(i)
            print("Produced:", i)

            condition.notify()

        time.sleep(1)


def consumer():
    for i in range(1, 6):
        with condition:
            while len(buffer) == 0:
                condition.wait()

            item = buffer.pop(0)
            print("Consumed:", item)

            condition.notify()

        time.sleep(1.5)


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Production and consumption completed.")

