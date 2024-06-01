import multiprocessing as mp
import threading
import time
from datetime import datetime
import psutil
import os

shared_value = mp.Value('i', 0)
lock = threading.Lock()


def get_current_cpu():
    try:
        p = psutil.Process(os.getpid())
        return p.cpu_num()
    except Exception as e:
        print(f"Error fetchign cpu cores: {e}")
        return None


def updated_shared():
    global shared_value
    with lock:
        shared_value.value += 1


def thread_fun(pid, tid):
    print(f"{datetime.now()} - Process {pid}, Thread {tid} started on CPU {get_current_cpu()}")
    for _ in range(5):
        updated_shared()
        time.sleep(1)
    print(f"{datetime.now()} - Process {pid}, Thread {tid} finished on CPU {get_current_cpu()}")


def process_func(pid, num_threads):
    print(f"{datetime.now()} - Process {pid} started on CPU {get_current_cpu()}")

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=thread_fun, args=(pid, i+1))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print(f"{datetime.now()} - Process {pid} finished on CPU {get_current_cpu()}")


if __name__ == "__main__":
    num_processes = 3
    num_threads = 2
    processes = []

    for i in range(num_processes):
        process = mp.Process(target=process_func, args=(i+1, num_threads))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


# Response:
# 2024-06-01 17:31:17.075763 - Process 1 started on CPU 0
# 2024-06-01 17:31:17.076210 - Process 2 started on CPU 6
# 2024-06-01 17:31:17.076370 - Process 1, Thread 1 started on CPU 0
# 2024-06-01 17:31:17.076544 - Process 1, Thread 2 started on CPU 0
# 2024-06-01 17:31:17.076744 - Process 2, Thread 1 started on CPU 6
# 2024-06-01 17:31:17.076712 - Process 3 started on CPU 5
# 2024-06-01 17:31:17.076850 - Process 2, Thread 2 started on CPU 6
# 2024-06-01 17:31:17.077156 - Process 3, Thread 1 started on CPU 5
# 2024-06-01 17:31:17.077246 - Process 3, Thread 2 started on CPU 5
# 2024-06-01 17:31:22.081386 - Process 1, Thread 1 finished on CPU 0
# 2024-06-01 17:31:22.081702 - Process 2, Thread 1 finished on CPU 6
# 2024-06-01 17:31:22.081876 - Process 3, Thread 2 finished on CPU 5
# 2024-06-01 17:31:22.081702 - Process 3, Thread 1 finished on CPU 5
# 2024-06-01 17:31:22.082294 - Process 2, Thread 2 finished on CPU 6
# 2024-06-01 17:31:22.082325 - Process 1, Thread 2 finished on CPU 3
# 2024-06-01 17:31:22.082517 - Process 2 finished on CPU 0
# 2024-06-01 17:31:22.082553 - Process 3 finished on CPU 2
# 2024-06-01 17:31:22.082680 - Process 1 finished on CPU 4

# Observations:
# - Process starts on a specific CPU.
# - Example: Process 1 starts on CPU 0, Process 2 on CPU 6, and Process 3 on CPU 5.
# - Process spawns multiple threads on a specific CPU.
# - Example: Process 1 spawns threads on CPU 0, Process 2 on CPU 6, and Process 3 on CPU 5.
# - Threads can start on one CPU and finish on another, showing dynamic scheduling.
# - Example: Process 1, Thread 2 starts on CPU 0 but finishes on CPU 3.
# - Entire process can also finish on different CPUs from where they started.
# - Example: Process 1 starts on CPU 0 but finishes on CPU 4.

# - Both processes and threads are not restricted to a single CPU throughout their execution.
# - This indicates the presence of context switching and load balancing by the OS scheduler.
# - Context switching allows processes and threads to move between CPUs, optimizing for load distribution and system efficiency.
# - Example: Process 1's threads finishing on different CPUs show the OS dynamically allocating resources.
# - Processes are executed concurrently across different CPUs, demonstrating effective multi-core utilization.
# - OS scheduler actively balances the load across CPUs, ensuring no single CPU is overwhelmed while others are idle.
# - Threads and processes can be shifted between CPUs to maintain optimal system performance.

# System Config:
# Ubuntu
# ➜ lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
# CPU(s):                             8
# Thread(s) per core:                 2
# Core(s) per socket:                 4
# Socket(s):                          1
# ➜ cat /proc/sys/kernel/pid_max
# 4194304
# ➜ ulimit -u (Maximum number of processes available to current user)
# 62545
