from multiprocessing import Process, Queue
import time
import logging
import os

import codecs

START_TIME = time.time()


def configure_logging():
    artifacts_dir = os.path.join(os.getcwd(), "hw_4", "artifacts", "4.3")
    logging.basicConfig(
        filename=os.path.join(artifacts_dir, "outputs.log"), level=logging.INFO
    )


def process_a(queue_in, queue_out):
    configure_logging()
    while True:
        if not queue_in.empty():
            message = queue_in.get()
            logging.info(
                f"{time.time()-START_TIME:8.4f}: Process A received message: {message}"
            )
            message = message.lower()
            logging.info(
                f"{time.time()-START_TIME:8.4f}: Process A is sending message: {message}"
            )
            queue_out.put(message)
            time.sleep(5)


def process_b(queue_in, queue_out):
    configure_logging()
    while True:
        if not queue_in.empty():
            message = queue_in.get()
            logging.info(
                f"{time.time()-START_TIME:8.4f}: Process B received message: {message}"
            )
            message = codecs.encode(message, "rot_13")
            print(message)
            logging.info(
                f"{time.time()-START_TIME:8.4f}: Process B is sending message: {message}"
            )
            queue_out.put(message)


if __name__ == "__main__":
    configure_logging()

    Main_queue = Queue()
    A_queue = Queue()
    B_queue = Queue()

    p_a = Process(target=process_a, args=(A_queue, B_queue))
    p_b = Process(target=process_b, args=(B_queue, Main_queue))

    p_a.start()
    p_b.start()

    while True:
        message = input()
        if len(message) != 0:
            logging.info(
                f"{time.time()-START_TIME:8.4f}: Main process is sending message: {message}"
            )
            A_queue.put(message)

        if not Main_queue.empty():
            message = Main_queue.get()
            logging.info(
                f"{time.time()-START_TIME:8.4f}: Main process received message: {message}"
            )
