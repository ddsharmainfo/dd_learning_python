import concurrent.futures
import time


# Function that simulates a task that takes some time to complete
def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    print(f"Task {n} completed")
    return f"Task {n} result"


def main():
    # Create a ThreadPoolExecutor with 3 worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the thread pool
        future1 = executor.submit(task, 1)
        future2 = executor.submit(task, 2)
        future3 = executor.submit(task, 3)

        # Wait for tasks to complete and get their results
        results = [future.result() for future in concurrent.futures.as_completed([future1, future2, future3])]

        print("All tasks completed:")
        for result in results:
            print(result)


if __name__ == "__main__":
    main()
