import concurrent.futures
import time


# Define a function to be executed in parallel
def task_function(task_id):
    print(f"Task {task_id} started")
    time.sleep(2)
    # Simulate some work
    result = task_id * 2
    print(f"Task {task_id} completed: Result = {result}")
    return result


def main():
    # Number of threads in the thread pool
    num_threads = 5

    # Create a thread pool with the specified number of threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Submit tasks to the thread pool
        futures = [executor.submit(task_function, i) for i in range(1, 6)]

        # Wait for all tasks to complete and retrieve their results
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(f"Task result: {result}")


if __name__ == "__main__":
    main()
