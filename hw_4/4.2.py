import math
import time
import os
import logging

from typing import Any, Callable, Tuple

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def configure_logging():
    artifacts_dir = os.path.join(os.getcwd(), "hw_4", "artifacts", "4.2")
    logging.basicConfig(
        filename=os.path.join(artifacts_dir, "outputs.log"), level=logging.INFO
    )


def helper_integrate_part(arguments: Tuple) -> float:
    """
    helper to pass multiple arguments to integrate_part in executor
    """
    return integrate_part(*arguments)


def integrate_part(
    f: Callable[[float], float],
    a: float,
    step: float,
    n_jobs: int,
    n_iter: int,
    part_i: int,
) -> float:
    configure_logging()
    part_step = n_iter // n_jobs
    shift = part_step * part_i

    logging.info(f"Integration with process/thread number {part_i} was started")
    start_time = time.time()
    res = sum(
        f(a + i * step) * step for i in range(shift, min(shift + part_step, n_iter))
    )
    end_time = time.time()
    logging.info(
        f"Integration with process/thread number {part_i} was finished in {end_time-start_time}"
    )
    return res


def integrate(
    f: Callable[[float], float],
    a: float,
    b: float,
    *,
    n_jobs: int = 1,
    n_iter: int = 10_000_000,
    executor_class: Any = ThreadPoolExecutor,
) -> float:
    step = (b - a) / n_iter

    executor = executor_class(max_workers=n_jobs)
    return sum(
        executor.map(
            helper_integrate_part,
            [(f, a, step, n_jobs, n_iter, part_i) for part_i in range(n_jobs)],
        )
    )


def run_integration(n_jobs: int, executor_class: Any = ThreadPoolExecutor) -> float:
    logging.info(
        f"Starting integration with {n_jobs} workers using {executor_class.__name__}"
    )

    start_time = time.time()
    result = integrate(
        math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_class=executor_class
    )
    end_time = time.time()

    logging.info(
        f"Finished integration with {n_jobs} workers using {executor_class.__name__} in {end_time-start_time:.2f}, result is {result}\n"
    )
    return end_time - start_time


if __name__ == "__main__":
    artifacts_dir = os.path.join(os.getcwd(), "hw_4", "artifacts", "4.2")

    logging.basicConfig(
        filename=os.path.join(artifacts_dir, "outputs.log"), level=logging.INFO
    )

    with open(os.path.join(artifacts_dir, "results.txt"), "w") as f:
        f.write(
            f"{'n_jobs':^8s} | {'ThreadPoolExecutor':^20s} | {'ProcessPoolExecutor':^20s}\n"
        )
        for n_jobs in range(1, os.cpu_count() * 2 + 1):
            thread_exec_time = run_integration(n_jobs, ThreadPoolExecutor)
            process_exec_time = run_integration(n_jobs, ProcessPoolExecutor)
            f.write(
                f"{n_jobs:^8d} | {thread_exec_time:^20.4f} | {process_exec_time:^20.4f}\n"
            )
