import time
import threading
import multiprocessing

import os


def fibonacci(n: int) -> int:
    return 1 if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def run_sync(n: int, iters: int) -> float:
    start = time.time()
    for _ in range(iters):
        fibonacci(n)
    end = time.time()
    return end - start


def run_thread(n: int, iters: int) -> float:
    start = time.time()
    threads = []
    for _ in range(iters):
        t = threading.Thread(target=fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return end - start


def run_process(n: int, iters: int) -> float:
    start = time.time()
    processes = []
    for _ in range(iters):
        p = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    return end - start


if __name__ == "__main__":
    n = 40
    sync_time = run_sync(n, 10)
    thread_time = run_thread(n, 10)
    process_time = run_process(n, 10)

    artifacts_dir = os.path.join(os.getcwd(), "hw_4", "artifacts", "4.1")
    with open(os.path.join(artifacts_dir, "results.txt"), "w") as f:
        # write to file in table format
        f.write(f"{'Sync: ':10s}{sync_time:.8f}\n")
        f.write(f"{'Thread: ':10s}{thread_time:.8f}\n")
        f.write(f"{'Process: ':10s}{process_time:.8f}")
